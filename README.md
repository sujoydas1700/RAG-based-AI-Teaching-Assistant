# RAG-Based AI Teaching Assistant

## Description

This project implements a Retrieval-Augmented Generation (RAG) pipeline that retrieves relevant information from existing courses and identifies which topics are taught in which videos, along with their corresponding timestamps, based on the user's questions.

## Technologies Used

- Python
- Pandas
- NumPy
- Joblib
- Scikit-learn
- FlagEmbedding
- LangChain Ollama
- [OpenAI Whisper](https://github.com/openai/whisper) (`git+https://github.com/openai/whisper.git`)

## Installation

### Clone the Repository

```bash
git clone https://github.com/sujoydas1700/RAG-based-AI-Teaching-Assistant.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Steps

### Step 1: Convert Video to Audio

Convert the video files into audio using `convert_video_to_audio.py`.

### Step 2: Transcribe Audio and Create Chunks

Use `audio_to_chunks_and_store_in_jsons.ipynb` to transcribe the audio and split the transcribed text into chunks, then store the chunks in JSON files.

I use OpenAI Whisper for transcription. Install it in the notebook using:

```python
!pip install git+https://github.com/openai/whisper.git
```

I use the `large-v2` model to transcribe Hindi audio into English text chunks.

```python
model = whisper.load_model("large-v2")
```

### Step 3: Generate Embeddings

Generate embeddings from the JSON files using `embedding_jsons.ipynb`.

Install FlagEmbedding in the notebook:

```python
!pip install -U FlagEmbedding
```

I use the `BAAI/bge-m3` model for embedding generation.

```python
model = BGEM3FlagModel("BAAI/bge-m3", use_fp32=True)
```

### Step 4: Store Embeddings Using Joblib

First, store the generated embeddings in a Pandas DataFrame. Then, use Joblib to serialize and save the DataFrame as `embedding_data.joblib`.

This process is performed in `creating_df_and_store_using_joblib.ipynb`.

### Step 5: Retrieve Relevant Chunks and Generate Answers

Load `embedding_data.joblib`, take a question from the user, and calculate cosine similarity to find the most relevant subtitle chunks.

Select the top four chunks based on cosine similarity and use them to construct a prompt. Pass this prompt to the LLM to generate an answer.

I use the `gemma3:4b` model through Ollama.

#### Install Dependencies

Install `zstd` and Ollama:

```bash
!apt-get update -qq
!apt-get install -y zstd
!curl -fsSL https://ollama.com/install.sh | sh
```

#### Download the LLM Model

```bash
!ollama pull gemma3:4b
```

---

## Improving Output Quality

For better output quality, you can use a more powerful LLM model with stronger reasoning capabilities.