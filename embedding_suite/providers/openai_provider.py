import openai
from embedding_suite.provider import Provider
from embedding_suite.utils.config import get_api_key

# https://platform.openai.com/docs/guides/embeddings?lang=python


class OpenaiProvider(Provider):
    def __init__(self, **config):
        self.api_key = config.get("api_key") or get_api_key("openai")
        if not self.api_key:
            raise ValueError("OpenAI API key is missing.")

        openai.api_key = self.api_key

    def generate_embeddings(self, model, inputs, **kwargs):
        response = openai.embeddings.create(
            model=model, input=inputs, **kwargs)

        print("Response:", response.data[0].embedding)
        return [item.embedding for item in response.data]
