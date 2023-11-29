from openai import OpenAI

class ChatGPT():

    def __init__(self, valid_stream) -> None:
        self.client = OpenAI()
        self.dialogue_history = []
        self.valid_stream = valid_stream

    def get(self, user_utterance):
        self.dialogue_history.append({"role": "user", "content": user_utterance})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.dialogue_history,
            stream = self.valid_stream
        )
        return completion.choices[0].message.content

    def set_agent_utterance(self, agent_utterance):
        self.dialogue_history.append({"role": "assistant", "content": agent_utterance})