from ..scrapping import Scrapping
from .course import Course
import string
from bs4 import BeautifulSoup
import random

class CourseScrapping(Scrapping, Course):
    def __init__(self):
        Scrapping.__init__(self)
        self.courses = []
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.YEAR = 2024
        self.PERIOD = 1

    def get_courses(self) -> list:
        self.login()
        self.sleep()
        self.client.get('https://intrauam.autonoma.edu.co/intrauam2/l/url/docente/horarioAsignatura/editar_sel.php')
        print('Entré a la sección de materias')
        for _ in range(len(self.letters)):
            self.sleep()
            selected_letter = random.choices(self.letters, k=1)[0]
            self.letters.remove(selected_letter)
            query = f'https://intrauam.autonoma.edu.co/intrauam2/l/url/docente/horarioAsignatura/editar_sel.php?letra={selected_letter}&periodo={self.PERIOD}&ano={self.YEAR}'
            print(f'Estoy revisando la letra {selected_letter}')
            html = self.client.get(query).content
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find(class_='datos')
            rows = table.find_all('tr')[1:]
            for row in rows:
                row_data = row.find_all('td')
                
                subject = {
                    'codigo': row_data[1].text.split(' - ')[0],
                    'nombre': row_data[1].text.split(' - ')[1],
                    'nro grupo': row_data[2].text.split(' - ')[0],
                    'grupo': row_data[2].text.split(' - ')[1],
                    'profesor': row_data[3].text,
                    'horario': row_data[4].text,
                    'salon': row_data[5].text 
                }
                self.courses.append(subject)
        return self.courses