# Chatbot-Langchain

Learning project with three small LangChain experiments against local Ollama models: a Streamlit
chatbot, a LangServe/FastAPI server with a Streamlit client, and a simple RAG ingestion notebook.

## Components

| Path | What it does |
|------|--------------|
| `chatbot/app.py` | Streamlit chatbot: `ChatPromptTemplate -> Ollama(llama2) -> StrOutputParser`, with LangSmith tracing enabled. |
| `api/app.py` | FastAPI + LangServe server on `localhost:8000` exposing `/chatbot` (raw llama2), `/chat` (100-word essay on a topic, llama2) and `/code` (code on a topic, codellama). |
| `api/client.py` | Streamlit client that calls `/chat/invoke` and `/code/invoke` on the server. |
| `rag/simplerag.ipynb` | Loads documents (`speech.txt`, a web page, `transformer.pdf`), splits them into 1000-char chunks, embeds with `OllamaEmbeddings` and runs similarity search in Chroma and FAISS. No generation step. |

`rag/transformer.pdf` is the "Attention Is All You Need" paper, used as sample input.

## Getting started

Prerequisites: Python 3.9+, [Ollama](https://ollama.com) running locally, and a
[LangSmith](https://smith.langchain.com) API key (the code reads it unconditionally).

```bash
ollama pull llama2
ollama pull codellama          # only needed for the /code route

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env           # then fill in LANGCHAIN_API_KEY / LANGCHAIN_PROJECT
```

Chatbot:

```bash
streamlit run chatbot/app.py
```

API server and client (two terminals):

```bash
python api/app.py              # serves http://localhost:8000 (LangServe playground at /chat/playground)
streamlit run api/client.py
```

Direct call to the server:

```bash
curl -X POST http://localhost:8000/chat/invoke \
  -H 'Content-Type: application/json' \
  -d '{"input": {"topic": "distributed systems"}}'
```

RAG notebook: run it from inside `rag/` so the relative paths to `speech.txt` and
`transformer.pdf` resolve.

## Notes

- Uses pre-1.0 LangChain import paths (`langchain.prompts`, `langchain.text_splitter`), so
  `requirements.txt` pins `langchain<1.0`.
- Environment variables: `LANGCHAIN_API_KEY`, `LANGCHAIN_PROJECT` (see `.env.example`).
