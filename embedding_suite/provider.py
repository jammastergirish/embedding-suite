from abc import ABC, abstractmethod
from pathlib import Path
import importlib
import functools


class Provider(ABC):
    @abstractmethod
    def generate_embeddings(self, model, inputs, **kwargs):
        pass


class ProviderFactory:
    PROVIDERS_DIR = Path(__file__).parent / "providers"

    @classmethod
    def create_provider(cls, provider_key, config):
        provider_class_name = f"{provider_key.capitalize()}Provider"
        provider_module_name = f"{provider_key}_provider"
        module_path = f"embedding_suite.providers.{provider_module_name}"
        try:
            module = importlib.import_module(module_path)
        except ImportError:
            raise ImportError(
                f"Could not find provider module: {module_path}.")
        provider_class = getattr(module, provider_class_name)
        return provider_class(**config)

    @classmethod
    @functools.cache
    def get_supported_providers(cls):
        provider_files = Path(cls.PROVIDERS_DIR).glob("*_provider.py")
        return {file.stem.replace("_provider", "") for file in provider_files}
