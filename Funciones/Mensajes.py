

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import platform
import json
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import json




class MessageBox(QtWidgets.QWidget):# Heredado de la clase padre QtWidgets.QWidget

    

    def __init__(self,parent = None):#parent = None significa que este QWidget pertenece a la ventana superior, que es MainWindows.
        QtWidgets.QWidget.__init__(self)#Debido a la relación de herencia, para inicializar la clase padre
        #Inicialice la clase padre a través de super, la función __init __ () no tiene self, si es directamente QtWidgets.QWidget .__ init __ (self), hay self entre paréntesis
        self.setGeometry(300, 300, 1500,500) # setGeometry () realiza dos funciones: establecer la posición de la ventana en la pantalla y establecer el tamaño de la ventana en sí. Sus dos primeros parámetros son las coordenadas xey de la ventana en la pantalla. Los dos últimos parámetros son el ancho y el alto de la propia ventana.
        self.setWindowTitle(u'ventana')  # Establezca el título del formulario, esta fila es opcional.
        self.button = QtWidgets.QPushButton(u'prueba', self)  # Cree un botón para mostrar la palabra "prueba"
        self.button.move(300,300)
        self.button.clicked.connect(self.show_message)  # Ranura de señal
        self.tipo = 0
        

    def show_message(self,tipo,titulo,mensaje):
            if tipo == 1:
              QtWidgets.QMessageBox.critical(self, titulo, mensaje)
            elif tipo == 2:
              QtWidgets.QMessageBox.information(self, titulo, mensaje) 
