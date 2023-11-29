import requests
import json
import time

def get_audio_query(text, speaker = 1):
    query_payload = {"text": text, "speaker": speaker}
    while True:
        try:
            url = "http://localhost:50021/audio_query"
            r = requests.post(url, params=query_payload, timeout=(10.0, 300.0))
            if r.status_code == 200:
                return r.json()
                
        except requests.exceptions.ConnectionError:
            print('fail connect...', url)
            time.sleep(0.1)


def run_synthesis(query_data, speaker = 1):
    synth_payload = {"speaker": speaker}    
    while True:
        try:
            url = "http://localhost:50021/synthesis"
            r = requests.post(url, params=synth_payload, data=json.dumps(query_data), timeout=(10.0, 300.0))
            if r.status_code == 200:
                return r.content
        except requests.exceptions.ConnectionError:
            print('fail connect...', url)
            time.sleep(0.1)

def extract_wav_length(query_data):
    length = 0
    for accent_phrase in query_data["accent_phrases"]:
        for mora in accent_phrase["moras"]:
            if mora["consonant_length"] != None:
                length += mora["consonant_length"]
            if mora["vowel_length"] != None:
                length += mora["vowel_length"]
    return length

def get_audio_file_from_text(text):
    query_data = get_audio_query(text)
    return run_synthesis(query_data), extract_wav_length(query_data)