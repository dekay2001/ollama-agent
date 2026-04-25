# ollama-agent

A local AI agent with web search, powered by [Ollama](https://ollama.com/) and [pydantic-ai](https://ai.pydantic.dev/).

## Prerequisites

- [Ollama](https://ollama.com/) installed and running
- A model pulled: `ollama pull gpt-oss:20b` (or swap for any model you have)
- [uv](https://docs.astral.sh/uv/) installed

## Setup

```bash
uv sync
```

## Run

```bash
# Make sure Ollama is serving
ollama serve

# Run the agent
uv run main.py
```

## How It Works

`main.py` creates a pydantic-ai `Agent` backed by a local Ollama model. The agent has a `search_web` tool that queries DuckDuckGo. When you ask a question, the model decides whether to search the web and synthesizes an answer from the results.

## Change the Model

Edit the `model_name` in `main.py`:

```python
model = OllamaModel(model_name="llama3.1:latest", provider=provider)
```

See your available models with `ollama list`.
