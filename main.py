from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import barcode
from barcode.writer import ImageWriter

codes = {
            'EAN-8': 'ean8',
            'EAN-13': 'ean13',
            'UPC-A': 'upca',
            'JAN': 'jan',
            'ISBN-10': 'isbn10',
            'ISBN-13': 'isbn13',
            'ISSN': 'issn',
            'Code 39': 'code39',
            'Code 128': 'code128',
            'PZN': 'pzn'
        }

ui,_ = loadUiType("main.ui")

class MainApp(QWidget, ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.Handle_Buttons()
        self.code()
        self.comboBox.currentIndexChanged.connect(self.code)

    def Handle_UI(self):
        self.setWindowTitle("Barcode Studio")
        self.setFixedSize(480, 80)
        self.setWindowIcon(QIcon("icons/icon.png"))
        self.pushButton.setIcon(QIcon('icons/generate.png'))

    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.generate)

    def generate(self):
        try:
            c = self.code()
            text = self.lineEdit.text()
            file = barcode.get(c, text, writer=ImageWriter())
            file = file.save(r'Barcodes/'+text)
            self.setFixedSize(480, 260)
            self.label.setPixmap(QtGui.QPixmap(r'Barcodes/'+text + '.png'))
        except barcode.errors.NumberOfDigitsError as e:
            #print("-->", e)
            #self.setFixedSize(370, 50)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.setDefaultButton(QMessageBox.Retry)
            msg.exec_()
        except barcode.errors.IllegalCharacterError as e:
            #print("-->", e)
            # self.setFixedSize(370, 50)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.setDefaultButton(QMessageBox.Retry)
            msg.exec_()
        except barcode.errors.BarcodeError as e:
            #print("-->", e)
            #self.setFixedSize(370, 50)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.setDefaultButton(QMessageBox.Retry)
            msg.exec_()
        except barcode.errors.BarcodeNotFoundError as e:
            #print("-->", e)
            # self.setFixedSize(370, 50)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.setDefaultButton(QMessageBox.Retry)
            msg.exec_()
        except barcode.errors.WrongCountryCodeError as e:
            #print("-->", e)
            # self.setFixedSize(370, 50)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.setDefaultButton(QMessageBox.Retry)
            msg.exec_()
    def code(self):
        c = self.comboBox.currentText()
        #print(c)
        if c == 'EAN-8':
            self.lineEdit.setMaxLength(7)
            self.lineEdit.setPlaceholderText("Enter 7 digits")
        if c == 'EAN-13':
            self.lineEdit.setMaxLength(12)
            self.lineEdit.setPlaceholderText("Enter 12 digits")
        if c == 'UPC-A':
            self.lineEdit.setMaxLength(11)
            self.lineEdit.setPlaceholderText("Enter 11 digits")
        if c == 'JAN':
            self.lineEdit.setMaxLength(20)
            self.lineEdit.setPlaceholderText("Enter 11 digits, Country code shoud be between (450-460 or 490-500)")
        if c == 'ISBN-10':
            self.lineEdit.setMaxLength(25)
            self.lineEdit.setPlaceholderText("")
        if c == 'ISBN-13':
            self.lineEdit.setMaxLength(30)
            self.lineEdit.setPlaceholderText("")
        if c == 'ISSN':
            self.lineEdit.setMaxLength(35)
            self.lineEdit.setPlaceholderText("")
        if c == 'Code 39':
            self.lineEdit.setMaxLength(40)
            self.lineEdit.setPlaceholderText("")
        if c == 'Code 128':
            self.lineEdit.setMaxLength(45)
            self.lineEdit.setPlaceholderText("")
        if c == 'PZN':
            self.lineEdit.setMaxLength(50)
            self.lineEdit.setPlaceholderText("")
        return codes[c]

def main():
    QApplication.processEvents()
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
