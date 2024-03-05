from abc import ABC, abstractmethod


class VacancyBase(ABC):
    """Description"""

    @abstractmethod
    def __init__(self, *args, **kwargs):
        ...


class Vacancy(VacancyBase):
    """Description"""

    def __init__(self):
        ...
