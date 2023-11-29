# stt
```
wget https://github.com/GoogleCloudPlatform/python-docs-samples/raw/main/speech/microphone/transcribe_streaming_infinite.py -O stt/google_stt.py
```
modified listen_print_loop

before
```
def listen_print_loop(responses: object, stream: object) -> object:

[中略]

        if result.is_final:
            sys.stdout.write(GREEN)
            sys.stdout.write("\033[K")
            sys.stdout.write(str(corrected_time) + ": " + transcript + "\n")

            stream.is_final_end_time = stream.result_end_time
            stream.last_transcript_was_final = True

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                sys.stdout.write(YELLOW)
                sys.stdout.write("Exiting...\n")
                stream.closed = True
                break
        else:
            sys.stdout.write(RED)
            sys.stdout.write("\033[K")
            sys.stdout.write(str(corrected_time) + ": " + transcript + "\r")

            stream.last_transcript_was_final = False

        return transcript
```
after
```
def listen_print_loop(responses: object, stream: object, callback_interim: object, callback_final: object) -> object:

[中略]

        if result.is_final:
            sys.stdout.write(GREEN)
            sys.stdout.write("\033[K")
            sys.stdout.write(str(corrected_time) + ": " + transcript + "\n")

            if callback_final != None:
                callback_final(transcript)

            stream.is_final_end_time = stream.result_end_time
            stream.last_transcript_was_final = True

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                sys.stdout.write(YELLOW)
                sys.stdout.write("Exiting...\n")
                stream.closed = True
                break
        else:
            sys.stdout.write(RED)
            sys.stdout.write("\033[K")
            sys.stdout.write(str(corrected_time) + ": " + transcript + "\r")

            if callback_interim != None:
                callback_interim(transcript)

            stream.last_transcript_was_final = False

    return transcript
```

modified main
```
def main() -> None:

[中略]

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=SAMPLE_RATE,
        language_code="en-US",
        max_alternatives=1,
    )

[中略]
            listen_print_loop(responses, stream)
```
```
def main(callback_interim, callback_final) -> None:

[中略]

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=SAMPLE_RATE,
        language_code="ja-JP",
        max_alternatives=1,
    )

[中略]

            listen_print_loop(responses, stream, callback_interim, callback_final)
```



```
export GOOGLE_APPLICATION_CREDENTIALS=...
```

