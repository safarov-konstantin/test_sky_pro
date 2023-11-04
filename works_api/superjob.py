import requests, json
from works_api.client_api import ApiClient

class SuperJobAPI(ApiClient):
    """
    Класс для работы с API HeadHunter
    """
    url_vacancies = 'https://api.superjob.ru/2.0/vacancies/'
    url_dictionaries = 'https://api.superjob.ru/2.0/references/'
    header = None

    def __init__(self):
        api_key = 'v3.r.137933430.81d31de66228c61b26d2f313373ac28fbb459d09.1d358a864423ec03c9b23429ee2671a5ce50ac65'
        self.header = {'X-Api-App-Id': api_key} 

    def get_vacancies(self, params):
        
        req = requests.get(SuperJobAPI.url_vacancies, headers=self.header, params=params) 
        data = req.content.decode()  
        req.close()
        data = json.loads(data)

        return data['objects']
    
    @staticmethod
    def get_solary_representation(payment_from, payment_to, currency): 

        if currency == 'rub':
            salary_currency = 'руб.'

        if payment_from is None and payment_to is None:
            return 'Не указана'
        elif (payment_from is not None) and (payment_to is not None):
            return f"{payment_from} - {payment_to} {salary_currency}"
        elif (payment_from is not None) and (payment_to is None):
            return f"{payment_from} {salary_currency}"
        elif (payment_from is None) and (payment_to is not None):
            return f"до {payment_to} {salary_currency}"

    @staticmethod
    def get_dictionaries():
        req = requests.get(SuperJobAPI.url_dictionaries, headers=SuperJobAPI.header)  
        data = req.content.decode()  
        req.close()
        return json.loads(data) 