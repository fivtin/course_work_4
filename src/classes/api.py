from abc import ABC, abstractmethod
import requests

from src.config.settings import HH_API_URL, HH_MAX_LOAD_PAGES, HH_MAX_PER_PAGE


class SiteAPI(ABC):
    """ The abstract class implements loading vacancies from an external resource. """

    @abstractmethod
    def __init__(self, *args, **kwargs):
        """ In this method it is necessary to implement the initialization of a class instance. """
        ...

    @abstractmethod
    def get_vacancies(self, search_text):
        """ The abstract method loads vacancies with the search query as an argument. """
        ...


class HeadHunterAPI(SiteAPI):
    """ Implementation of a class for loading vacancies from an external resource - HH.ru """

    def __init__(self):
        """ Set basic settings and variables of the class  instance. """
        self.base_url = HH_API_URL
        self.per_page = HH_MAX_PER_PAGE
        self.max_pages = HH_MAX_LOAD_PAGES

    def get_vacancies(self, search_text):
        """ Implementation of a method for loading vacancies using a search query. """

        params = {
            'per_page': self.per_page,
            'page': 0,
            'pages': 10000,
            'text': search_text,
            'search_field': ('name', 'description'),
        }

        result = list()

        while params['page'] < params['pages'] and params['page'] < self.max_pages:
            response = requests.get(self.base_url, params)
            if response.status_code == 200:
                response_json = response.json()
                params['page'] = int(response_json['page']) + 1
                params['pages'] = int(response_json['pages'])
                result.extend(response_json['items'])
            else:
                break

        return result
