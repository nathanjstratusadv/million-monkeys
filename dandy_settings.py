import os

from pathlib import Path


ALLOW_DEBUG_RECORDING = True
BASE_PATH = Path(__file__).resolve().parent
DEFAULT_LLM_PROMPT_RETRY_COUNT: int = 2


LLM_CONFIGS = {
    'DEFAULT': {
        'TYPE': 'openai',
        'HOST': os.getenv('AI_API_HOST'),
        'PORT': 443,
        'API_KEY': os.getenv('AI_API_KEY'),
        'MODEL': os.getenv('AI_API_MODEL'),
        'TEMPERATURE': 0.1,
        'MAX_INPUT_TOKENS': 128000,
        'MAX_OUTPUT_TOKENS': 64000,
    },
}
