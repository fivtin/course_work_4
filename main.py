from src.classes.api import HeadHunterAPI
from src.classes.vacancy import Vacancy
from src.utils.functions import filter_vacancies, append_and_save_json, get_top_vacancies, get_vacancies_by_salary, \
    sort_vacancies, print_vacancies, print_length


def user_interaction():
    print("Программа поиска вакансий на HH.ru\n\n")
    search_query = input("Введите ключевое слово для поиска (например, Python): ")

    hh_api = HeadHunterAPI()
    print("Выполняется запрос...")
    hh_vacancies = hh_api.get_vacancies(search_query)

    print(f"Найдено {len(hh_vacancies)} вакансий.\n")

    vacancies = Vacancy.cast_to_object_list(hh_vacancies)

    print("Уточним параметры вакансий:")
    print("(для отмены фильтра просто нажмите Enter)\n")

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().strip().split()
    filtered_vacancies = filter_vacancies(vacancies, filter_words)
    print_length(filtered_vacancies)

    salary_range = input("Введите диапазон зарплат (например, 90000-120000): ").strip()
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    print_length(ranged_vacancies)

    top_n = input("Введите количество вакансий для вывода в топ N (по умолчанию 20): ").strip()
    if top_n and top_n.isdigit():
        top_n = int(top_n)
    else:
        if top_n != '':
            print("Неверно указано число, будут выведен топ-20 вакансий.")
        top_n = 20

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)

    user_yn = input("Сохранить найденые вакансии в файл (да / нет)? : ").strip().lower()
    if user_yn in ('да', 'д', 'yes', 'y'):
        append_and_save_json(top_vacancies)


if __name__ == "__main__":
    user_interaction()
