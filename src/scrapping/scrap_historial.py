import requests
from bs4 import BeautifulSoup
import json

client = requests.Session()

login_data = {
    'LoginForm[username]': 'martin.ostiosa',
    'LoginForm[password]': 'secret'
}

historial_data = {
    'usuario': '1055751017',
    'codigo': '10202200132'
}

client.post('https://intrauam.autonoma.edu.co/intrauam2/site/login/', login_data, verify=False)
query = f'https://intrauam.autonoma.edu.co/intrauam2/l/url/estudiantes/histacad/consultaHistorialAcademico.php'
html = client.post(query, historial_data, verify=False).content
soup = BeautifulSoup(html, 'html.parser')

encabezado = soup.find(class_='encabezado')
rows = encabezado.find_all('td')
user = {
    'nombre': rows[5].get_text(strip=True).replace("\t",""),
    'codigo': rows[7].get_text(strip=True).replace("\t",""),
    'programa': rows[1].get_text(strip=True).replace("\t","")
}

tablas = soup.find_all(class_='table')
lista_asignaturas = []
for tabla in tablas:
    materias = tabla.find_all('tr')[1:-2]
    for materia in materias:
        asignatura = materia.find_all('td')
        asig = {
            'periodo': asignatura[0].get_text(strip=True).replace("\t","") + "-" + asignatura[1].get_text(strip=True).replace("\t",""),
            'codigo': asignatura[2].get_text(strip=True).replace("\t",""),
            'nombre': asignatura[3].get_text(strip=True).replace("\t",""),
            'creditos': int(asignatura[5].get_text(strip=True).replace("\t","")),
            'nota': float(asignatura[6].get_text(strip=True).replace("\t","")) if asignatura[6].get_text(strip=True).replace("\t","") != '' else 0
        }
        lista_asignaturas.append(asig)


historial = {
    "usuario": "¿?",
    "nombre": user['nombre'],
    "codigo": user['codigo'],
    "plan": user['codigo'][:4],
    "historial": lista_asignaturas
}

with open('historial.json', 'w', encoding='utf8') as file:
    data = json.dump(historial, file, ensure_ascii= False, indent= 4)
