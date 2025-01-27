from sentence_transformers import SentenceTransformer
from embedding_suite.provider import Provider
from embedding_suite.utils.config import get_api_key

# https://sbert.net/


class SentencetransformersProvider(Provider):
    def __init__(self, **config):
        pass

    def generate_embeddings(self, model, inputs, **kwargs):

        model = SentenceTransformer(model)

        embeddings = model.encode(inputs)

        return embeddings
