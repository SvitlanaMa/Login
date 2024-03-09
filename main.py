from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QButtonGroup, QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt  

app = QApplication([])
window = QWidget()
window.resize(600, 500)
window.setWindowTitle("Login")
window.show()


main_line = QVBoxLayout()
line1 = QHBoxLayout()
button1 = QPushButton("login")


window.setLayout(line1)

line1.addWidget(button1, alignment=Qt.AlignCenter)




app.exec_()