from stt import google_stt
from vad import google_vad
import threading

def callback_interim(user_utterance):
    print("interim", user_utterance)

def callback_final(user_utterance):
    print("final", user_utterance)

def callback_vad(flag):
    print("vad", flag)

if __name__ == '__main__':

    vad = google_vad.GOOGLE_WEBRTC()
    vad_thread = threading.Thread(target=vad.vad_loop, args=(callback_vad, ))
    vad_thread.start()

    stt_thread = threading.Thread(target=google_stt.main, args=(callback_interim, callback_final,))
    stt_thread.start()

    thread_list = threading.enumerate()
    thread_list.remove(threading.main_thread())
    for thread in thread_list:
        thread.join()

