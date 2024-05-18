from pathlib import Path

from devtools.config import Config

config = Config()

ROOT = Path(__file__).parent.parent
BASE_PATH = config("BASE_PATH_ZAWS", str, "/app/zaws")
