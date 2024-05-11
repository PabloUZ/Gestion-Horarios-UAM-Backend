from lector import Lector
from escritor import Escritor

class Procesador:
    def __init__(self):
        self.MICRO = 0
        self.MESO = 1
        self.MACRO = 2
        self.SEMESTRES = 10
        self.tipologia_nombres = {}
        self.tipologia_nombres[self.MICRO] = "Microcurrículo"
        self.tipologia_nombres[self.MESO] = "Mesocurrículo"
        self.tipologia_nombres[self.MACRO] = "Macrocurrículo"

        self.asignaturas = {}
        self.grafos = []
        self.historial = {}
        self.tipologias = {}
        self.equivalencias = []

        self.data = {}

        self.plan = '1020'
        self.grafo = {}
        self.usuario = True

    def cargar_data(self):
        lector = Lector()
        self.asignaturas = lector.leer_json('asignaturas')
        self.grafos = lector.leer_json('grafos')
        self.historial = lector.leer_json('ejemplo_historial')
        self.tipologias = lector.leer_json('tipologia')
        self.equivalencias = lector.leer_json('equiv')
        self.grafo = self.obtener_grafo(self.plan)

    def obtener_grafo(self, plan):
        for grafo in self.grafos:
            if grafo['codigo'] == plan:
                return grafo

    def buscar_materia_estudiante(self, codigo):
        for asignatura in self.historial['historial']:
            if asignatura['codigo'] == codigo:
                return asignatura

    def buscar_equivalencias(self, codigo):
        for asignatura in self.equivalencias:
            if asignatura['codigo'] == codigo:
                return asignatura['equiv']

    def buscar_nombre_materia(self, codigo):
        return self.asignaturas[codigo]

    def obtener_codigos_por_tipo(self, tipo_materia):
        codigos = []
        for codigo, tipo in self.tipologias.items():
            if tipo == tipo_materia:
                codigos.append(codigo)
        return codigos

    def obtener_materia(self, codigo):
        materia = {'nombre': self.buscar_nombre_materia(codigo)}

        for asignatura in self.grafo['asignaturas']:
            if asignatura['codigo'] == codigo:
                materia.update(asignatura)
                if self.usuario:
                    materia = self.agregar_info_usuario(codigo, materia)
                return materia

    def agregar_info_usuario(self, codigo, materia):
        asignatura_usuario = self.buscar_materia_estudiante(codigo)
        materia['vista'] = False
        if asignatura_usuario:
            materia = self.asignar_info_usuario(materia, asignatura_usuario)
        else:
            equiv_codigos = self.buscar_equivalencias(codigo)
            if equiv_codigos:
                for equiv_codigo in equiv_codigos:
                    asignatura_usuario = self.buscar_materia_estudiante(
                        equiv_codigo)
                    if asignatura_usuario:
                        materia = self.asignar_info_usuario(materia, asignatura_usuario)
                        break

        return materia

    def asignar_info_usuario(self, materia, asignatura_usuario):
        if asignatura_usuario['nota']:
            if asignatura_usuario['nota'] > 3:
                materia['vista'] = True
                materia['periodo'] = asignatura_usuario['periodo']
                materia['nota'] = asignatura_usuario['nota']
        return materia

    def obtener_lista_materias(self, codigos):
        materias = []
        for codigo in codigos:
            asignatura = self.obtener_materia(codigo)
            if asignatura:
                materias.append(asignatura)
        return materias

    def generar_diccionario_semestres(self):
        diccionario = []
        for i in range(1, self.SEMESTRES + 1):
            diccionario.append({
                'num_semestre': i,
                'asignaturas': []
            })
        return diccionario

    def agregar_materia_diccionario(self, asignaturas, semestres):
        for semestre in semestres:
            for asignatura in asignaturas:
                if semestre['num_semestre'] == asignatura['semestre']:
                    semestre['asignaturas'].append(asignatura)
        return semestres

    def obtener_materias_por_tipo(self, tipo_materia):
        
        codigos = self.obtener_codigos_por_tipo(tipo_materia)
        asignaturas = self.obtener_lista_materias(codigos)
        semestres = self.generar_diccionario_semestres()
        semestres = self.agregar_materia_diccionario(asignaturas, semestres)
        return {
            'tipo': self.tipologia_nombres[tipo_materia],
            'semestres': semestres
        }

    def procesar_informacion(self):
        asignaturas = []
        asignaturas.append(self.obtener_materias_por_tipo(self.MICRO))
        asignaturas.append(self.obtener_materias_por_tipo(self.MESO))
        asignaturas.append(self.obtener_materias_por_tipo(self.MACRO))

        self.data['plan'] = self.grafo['codigo']
        self.data['jornada'] = self.grafo['jornada']
        if self.usuario:
            self.data['usuario'] = self.historial['usuario']
            self.data['nombre'] = self.historial['nombre']
            self.data['codigo_est'] = self.historial['codigo']

        self.data['asignaturas'] = asignaturas

    def crear_json(self):
        escritor = Escritor()
        if self.data:
            escritor.escribir_json('salida', self.data)


if __name__ == '__main__':
    procesador = Procesador()
    procesador.cargar_data()
    procesador.procesar_informacion()
    procesador.crear_json()
