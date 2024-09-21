from PyQt5.QtWidgets import QApplication, QVBoxLayout, QTextEdit, QLineEdit, QWidget, QPushButton, QMessageBox, QLabel
class MyWindow(QWidget):
   def __init__(self):
      super().__init__()

      self.ism = QLabel("Ism", self)
      self.ism_input = QLineEdit(self)

      self.Email = QLabel("Email", self)
      self.Email_input = QLineEdit(self)

      self.tarjimaiXol = QLabel("Qisqacha tarjimai xol", self)
      self.tarjimaiXol_input = QLineEdit(self)

      self.Button1 = QPushButton(self)
      self.Button1.clicked.connect(self.ShowMessage)
      self.Button1.setText("Submmit")

      self.natija1 = QTextEdit(self)
      self.natija1.setReadOnly(True)
      
      self.setFixedSize(550, 300)

      layout = QVBoxLayout()
      layout.addWidget(self.ism)
      layout.addWidget(self.ism_input)
      layout.addWidget(self.Email)
      layout.addWidget(self.Email_input)
      layout.addWidget(self.tarjimaiXol)
      layout.addWidget(self.tarjimaiXol_input)
      layout.addWidget(self.Button1)
      layout.addWidget(self.natija1)

      self.setLayout(layout)
      self.setWindowTitle("Ma'lumotlarni kiriting!")
      self.show()
      
   def ShowMessage(self):
      ism = self.ism_input.text()
      Email = self.Email_input.text()
      tarjimaiXol = self.tarjimaiXol_input.text()

      natija = (f"Ism: {ism}\nEmail: {Email}\nTarjimaiXol: {tarjimaiXol}")
      self.natija1.setText(natija)
      
myApp = QApplication([])
window = MyWindow()
myApp.exec_()