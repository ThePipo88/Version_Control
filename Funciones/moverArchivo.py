import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import Funciones.carpetas as carpet
import os

class App(QWidget):

    def getFileName(self, nombre,table):
        file_filter = 'All Files ();;Python Files (.py)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='All Files ()'
        )
        print(response[0])
        carpet.carpeta.cargarArchivo(nombre, response[0],table)
        return response[0]
