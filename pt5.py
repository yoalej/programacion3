#como instalar PYQt5
print("*********************************")
print("*********************************")
print("Instalando PYQt5...")    
# pip install PyQt5
print("¡PYQt5 instalado correctamente! 🎉")
print("*********************************")  
print("*********************************")

# archivo: ejemplo_pyqt5.py
"""from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle('Ventana PyQt5')
window.setGeometry(100, 100, 300, 200)

label = QLabel('¡Hola, PyQt5 ooo!', parent=window)
label.move(100, 80)

window.show()
app.exec_()"""


#Haciendo una calculadora con PyQt5 mi primera calculadora
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import sys

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculadora PyQt5')
        self.setGeometry(100, 100, 320, 420)

        layout = QGridLayout()

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; background: #e0e0e0; color: #333; border-radius: 8px; padding: 8px;")
        layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('CE', 5, 1), ('(', 5, 2), (')', 5, 3),
        ]

        # Colores para los botones
        button_styles = {
            'C': 'background: #ff6666; color: white; font-weight: bold;',
            'CE': 'background: #ffb366; color: white; font-weight: bold;',
            '=': 'background: #66b3ff; color: white; font-weight: bold;',
            '/': 'background: #b3b3b3;',
            '*': 'background: #b3b3b3;',
            '-': 'background: #b3b3b3;',
            '+': 'background: #b3b3b3;',
            '(': 'background: #cccccc;',
            ')': 'background: #cccccc;',
        }

        for (text, row, col) in buttons:
            btn = QPushButton(text)
            btn.setFixedSize(70, 50)
            style = button_styles.get(text, 'background: #f2f2f2; color: #333;')
            btn.setStyleSheet(f"{style} font-size: 18px; border-radius: 8px;")
            btn.clicked.connect(self.on_click)
            layout.addWidget(btn, row, col)

        self.setLayout(layout)

    def on_click(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
        elif text == 'C':
            self.display.clear()
        elif text == 'CE':
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        else:
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec_())
