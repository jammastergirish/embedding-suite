# Embedding Suite

[![PyPI](https://img.shields.io/pypi/v/embedding-suite)](https://pypi.org/project/embedding-suite/)

[![GitHub last commit](https://img.shields.io/github/last-commit/jammastergirish/embedding-suite)](https://github.com/jammastergirish/embedding-suite)

A simple, unified interface for generating text embeddings from various providers. (This is heavily modeled on Andrew Ng's [AI Suite](https://github.com/andrewyng/aisuite), which does the same thing for Large Language Models.)

This is a work-in-progress, though is fully functional as described below. On the roadmap are new providers,  an easier way to optionally also install providers' packages, perhaps use of HTTP endpoints in lieu of providers' packages, perhaps multimodal embeddings...

## Installation

(You'll need to install the provider's SDK separately.)

### Pip

```bash
pip install embedding-suite
```

### Poetry

```bash
poetry add embedding-suite
```

### UV (recommended)

```bash
uv add embedding-suite
```

## Example Usage

```python
inputs = ["First sentence", "Second sentence"]
```

You can serve API keys from your `.env` or explicitly add them as in the below examples. 

### OpenAI

```python
from embedding_suite import EmbeddingSuiteClient

client = EmbeddingSuiteClient(provider_configs={"openai": {
    "api_key": "XXX"}})

embeddings = client.generate_embeddings(
    model="openai:text-embedding-3-large", inputs=inputs)
```

### Cohere

```python
from embedding_suite import EmbeddingSuiteClient

client = EmbeddingSuiteClient(provider_configs={"cohere": {
    "api_key": "XXX"}})

embeddings = client.generate_embeddings(
    model="cohere:embed-english-v3.0", inputs=inputs)
```

### VoyageAI

```python
from embedding_suite import EmbeddingSuiteClient

client = EmbeddingSuiteClient(provider_configs={"voyageai": {
    "api_key": "XXX"}})

embeddings = client.generate_embeddings(
    model="voyage:voyage-3", inputs=inputs)
```

### Sentence Transformers

```python
from embedding_suite import EmbeddingSuiteClient

client = EmbeddingSuiteClient(provider_configs={"sentencetransformers": {}})

embeddings = client.generate_embeddings(
    model="sentencetransformers:all-mpnet-base-v2", inputs=inputs)
```

### Huggingface

```python
from embedding_suite import EmbeddingSuiteClient

client = EmbeddingSuiteClient(provider_configs={"huggingface": {
    "api_key": "XXX"}})

embeddings = client.generate_embeddings(
    model="huggingface:sentence-transformers/sentence-t5-large", inputs=inputs)
```
