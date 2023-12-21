# 概要

LLMを用いたシンプルな音声対話システムです。

# 環境設定

googleとopenaiのキーをそれぞれ環境変数に登録してください。

```
export GOOGLE_APPLICATION_CREDENTIALS=...
```
```
export OPENAI_API_KEY=...
```

pipモジュールをインストールします。
```
pip install -r requirements.txt
```

その後、voicevoxをインストールしてください。具体的なインストール方法は公式ページを参照してください。

https://voicevox.hiroshiba.jp/


# voice_interaction_base

一番遅いモデルです。Google STTのfinalの終わりまで待ち、ChatGPTにリクエストを投げます。ただし応答内容の精度は良いです。

```
python voice_interaction_base.py
```

# voice_interaction

Google STTのfinalが出力されるまでの時間が短縮されています。

```
python voice_interaction.py
```

# voice_interaction_stream

リアルタイムもどきの方法で音声合成が行われます。

```
python voice_interaction_stream.py
```

# voice_interaction_llama2

ChatGPTではなくllama2を用います。事前にモデルデータを準備しておく必要があります。

```
# bash
> git clone https://github.com/ggerganov/llama.cpp
> cd llama.cpp
> make -j 8 LLAMA_CUBLAS=1
> python
    import huggingface_hub
    huggingface_hub.snapshot_download(repo_id='elyza/ELYZA-japanese-Llama-2-7b-instruct', cache_dir="original_models")
    exit()
> python3 convert.py original_models/models--elyza--ELYZA-japanese-Llama-2-7b-instruct/snapshots/48fa08b3098a23d3671e09565499a4cfbaff1923 --outfile gguf-models/elyza.gguf
> ./quantize gguf-models/elyza.gguf gguf-models/elyza-q8.gguf q8_0
```

生成された`gguf-models/elyza-q8.gguf`を`llm/models`に配置してください。
次に、llama-cpp-pythonをインストールします。

```
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir -vv
```

以上で準備は完了です。実行してください。

```
python voice_interaction_llama2.py
```
