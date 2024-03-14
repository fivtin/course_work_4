import json
import os

from abc import ABC, abstractmethod
from pathlib import Path

from src.classes.vacancy import Vacancy
from src.config.settings import JSON_DATA_DIR, JSON_DATA_FILE


class DataSaver(ABC):
    """ Abstract class for load/save vacancies. """

    @abstractmethod
    def add_vacancy(self, vacancy):
        """ In this method it is necessary to implement addition of a vacancy. """
        ...

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """ In this method it is necessary to implement removal of the vacancy. """
        ...


class JsonSaver(DataSaver):
    """ Implementation of a class for working with a json file. """

    def __init__(self):
        """  Set basic settings and variables of the class  instance. """

        self.root_dir = Path(__file__).parent.parent.parent
        self.data_dir = Path(self.root_dir, JSON_DATA_DIR)
        self.data_file = Path(self.data_dir, JSON_DATA_FILE)
        self.vacancies = list()
        if not Path.exists(self.data_dir):
            os.mkdir(self.data_dir)
        if not Path.exists(self.data_file):
            with open(self.data_file, 'x') as f:
                f.write('[]')
        with open(self.data_file) as f:
            json_vacancies = json.load(f)
        for j in json_vacancies:
            self.vacancies.append(Vacancy(j['id'], j['name'], j['schedule'], j['salary_from'], j['salary_to'], j['city']))

    def add_vacancy(self, vacancy: Vacancy):
        """ Implementation of adding a vacancy to the list of vacancies. """

        index = self.find_vacancy_by_id(vacancy.id)
        if index is None:
            self.vacancies.append(vacancy)
        else:
            self.vacancies[index] = vacancy

    def delete_vacancy(self, vacancy):
        """ Implementation of removing a vacancy from the vacancy list. """

        index = self.find_vacancy_by_id(vacancy.id)
        if index is not None:
            del self.vacancies[index]

    def find_vacancy_by_id(self, vacancy_id):
        """ Find a vacancy in the list of vacancies by id. None, if not found. """

        for index, value in enumerate(self.vacancies):
            if self.vacancies[index].id == vacancy_id:
                return index

    @staticmethod
    def vacancy_to_dict(vacancy: Vacancy):
        """ Convert Vacancy-object to dictionary. """

        data = {
            'id': vacancy.id,
            'name': vacancy.name,
            'schedule': vacancy.schedule,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to,
            'city': vacancy.city,
        }
        return data

    def save(self):
        """ Saving a list of vacancies to a json file. """

        data_list = list()
        for vacancy in self.vacancies:
            data_list.append(self.vacancy_to_dict(vacancy))

        with open(self.data_file, 'w') as f:
            f.write(json.dumps(data_list))
