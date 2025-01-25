import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


def get_api_key(provider_name):
    """
    Get the API key for a specific provider.

    Args:
        provider_name (str): The name of the provider (e.g., 'openai').

    Returns:
        str: The API key or None if not found.
    """
    env_var_name = f"{provider_name.upper()}_API_KEY"
    return os.getenv(env_var_name)
