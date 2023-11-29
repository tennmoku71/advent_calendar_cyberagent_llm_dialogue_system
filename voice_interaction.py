from stt import google_stt
import threading

def callback_interim(user_utterance):
    print("interim", user_utterance)

def callback_final(user_utterance):
    print("final", user_utterance)

if __name__ == '__main__':

    stt_thread = threading.Thread(target=google_stt.main, args=(callback_interim, callback_final,))
    stt_thread.start()

    thread_list = threading.enumerate()
    thread_list.remove(threading.main_thread())
    for thread in thread_list:
        thread.join()

