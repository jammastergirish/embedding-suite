# embedding_suite/client.py
from .provider import ProviderFactory


class EmbeddingSuiteClient:
    def __init__(self, provider_configs: dict = {}):
        """
        Initialize the client with provider configurations.

        Args:
            provider_configs (dict): A dictionary containing provider configurations.
                Example:
                {
                    "openai": {"api_key": "your-openai-api-key"},
                    "huggingface": {"api_key": "your-huggingface-api-key"}
                }
        """
        self.providers = {}
        self.provider_configs = provider_configs
        self._initialize_providers()  # Initialize providers

    def _initialize_providers(self):
        """
        Helper method to initialize providers based on the configuration.
        """
        for provider_key, config in self.provider_configs.items():
            self.providers[provider_key] = ProviderFactory.create_provider(
                provider_key, config
            )

    def generate_embeddings(self, model: str, inputs: list, **kwargs):
        """
        Generate embeddings using the specified provider and model.

        Args:
            model (str): The provider and model in format `provider:model`.
            inputs (list): List of text inputs to embed.

        Returns:
            list: A list of embeddings.
        """
        # Extract provider key from the model
        if ":" not in model:
            raise ValueError(
                f"Invalid model format. Expected 'provider:model', got '{model}'")

        provider_key, model_name = model.split(":", 1)
        if provider_key not in self.providers:
            raise ValueError(f"Provider '{provider_key}' is not configured.")

        provider = self.providers[provider_key]

        return provider.generate_embeddings(model_name, inputs, **kwargs)
