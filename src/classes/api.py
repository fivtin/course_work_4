from abc import ABC, abstractmethod
from src.config.settings import HH_API_URL


class SiteAPI(ABC):
    """ """

    @abstractmethod
    def __init__(self, *args, **kwargs):
        ...

    @abstractmethod
    def get_vacancies(self):
        ...


class HeadHunterAPI(SiteAPI):
    """ """

    def __init__(self):
        self.base_url = HH_API_URL

    def get_vacancies(self):
        ...
