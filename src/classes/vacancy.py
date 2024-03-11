from abc import ABC, abstractmethod


class VacancyBase(ABC):
    """ Abstract class for working with vacancies. """

    @abstractmethod
    def __init__(self, *args, **kwargs):
        """ In this method it is necessary to implement the initialization of a class instance. """
        ...

    @abstractmethod
    def __lt__(self, other):
        """ In this method it is necessary to implement a comparison of two instances for salary size. """
        ...

    @classmethod
    @abstractmethod
    def cast_to_object_list(cls, items):
        """
        In this method it is necessary to implement the creation of a list of vacancies from list of api_json items.
        """
        ...


class Vacancy(VacancyBase):
    """ Implementation of a Vacancy class. """

    def __init__(self, id: str, name: str, schedule: str, salary_from, salary_to, city: str):
        """ Set attributes of the class  instance. """

        self.id = id
        self.name = name
        self.schedule = schedule
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city

    def __lt__(self, other):
        """ Checking that the salary of an instance is less than the salary of another. """

        self_salary = max(self.salary_from or 0, self.salary_to or 0)
        other_salary = max(other.salary_from or 0, other.salary_to or 0)

        return self_salary < other_salary

    def __repr__(self):
        """ Returns a string representation of the instance for the developer. """

        return f"Vacancy({', '.join([attr + '=' + str(self.__dict__[attr]) for attr in self.__dict__])})"

    @property
    def salary(self):
        """ Returns a string representation of the salary size. """

        salary_from = f"от {self.salary_from}" if self.salary_from else ''
        salary_to = f"до {self.salary_to}" if self.salary_to else ''
        return f"{salary_from}{' ' + salary_to if salary_from and salary_to else salary_to}"

    def __str__(self):
        """ Returns a string representation of the instance for the user. """

        return f"Вакансия: {self.name}, зарплата: {self.salary if self.salary else 'не указана'}, город: {self.city}, график: {self.schedule}"

    @classmethod
    def cast_to_object_list(cls, items):
        """ Implementation of creating a list of vacancies from a list of api_json items. """

        return [
            cls(item['id'],
                item['name'],
                item['schedule']['name'],
                item['salary']['from'] if item['salary'] else 0,
                item['salary']['to'] if item['salary'] else 0,
                item['area']['name'])
            for item in items
        ]
