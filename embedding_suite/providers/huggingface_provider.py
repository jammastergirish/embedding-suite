import requests
from embedding_suite.provider import Provider
from embedding_suite.utils.config import get_api_key

# https://huggingface.co/blog/getting-started-with-embeddings


class HuggingfaceProvider(Provider):
    def __init__(self, **config):
        self.api_key = config.get("api_key") or get_api_key("huggingface")
        if not self.api_key:
            raise ValueError("Huggingface API key is missing.")

    def generate_embeddings(self, model, inputs, **kwargs):

        api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model}"

        headers = {"Authorization": f"Bearer {self.api_key}"}

        response = requests.post(api_url, headers=headers, json={
                                 "inputs": inputs, "options": {"wait_for_model": True}})

        return response.json()
