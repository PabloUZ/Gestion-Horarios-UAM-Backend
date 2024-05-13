class CourseProcessor:
    def __init__(self):
        self.raw_courses: list = None
        self.courses = {}

    def set_courses(self, courses):
        if courses:
            self.raw_courses = courses

    def process(self) -> dict:
        if self.raw_courses:
            for course in self.raw_courses:
                self.add_course(course['codigo'], course['nombre'], 0, None)
                self.add_group(
                    course['codigo'], course['nro grupo'], course['grupo'], course['profesor'])
                self.add_classtime(
                    course['codigo'], course['nro grupo'], course['horario'], course['salon'])
            
            return self.courses

    def add_course(self, code, course_name, credits, type):
        if code not in self.courses:
            self.courses[code] = {
                'code': code,
                'name': course_name,
                'credits': credits,
                'type': type,
                'groups': []
            }

    def add_group(self, code, group_number, group_name, proffesor):
        if code in self.courses:
            agregar = True
            for group in self.courses[code]['groups']:
                if group['number'] == group_number:
                    agregar = False

            if agregar:
                self.courses[code]['groups'].append({
                        'name': group_name,
                        'number': group_number,
                        'proffesor': proffesor,
                        'classtimes': []
                    })

    def add_classtime(self, code, group_number, classtime, room):
        if code in self.courses:
            for group in self.courses[code]['groups']:
                classtime_split = []
                if group['number'] == group_number:
                    classtime_split = classtime.split()
                    if len(classtime_split) == 4:
                        day = classtime_split[0]
                        start = classtime_split[1].split(':')
                        end = classtime_split[3].split(':')

                        start_hour = int(start[0])
                        start_minute = int(start[1])

                        end_hour = int(end[0])
                        end_minute = int(end[1])

                        group['classtimes'].append({
                            'day': day,
                            'start_hour': start_hour,
                            'start_minute': start_minute,
                            'end_hour': end_hour,
                            'end_minute': end_minute,
                            'room': room
                        })
                    else:
                        group['classtimes'].append({
                            'day': '',
                            'start_hour': 0,
                            'start_minute': 0,
                            'end_hour': 0,
                            'end_minute': 0,
                            'room': room
                        })

