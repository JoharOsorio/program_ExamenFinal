import datetime
import re

class Paciente:
    def __init__(self, rut, nombre, apellidos, direccion, correo, edad, genero, estado_salud):
        self.rut = rut
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.correo = correo
        self.edad = edad
        self.genero = genero
        self.estado_salud = estado_salud
        self.registros = []

    def mostrar_informacion(self):
        print(f"RUT: {self.rut}\nNombre: {self.nombre}\nApellidos: {self.apellidos}\nDirección: {self.direccion}\nCorreo: {self.correo}\nEdad: {self.edad}\nGénero: {self.genero}\nEstado de Salud: {self.estado_salud}\nRegistros: {self.registros}")


class Sistema:
    def __init__(self):
        self.pacientes = []

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def obtener_paciente(self, rut):
        for paciente in self.pacientes:
            if paciente.rut == rut:
                return paciente
        return None

    def atender_paciente(self, rut, fecha, observacion):
        paciente = self.obtener_paciente(rut)
        if paciente:
            paciente.registros.append({"fecha": fecha, "observacion": observacion})
            print("Registro de atención añadido con éxito.")
        else:
            print("El paciente no existe en el sistema.")

sistema = Sistema()

while True:
    print("Menú de Opciones:")
    print("1. Registrar Paciente")
    print("2. Atención Paciente")
    print("3. Consultar Paciente")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        rut_valido = False
        while not rut_valido:
            rut = input("Ingrese el RUT del paciente (formato 11111111-X): ")
            if re.match("^[0-9]{7,8}-[0-9Kk]$", rut):
                rut_valido = True
            else:
                print("Formato de RUT incorrecto, intente nuevamente.")
        
        nombre = input("Ingrese el nombre del paciente: ")
        apellidos = input("Ingrese los apellidos del paciente: ")
        direccion = input("Ingrese la dirección del paciente: ")

        correo_valido = False
        while not correo_valido:
            correo = input("Ingrese el correo del paciente: ")
            if "@" in correo:
                correo_valido = True
            else:
                print("Correo inválido, intente nuevamente.")

        edad_valida = False
        while not edad_valida:
            edad = int(input("Ingrese la edad del paciente: "))
            if 1 <= edad <= 90:
                edad_valida = True
            else:
                print("Edad inválida, intente nuevamente.")

        genero_valido = False
        while not genero_valido:
            genero = input("Ingrese el género del paciente (M/F): ")
            if genero in ["M", "F"]:
                genero_valido = True
            else:
                print("Género inválido, intente nuevamente.")

        estado_salud_valido = False
        while not estado_salud_valido:
            estado_salud = input("Ingrese la previsión del paciente (Particular/Isapre/Fonasa): ")
            if estado_salud in ["Particular", "Isapre", "Fonasa"]:
                estado_salud_valido = True
            else:
                print("Estado de salud inválido, intente nuevamente.")
        
        paciente = Paciente(rut, nombre, apellidos, direccion, correo, edad, genero, estado_salud)
        sistema.registrar_paciente(paciente)

    elif opcion == 2:
        rut = input("Ingrese el RUT del paciente: ")
        fecha_valida = False
        while not fecha_valida:
            fecha = input("Ingrese la fecha de la visita (formato DD/MM/AAAA): ")
            try:
                datetime.datetime.strptime(fecha, "%d/%m/%Y")
                fecha_valida = True
            except:
                print("Formato de fecha incorrecto, intente nuevamente.")
        observacion = input("Ingrese la observación de la visita: ")
        sistema.atender_paciente(rut, fecha, observacion)

    elif opcion == 3:
        rut = input("Ingrese el RUT del paciente: ")
        paciente = sistema.obtener_paciente(rut)
        if paciente:
            paciente.mostrar_informacion()
        else:
            print("El paciente no existe en el sistema.")

    elif opcion == 4:
        print("Fecha actual: ", datetime.datetime.now().strftime("%d/%m/%Y"))
        print("Integrantes del grupo: Juan, Pedro, María")
        print("Asignatura: Programación en Python")
        print("Versión de la aplicación: 1.0")
        confirmacion = input("¿Estás seguro de que quieres salir? (S/N): ")
        if confirmacion.lower() == "s":
            break
