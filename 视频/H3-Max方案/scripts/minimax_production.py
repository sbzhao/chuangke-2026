#!/usr/bin/env python3
"""Project-scoped official MiniMax API client; never retries paid submissions.

Credentials are read only from the existing MMX configuration/environment.
Persist request intent before sending; resume saved video task IDs without resubmitting.
"""
import argparse
import base64
import datetime
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
API = 'https://api.minimax.cn'
MODEL = 'speech-2.8-turbo'
PEOPLE = {
    '张楚珺': 'zhangchujun', '张铭轩': 'zhangmingxuan',
    '汤兴昊': 'tangxinghao', '赵以清': 'zhaoyiqing', '王一初': 'wangyichu',
}
LINES = [
    ('M02_zhangchujun_arrival', '张楚珺', '抵达目标，进入伴飞。', 'calm'),
    ('M03_zhangchujun_rotation', '张楚珺', '自转周期，十五点九二小时。', 'calm'),
    ('M03_zhaoyiqing_reflection', '赵以清', '那道光，是它在转。', 'calm'),
    ('M04_zhangmingxuan_sample', '张铭轩', '稳住相对位置，准备采样。', 'calm'),
    ('M04_tangxinghao_pause', '汤兴昊', '角度不对，暂停接近。', 'calm'),
    ('M05_zhaoyiqing_steady', '赵以清', '它的自转……太稳了。', 'calm'),
    ('M05_tangxinghao_window', '汤兴昊', '窗口到了。', 'calm'),
    ('M06_tangxinghao_lock', '汤兴昊', '锁定，花瓣合拢。', 'calm'),
    ('M08_wangyichu_return', '王一初', '样本已封装，准备返航。', 'calm'),
    ('M08_zhaoyiqing_flash', '赵以清', '等等，那颗星，又闪了一下。', 'surprised'),
    ('M09_zhangmingxuan_look', '张铭轩', '再看它一眼。', 'calm'),
]

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)

def key():
    config = json.loads((Path.home() / '.mmx/config.json').read_text())
    value = os.environ.get('MINIMAX_API_KEY') or config.get('api_key')
    if not value:
        raise RuntimeError('No saved API key; use mmx auth login.')
    return value

def request(path, payload=None, multipart=None):
    headers = {'Authorization': 'Bearer ' + key()}
    body = None
    if payload is not None:
        headers['Content-Type'] = 'application/json'
        body = json.dumps(payload, ensure_ascii=False).encode()
    if multipart is not None:
        source = Path(multipart)
        boundary = 'MiniMaxProject' + uuid.uuid4().hex
        headers['Content-Type'] = 'multipart/form-data; boundary=' + boundary
        body = (f'--{boundary}\r\nContent-Disposition: form-data; name="purpose"\r\n\r\nvoice_clone\r\n'
                f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="sample.wav"\r\n'
                'Content-Type: audio/wav\r\n\r\n').encode() + source.read_bytes() + f'\r\n--{boundary}--\r\n'.encode()
    req = urllib.request.Request(API + path, data=body, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=240) as response:
            result = json.load(response)
    except urllib.error.HTTPError as error:
        try:
            detail = json.loads(error.read())
        except Exception:
            detail = {'message': 'Non-JSON HTTP error'}
        raise RuntimeError(json.dumps({'http_status': error.code, 'response': detail}, ensure_ascii=False)) from None
    code = result.get('base_resp', {}).get('status_code', 0)
    if code or result.get('type') == 'error':
        raise RuntimeError(json.dumps(result, ensure_ascii=False))
    return result

def download(url, target):
    target = Path(target)
    partial = target.with_suffix(target.suffix + '.part')
    with urllib.request.urlopen(url, timeout=240) as response, partial.open('wb') as output:
        while chunk := response.read(1024 * 1024):
            output.write(chunk)
    partial.replace(target)

def duration(path):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                         '-of', 'default=nw=1:nk=1', str(path)], text=True).strip())

def clone(name):
    path = ROOT / 'tasks' / ('voice_' + PEOPLE[name] + '.json')
    record = json.loads(path.read_text()) if path.exists() else {
        'person': name, 'voice_id': 'qukanyiyan_' + PEOPLE[name] + '_20261029a',
        'consent': 'User confirmed member and guardian consent for this film',
        'model': MODEL,
    }
    sample = ROOT / 'audio/samples' / (name + '.wav')
    if not sample.exists() or not 10 <= duration(sample) <= 300:
        raise RuntimeError('Missing or invalid prepared sample: ' + str(sample))
    if record.get('status') == 'cloned':
        print(name + ': reuse saved cloned voice', flush=True)
        return
    if record.get('status') in ('uploading', 'cloning', 'uncertain'):
        raise RuntimeError('Prior request uncertain; inspect record before any new POST: ' + str(path))
    if not record.get('file_id'):
        record.update(status='uploading', updated_at=now(), sample=str(sample.relative_to(ROOT)))
        save(path, record)
        result = request('/v1/files/upload', multipart=sample)
        record.update(file_id=result['file']['file_id'], status='uploaded', updated_at=now())
        save(path, record)
        print(name + ': sample uploaded', flush=True)
    text = next(line[2] for line in LINES if line[1] == name)
    payload = {'file_id': int(record['file_id']), 'voice_id': record['voice_id'],
               'text': text, 'model': MODEL, 'language_boost': 'Chinese',
               'need_noise_reduction': False, 'need_volume_normalization': True}
    record.update(status='cloning', clone_request=payload, updated_at=now())
    save(path, record)
    result = request('/v1/voice_clone', payload)
    record.update(status='cloned', response=result, updated_at=now())
    save(path, record)
    if result.get('demo_audio'):
        download(result['demo_audio'], ROOT / 'audio' / ('试听_' + name + '.mp3'))
    print(name + ': cloned, preview saved', flush=True)

def speech():
    for identifier, name, text, emotion in LINES:
        out = ROOT / 'audio/lines' / (identifier + '.wav')
        log = ROOT / 'tasks' / (identifier + '_tts.json')
        if out.exists() and log.exists() and json.loads(log.read_text()).get('status') == 'succeeded':
            continue
        if log.exists():
            raise RuntimeError('Existing speech request requires recovery: ' + str(log))
        voice = json.loads((ROOT / 'tasks' / ('voice_' + PEOPLE[name] + '.json')).read_text())
        if voice.get('status') != 'cloned':
            raise RuntimeError('Voice not ready: ' + name)
        payload = {'model': MODEL, 'text': text, 'stream': False,
                   'voice_setting': {'voice_id': voice['voice_id'], 'speed': 1, 'vol': 1, 'pitch': 0, 'emotion': emotion},
                   'audio_setting': {'sample_rate': 48000, 'format': 'wav', 'channel': 1},
                   'language_boost': 'Chinese', 'subtitle_enable': True}
        record = {'status': 'submitting', 'created_at': now(), 'request': payload}
        save(log, record)
        result = request('/v1/t2a_v2', payload)
        audio_hex = result.get('data', {}).get('audio')
        if not audio_hex:
            raise RuntimeError('No audio returned; inspect request ' + identifier)
        out.write_bytes(bytes.fromhex(audio_hex))
        # Keep usage/timing metadata without the large encoded waveform.
        result['data']['audio'] = '[saved to ' + str(out.relative_to(ROOT)) + ']'
        record.update(status='succeeded', response=result, duration=duration(out), output=str(out.relative_to(ROOT)))
        save(log, record)
        print(identifier + ': ' + str(record['duration']) + 's', flush=True)

def media_item(kind, source, role):
    path = ROOT / source
    size_limit = 30 if kind == 'image' else 15
    if path.stat().st_size > size_limit * 1024 * 1024:
        raise RuntimeError('Reference too large: ' + source)
    mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    field = kind + '_url'
    return {'type': field, field: {'url': 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()}, 'role': role}

def video(manifest_path):
    spec = json.loads(Path(manifest_path).read_text())
    assert spec['model'] == 'MiniMax-H3-Max' and spec['resolution'] == '480P'
    assert 5 <= spec['duration'] <= 15 and spec['ratio'] == '16:9'
    log = ROOT / 'tasks' / (spec['id'] + '.json')
    output = ROOT / 'output' / (spec['id'] + '.mp4')
    record = json.loads(log.read_text()) if log.exists() else None
    if record and record.get('status') == 'downloaded' and output.exists():
        print('Already downloaded: ' + str(output), flush=True)
        return
    if record and not record.get('task_id'):
        raise RuntimeError('Prior submit is uncertain or failed; do not resubmit automatically: ' + str(log))
    if not record:
        prompt = (ROOT / spec['prompt_file']).read_text()
        assert len(prompt) <= 7000
        images = spec.get('images', [])
        audios = spec.get('audios', [])
        assert len(images) <= 9 and len(audios) <= 3 and len(images) + len(audios) <= 12
        audio_duration = sum(duration(ROOT / path) for path in audios)
        assert audio_duration <= 15 and all(2 <= duration(ROOT / path) <= 15 for path in audios)
        content = [{'type': 'text', 'text': prompt}]
        content.extend(media_item('image', path, 'reference_image') for path in images)
        content.extend(media_item('audio', path, 'reference_audio') for path in audios)
        payload = {k: spec[k] for k in ('model', 'resolution', 'duration', 'ratio')}
        payload['content'] = content
        assert len(json.dumps(payload).encode()) <= 64 * 1024 * 1024
        record = {'status': 'submitting', 'created_at': now(), 'manifest': spec,
                  'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest()}
        save(log, record)
        try:
            result = request('/v2/video_generation', payload)
        except Exception as error:
            record.update(status='submission_error_or_uncertain', error=str(error), updated_at=now())
            save(log, record)
            raise
        record.update(task_id=result['task_id'], status='submitted', updated_at=now())
        save(log, record)
        print('Task created: ' + str(record['task_id']), flush=True)
    start = time.monotonic()
    while time.monotonic() - start < 2400:
        result = request('/v2/query/video_generation/' + str(record['task_id']))
        task = result['task']
        state = task['status']
        record.update(status=state, task=task, updated_at=now())
        save(log, record)
        print(str(record['task_id']) + ': ' + state, flush=True)
        if state == 'succeeded':
            download(task['content']['url'], output)
            record.update(status='downloaded', output=str(output.relative_to(ROOT)), actual_duration=duration(output))
            save(log, record)
            print('Saved: ' + str(output), flush=True)
            return
        if state in ('failed', 'cancelled', 'expired'):
            raise RuntimeError('Terminal task status: ' + json.dumps(task, ensure_ascii=False))
        time.sleep(15)
    raise RuntimeError('Timed out waiting; saved task ID must be resumed without resubmission')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['clone', 'speech', 'video'])
    parser.add_argument('argument', nargs='?')
    args = parser.parse_args()
    try:
        if args.action == 'clone':
            clone(args.argument)
        elif args.action == 'speech':
            speech()
        else:
            video(args.argument)
    except Exception as error:
        print(type(error).__name__ + ': ' + str(error), file=sys.stderr, flush=True)
        sys.exit(1)
