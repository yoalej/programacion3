#como instalar PYQt5
print("*********************************")
print("*********************************")
print("Instalando PYQt5...")    
# pip install PyQt5
print("¡PYQt5 instalado correctamente! 🎉")
print("*********************************")  
print("*********************************")

# archivo: ejemplo_pyqt5.py
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle('Ventana PyQt5')
window.setGeometry(100, 100, 300, 200)

label = QLabel('¡Hola, PyQt5 ooo!', parent=window)
label.move(100, 80)

window.show()
app.exec_()


