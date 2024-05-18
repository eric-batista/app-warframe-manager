from pathlib import Path

from devtools.database import AbstractEntity
from devtools.utils import FinderBuilder


def get_metadata():
    ROOT_DIR = Path(__file__).parent
    print(ROOT_DIR)
    finder = FinderBuilder().child_of(AbstractEntity).from_path(ROOT_DIR).build()
    instance = finder.find().get("Zaw")
    return instance.metadata
