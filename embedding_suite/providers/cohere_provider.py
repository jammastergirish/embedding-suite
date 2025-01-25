import cohere
from embedding_suite.provider import Provider
from embedding_suite.utils.config import get_api_key

# https://docs.cohere.com/v2/docs/embeddings


class CohereProvider(Provider):
    def __init__(self, **config):
        self.api_key = config.get("api_key") or get_api_key("cohere")
        if not self.api_key:
            raise ValueError("Cohere API key is missing.")

    def generate_embeddings(self, model, inputs, **kwargs):

        co = cohere.Client(api_key=self.api_key)

        input_type = "search_document"
        response = co.embed(
            texts=inputs,
            model=model,
            input_type=input_type,
            embedding_types=["float"], **kwargs
        )

        return response.embeddings.float
