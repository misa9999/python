import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Resize(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.open_image)
        self.btnRedimensionar.clicked.connect(self.resize_image)
        self.btnSalvar.clicked.connect(self.save)

    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            "Open Image",
            "/home/anthrax/Pictures/",
            options=QFileDialog.DontUseNativeDialog,
        )
        self.inputAbrirArquivo.setText(image)
        self.original_img = QPixmap(image)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def resize_image(self):
        height = int(self.inputLargura.text())
        self.new_image = self.original_img.scaledToWidth(height)
        self.labelImg.setPixmap(self.new_image)
        self.inputLargura.setText(str(self.new_image.width()))
        self.inputAltura.setText(str(self.new_image.height()))

    def save(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            "Save Image",
            "/home/anthrax/Documents/",
            options=QFileDialog.DontUseNativeDialog,
        )
        self.new_image.save(image, "PNG")


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    resize = Resize()
    resize.show()
    qt.exec_()
