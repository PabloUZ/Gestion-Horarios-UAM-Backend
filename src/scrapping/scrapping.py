import requests, time, random
from os import getenv

class Scrapping:
    def __init__(self):
        self.client = requests.Session()
        self.__username = getenv('UAM_USER')
        self.__password = getenv('UAM_PASSWORD')
    
    def login(self):
        print(self.__username)
        print(self.__password)
        login_data = {
            'LoginForm[username]': self.__username,
            'LoginForm[password]': self.__password
        }
        self.client.post('https://intrauam.autonoma.edu.co/intrauam2/site/login/', login_data, verify=False)
        print('Se inició sesión')
    
    def sleep(self):
        tiempo = random.random() * 10
        time.sleep(tiempo)
        print(f'Tiempo de detención: {tiempo}')



