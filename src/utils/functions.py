from typing import List

from src.classes.saver import JsonSaver
from src.classes.vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], filter_words) -> List[Vacancy]:
    """ Filtering vacancies by keywords. """

    if not filter_words:
        return vacancies
    result = list()
    for vacancy in vacancies:
        for word in filter_words:
            if word in vacancy.name.lower():
                result.append(vacancy)
                continue
    return result


def get_vacancies_by_salary(vacancies: List[Vacancy], salary_range: str) -> List[Vacancy]:
    """ Filtering vacancies by salary. """

    if not salary_range:
        return vacancies
    result = list()
    salary_range = salary_range.replace(' ', '').split('-')
    for vacancy in vacancies:
        if int(salary_range[0]) <= max(vacancy.salary_from or 0, vacancy.salary_to or 0) < int(salary_range[1]):
            result.append(vacancy)
    return result


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """ Sort vacancies by increasing salary. """

    return sorted(vacancies)


def get_top_vacancies(vacancies: List[Vacancy], top_number: int) -> List[Vacancy]:
    """ Return top N vacancies from the list. """

    return vacancies[0:top_number]


def append_and_save_json(vacancies: List[Vacancy]):
    """ Add vacancies to existing ones and save them in a file. """

    json_saver = JsonSaver()
    for vacancy in vacancies:
        json_saver.add_vacancy(vacancy)
    json_saver.save()
    print("Вакансии сохранены.")


def print_vacancies(vacancies: List[Vacancy]):
    """ Print a list of vacancies. """

    print('\n', '-' * 72)
    print(*vacancies, sep='\n')
    print('-' * 72)
    print(f"Вакансий: {len(vacancies)}")
    print("")


def print_length(items_list: list):
    """ Print the number of elements in a list. """

    print(f'Вакансий в списке: {len(items_list)}')
