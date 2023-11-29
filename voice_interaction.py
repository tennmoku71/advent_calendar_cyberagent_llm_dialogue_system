from stt import google_stt
from vad import google_vad
from llm import chatgpt
from tts import voicevox
import threading
from playsound import playsound

class Main():

    def __init__(self) -> None:
        vad = google_vad.GOOGLE_WEBRTC()
        vad_thread = threading.Thread(target=vad.vad_loop, args=(self.callback_vad, ))
        stt_thread = threading.Thread(target=google_stt.main, args=(self.callback_interim, self.callback_final,))
        self.llm = chatgpt.ChatGPT(valid_stream=False)

        self.latest_user_utterance = None
        self.finished_user_speeching = False

        stt_thread.start()
        vad_thread.start()

    def wait(self):
        thread_list = threading.enumerate()
        thread_list.remove(threading.main_thread())
        for thread in thread_list:
            thread.join()

    def callback_interim(self, user_utterance):
        print("interim", user_utterance)
        self.latest_user_utterance = user_utterance

    def callback_final(self, user_utterance):
        print("final", user_utterance)
        self.latest_user_utterance = user_utterance

    def callback_vad(self, flag):
        print("vad", flag)
        if flag == True:
            self.latest_user_utterance = None
        elif self.latest_user_utterance != None:
            threading.Thread(target=self.main_process, args=(self.latest_user_utterance,)).start()

    def main_process(self, user_utterance):
        llm_result = self.llm.get(user_utterance)
        print("llm end", llm_result)
        if type(llm_result) == str:
            print(llm_result)
            wav_data = voicevox.get_audio_file_from_text(llm_result)
            self.audio_play(wav_data)
        else:
            print(llm_result)

    def audio_play(self, wav_data):
        with open("tmp.wav", mode='bx') as f:
            f.write(wav_data)
        playsound("tmp.wav")

if __name__ == '__main__':
    ins = Main()
    ins.wait()



