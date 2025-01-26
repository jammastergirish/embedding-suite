import voyageai
from embedding_suite.provider import Provider
from embedding_suite.utils.config import get_api_key

# https://docs.cohere.com/v2/docs/embeddings


class VoyageaiProvider(Provider):
    def __init__(self, **config):
        self.api_key = config.get("api_key") or get_api_key("voyageai")
        if not self.api_key:
            raise ValueError("VoyageAI API key is missing.")

    def generate_embeddings(self, model, inputs, **kwargs):

        vo = voyageai.Client(api_key=self.api_key)

        result = vo.embed(inputs, model=model, input_type="document")

        return result.embeddings
