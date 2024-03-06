from abc import ABC, abstractmethod


class VacancyBase(ABC):
    """Description"""

    @abstractmethod
    def __init__(self, *args, **kwargs):
        ...

    @abstractmethod
    def __gt__(self, other):
        ...

    # @abstractmethod
    # def __lt__(self, other):
    #     ...


class Vacancy(VacancyBase):
    """Description"""

    def __init__(self):
        ...

    def __gt__(self, other):
        ...
