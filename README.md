# Embedding Suite

[![PyPI](https://img.shields.io/pypi/v/embedding-suite)](https://pypi.org/project/embedding-suite/)

A simple, unified interface for generating embeddings from various providers. (This is heavily modeled on Andrew Ng's [AI Suite](https://github.com/andrewyng/aisuite), which does the same thing for Large Language Models.)

## Installation

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

## Usage

```python
from embedding_suite import EmbeddingSuiteClient

client = EmbeddingSuiteClient(provider_configs={"openai": {
    "api_key": "XXX"}})

embeddings = client.generate_embeddings(
    model="openai:text-embedding-3-large", inputs=["Hi", "Hello"])
```
