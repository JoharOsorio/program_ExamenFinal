# program_ExamenFinal
Instrucciones para el examen

Un Laboratorio médico desea implementar un sistema informático para la atención de sus
pacientes, y para ello, le solicitan a usted que desarrolle los siguientes requerimientos:

Crear un menú, que registre la ficha médica de un paciente, considerando los siguientes datos:
 Run, sin dígito verificador ni puntos.
 Nombre y apellidos.
 Dirección.
 Correo.
 Edad (número entero entre 1 y 90).
 Género (considere un carácter para identificarlo).
 Registros.
 Estado de Salud (Particular, Isapre o Fonasa).

El menú considera las opciones de:
1. Registrar Paciente.
2. Atención Paciente.
3. Consultar Paciente.
4. Salir.

Detalle de cada opción:
1. Registrar Paciente:
Solicitar los datos del paciente y generar una nueva ficha.
Validar los datos que lo requieran y estén especificados.

Reglas de Negocio:
● Rut - número entero que se encuentre en el rango de 3999999 y 22000000.
● Edad - número entero que se encuentre en el rango 1 y 90.
● Género - caracter que lo defina – usted los asigna.
● Estado de Salud - cadena de caracteres que acepta – Particular. Isapre o Fonasa.
● Correo - cadena de caracteres que contenga al menos un carácter “@”. Ej: juan@lopez.

2. Atención Paciente
Solicitar el Run del paciente.
Verificar que el Paciente se encuentre registrado en el sistema.
Ingresar fecha y observaciones de la visita, éstos datos se almacenan en registros, concatenando
los registros anteriores con el nuevo registro.

3. Consultar Paciente:
Mostrar por pantalla todos los datos del paciente, si el run ingresado se encuentra en el sistema.
Mostrar la información ordenada por apellido.

4. Salir
Al salir de la aplicación, debe mostrar la fecha actual, el nombre y apellido de cada integrante
del grupo, asignatura y la versión de la aplicación.
Verifique si realmente desea salir del programa.
