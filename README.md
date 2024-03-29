## Поиск вакансий на HH.RU

Для запуска программы используйте команду __python3 main.py__

Перед этим __необходимо переименовать__ файл ___config/.env-demo___ в ___config/.env___, или же создать новый по этому образцу.

1. На первом этапе программа запросит ключевое слово для поиска вакансий на сайте hh.ru
2. После выполнения запроса будет показано количество найденных вакансий.
3. Далее пользователь работает уже со списком полученных вакансий
    - фильтрация по указанным словам (совпадение любого слова)
    - фильтрация по заработной плате (формат ввода: 10000-100000)
    - указывает количество вакансий для вывода
4. После вывода вакансий на экран, пользователь может сохранить эти вакансии в файл (либо они добавятся к существующим).

-------------------
Основные настройки в файле config/.env :

__HH_API_URL=https://api.hh.ru/vacancies__ - базовый URL-запрос

__HH_MAX_LOAD_PAGES=10__ - максимальное количество запросов страниц

__HH_MAX_PER_PAGE=100__ - количество вакансий в одном запросе (макс. 100)

__JSON_DATA_DIR=data__ - каталог для хранения файлов с вакансиями (относительно текущего)

__JSON_DATA_FILE=data.json__ - имя json-файла для хранения вакансий.
