import requests
import string
from bs4 import BeautifulSoup
import json

client = requests.Session()

login_data = {
    'LoginForm[username]': 'martin.ostiosa',
    'LoginForm[password]': 'secret'
}

client.post('https://intrauam.autonoma.edu.co/intrauam2/site/login/', login_data, verify=False)
data_set = []
print(string.ascii_lowercase)
for letter in string.ascii_uppercase:
    query = f'https://intrauam.autonoma.edu.co/intrauam2/l/url/docente/horarioAsignatura/editar_sel.php?letra={letter}&periodo=1&ano=2024'
    print(query)
    html = client.get(query).content
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(class_='datos')
    print('------------------')
    print(table)
    rows = table.find_all('tr')[1:]
    for row in rows:
        row_data = row.find_all('td')
        print(row_data)
        
        subject = {
            'codigo': row_data[1].text.split(' - ')[0],
            'nombre': row_data[1].text.split(' - ')[1],
            'nro grupo': row_data[2].text.split(' - ')[0],
            'grupo': row_data[2].text.split(' - ')[1],
            'profesor': row_data[3].text,
            'horario': row_data[4].text,
            'salon': row_data[5].text 
        }
        data_set.append(subject)
    

with open('data2.json', 'w') as file:
    data = json.dump(data_set, file)

