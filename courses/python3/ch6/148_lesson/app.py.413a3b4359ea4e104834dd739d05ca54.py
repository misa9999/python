import sys
from validate_cpf import validate_cpf
from generate_cpf import generate_cpf

from PyQt5.QtWidgets import QApplication, QMainWindow

from design import *


class CPF(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGenerateCPF.clicked.connect(self.generate_cpf)
        self.btnValidateCPF.clicked.connect(self.validate_cpf)

    def generate_cpf(self):
        self.labelReturn.setText(str(generate_cpf()))

    def validate_cpf(self):
        cpf = self.inputValidateCPF.text()
        self.labelReturn.setText(str(validate_cpf(cpf)))


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    cpf = CPF()
    cpf.show()
    qt.exec_()
