import json

from abc import ABC, abstractmethod
from pathlib import Path

from src.config.settings import JSON_DATA_DIR, JSON_DATA_FILE


class DataSaver(ABC):
    """ """

    @abstractmethod
    def add_vacancy(self, vacancy):
        ...

    @abstractmethod
    def delete_vacancy(self, vacancy):
        ...


class JsonSaver(DataSaver):
    """ """

    def __init__(self):
        current_dir = Path(__file__).parent.parent.parent
        self.filename = Path(current_dir, JSON_DATA_DIR, JSON_DATA_FILE)

    def add_vacancy(self, vacancy):
        ...

    def delete_vacancy(self, vacancy):
        ...
