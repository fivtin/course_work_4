import requests

response = requests.get('https://api.hh.ru/vacancies?per_page=100&page=1')

print(*[f"{k}:{v}" for k,v in response.json()['items'][0].items()], sep='\n')
