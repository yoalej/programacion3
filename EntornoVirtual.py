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