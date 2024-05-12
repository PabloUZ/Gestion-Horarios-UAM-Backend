import requests, time, random

class Scrapping:
    def __init__(self):
        self.client = requests.Session()
        self.__username = 'martin.ostiosa'
        self.__password = 'Kiara.1005'
    
    def login(self):
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



