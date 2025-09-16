# Usando pip list

#Este es el comando más común y fácil de leer para ver los paquetes instalados.
#  Muestra una tabla con el nombre del paquete y su versión.


#pip list
#Si quieres ver los paquetes que tienen actualizaciones disponibles, puedes usar:


#pip list --outdated
#Esto mostrará una tabla con los paquetes que no están en su última versión,

#pip install requests==
#Esto fallará, pero en el mensaje de error mostrará una lista de todas
#las versiones de requests que puedes instalar. Es un truco muy útil.

#pip install requests==2.25.1
#Esto instalará la versión 2.26.1 de requests.

#py -m venv mi_primer-entorno-v
#Este comando le dice a Windows: "Usa el lanzador py para ejecutar el módulo (-m) de Python 
# llamado venv y crea un entorno llamado mi_primer-entorno-v".

#pip freeze > requirements.txt
#Este comando crea un archivo llamado requirements.txt que contiene una lista de todos los paquetes
# instalados en el entorno virtual, junto con sus versiones exactas.


print("*********************************")
print("*********************************")

# archivo: ejemplo_math.py
import math

# Datos de los catetos
cateto_a = 3
cateto_b = 4

# Calculamos la suma de los cuadrados
suma_cuadrados = cateto_a**2 + cateto_b**2

# Usamos math.sqrt() para encontrar la hipotenusa
hipotenusa = math.sqrt(suma_cuadrados)

print(f"La raíz cuadrada de {suma_cuadrados} es: {hipotenusa}")
print(f"La hipotenusa de un triángulo con lados {cateto_a} y {cateto_b} es {hipotenusa}")

print("¡Cálculo completado! 📐")

print("*********************************")
print("*********************************")
# archivo: ejemplo_random.py
import random

print("Lanzando un dado de 6 caras...")

# Genera un número entero aleatorio entre 1 y 6
resultado_dado = random.randint(1, 6)

print(f"¡El resultado es: {resultado_dado}! 🎲")
print("¡Gracias por jugar! 🎉")
print("*********************************")
print("*********************************")
# archivo: ejemplo_statistics.py
import statistics

# Lista de calificaciones de un estudiante
calificaciones = [8, 10, 7, 9, 8, 10]

# Usamos statistics.mean() para calcular el promedio
promedio = statistics.mean(calificaciones)

print(f"Las calificaciones son: {calificaciones}")
print(f"El promedio final es: {promedio}")

print("¡Cálculo de promedio completado! 🎓")
print("*********************************")
print("*********************************")

# archivo: ejemplo_time.py
import time

print("Iniciando cuenta regresiva... 🚀")

# Pausa de 1 segundo
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)

print("¡Despegue!")
print("¡Gracias por esperar! ⏳")
print("*********************************")
print("*********************************")

# archivo: ejemplo_datetime.py
import datetime

# Obtenemos la fecha de hoy
fecha_de_hoy = datetime.date.today()

print(f"¡Hola! Hoy es {fecha_de_hoy}.")

# Puedes acceder a sus partes
print(f"Año: {fecha_de_hoy.year}")
print(f"Mes: {fecha_de_hoy.month}")
print(f"Día: {fecha_de_hoy.day}")

print("¡Gracias por usar datetime! 📅")
print("*********************************")
print("*********************************")

# archivo: ejemplo_os.py
import os       
print("Listando archivos en el directorio actual:")
# Listamos los archivos en el directorio actual
archivos = os.listdir('.')
for archivo in archivos:
    print(f"- {archivo}")   
print("¡Gracias por usar 2os! 📂")
print("*********************************")
print("*********************************")  

# archivo: ejemplo_sys.py
import sys      
print("Información del sistema:")
# Mostramos la versión de Python  
print(f"Versión de Python: {sys.version}")
print(f"Plataforma: {sys.platform}")
print("¡Gracias por usar sys! 💻"   )
print("*********************************")
