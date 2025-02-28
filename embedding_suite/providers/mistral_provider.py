from mistralai import Mistral
from embedding_suite.provider import Provider
from embedding_suite.utils.config import get_api_key

# https://docs.mistral.ai/capabilities/embeddings/


class MistralProvider(Provider):
    def __init__(self, **config):
        self.api_key = config.get("api_key") or get_api_key("mistral")
        if not self.api_key:
            raise ValueError("Mistral API key is missing.")

    def generate_embeddings(self, model, inputs, **kwargs):
        client = Mistral(api_key=self.api_key)

        response = client.embeddings.create(
            model=model,
            inputs=inputs,
            **kwargs
        )

        return response
