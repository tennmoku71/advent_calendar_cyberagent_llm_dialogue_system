from llama_cpp import Llama

class Llama2():

    def __init__(self, valid_stream=True) -> None:
        self.llama = Llama(model_path="llm/models/elyza-q8.gguf", n_gpu_layers=50)
        self.valid_stream = valid_stream

    def get(self, user_utterance):
        streamer = self.llama.create_chat_completion(
            [{"role":"user", "content": f"""[INST] <<SYS>>\nあなたはアシスタントです。\n<</SYS>>\n\n{user_utterance}[/INST]"""}], 
            stream=self.valid_stream
        )
        return streamer

    def set_agent_utterance(self, agent_utterance):
        pass