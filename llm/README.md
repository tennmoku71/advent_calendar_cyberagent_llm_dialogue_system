```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build

make  -j 8 LLAMA_CUBLAS=1

mkdir -p gguf_models
python3 convert.py original_models/models--cyberagent--open-calm-7b/snapshots/276a5fb67510554e11ef191a2da44c919acccdf5/ \
 --vocabtype spm \
 --outtype f16 \
 --outfile gguf_models/open-calm-7b-f16.gguf

./quantize \
    gguf-models/cyberagent/llama2-7b-chat-japanese/ggml-model-f16.gguf \
    gguf-models/cyberagent/llama2-7b-chat-japanese/ggml-model-q8_0.gguf q8_0


./main -m gguf-models/cyberagent/llama2-7b-chat-japanese/ggml-model-q8_0.gguf \
    -n 512 -c 0 \
    --repeat_penalty 1.0 \
    --color -i -r "User:" \
    -f prompts/chat-with-sota-kun.txt
```
test
```
./main -m gguf-models/cyberagent/llama2-7b-chat-japanese/ggml-model-q8_0.gguf --temp 0.1 -p "[INST]こんにちは。[/INST]" -ngl 32 -b 512
```
