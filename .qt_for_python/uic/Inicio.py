# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Inicio.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Git(object):
    def setupUi(self, Git):
        if not Git.objectName():
            Git.setObjectName(u"Git")
        Git.resize(1003, 733)
        Git.setStyleSheet(u"background-color: rgb(32, 73, 116)")
        self.centralwidget = QWidget(Git)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1011, 721))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(32, 73, 116)")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.page_inicio.setAutoFillBackground(False)
        self.page_inicio.setStyleSheet(u"")
        self.btn_iniciarSesion = QPushButton(self.page_inicio)
        self.btn_iniciarSesion.setObjectName(u"btn_iniciarSesion")
        self.btn_iniciarSesion.setGeometry(QRect(430, 420, 171, 31))
        self.btn_iniciarSesion.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.label = QLabel(self.page_inicio)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 160, 431, 41))
        self.label.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.label_2 = QLabel(self.page_inicio)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 250, 111, 21))
        self.label_2.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.label_3 = QLabel(self.page_inicio)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 340, 121, 21))
        self.label_3.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.btn_registrar = QPushButton(self.page_inicio)
        self.btn_registrar.setObjectName(u"btn_registrar")
        self.btn_registrar.setGeometry(QRect(430, 470, 171, 31))
        self.btn_registrar.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.text_usuario = QLineEdit(self.page_inicio)
        self.text_usuario.setObjectName(u"text_usuario")
        self.text_usuario.setGeometry(QRect(480, 250, 191, 31))
        self.text_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font-weight: bold;")
        self.text_password = QLineEdit(self.page_inicio)
        self.text_password.setObjectName(u"text_password")
        self.text_password.setGeometry(QRect(480, 340, 191, 31))
        self.text_password.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 18px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_inicio)
        self.page_registro = QWidget()
        self.page_registro.setObjectName(u"page_registro")
        self.label_4 = QLabel(self.page_registro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 350, 121, 21))
        self.label_4.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.text_usuarioRegistro = QLineEdit(self.page_registro)
        self.text_usuarioRegistro.setObjectName(u"text_usuarioRegistro")
        self.text_usuarioRegistro.setGeometry(QRect(500, 260, 191, 31))
        self.text_usuarioRegistro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font-weight: bold;")
        self.text_passwordRegistro = QLineEdit(self.page_registro)
        self.text_passwordRegistro.setObjectName(u"text_passwordRegistro")
        self.text_passwordRegistro.setGeometry(QRect(500, 350, 191, 31))
        self.text_passwordRegistro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 18px;\n"
"font-weight: bold;")
        self.label_5 = QLabel(self.page_registro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(380, 260, 111, 21))
        self.label_5.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.label_6 = QLabel(self.page_registro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(440, 160, 151, 51))
        self.label_6.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.btn_registrarse = QPushButton(self.page_registro)
        self.btn_registrarse.setObjectName(u"btn_registrarse")
        self.btn_registrarse.setGeometry(QRect(470, 440, 171, 31))
        self.btn_registrarse.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_atrasRegistro = QPushButton(self.page_registro)
        self.btn_atrasRegistro.setObjectName(u"btn_atrasRegistro")
        self.btn_atrasRegistro.setGeometry(QRect(470, 490, 171, 31))
        self.btn_atrasRegistro.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_registro)
        self.page_adminCreaRepo = QWidget()
        self.page_adminCreaRepo.setObjectName(u"page_adminCreaRepo")
        self.btn_crearRepoPrincipal = QPushButton(self.page_adminCreaRepo)
        self.btn_crearRepoPrincipal.setObjectName(u"btn_crearRepoPrincipal")
        self.btn_crearRepoPrincipal.setGeometry(QRect(370, 300, 281, 31))
        self.btn_crearRepoPrincipal.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_administrarRepositorioPrincipal = QPushButton(self.page_adminCreaRepo)
        self.btn_administrarRepositorioPrincipal.setObjectName(u"btn_administrarRepositorioPrincipal")
        self.btn_administrarRepositorioPrincipal.setGeometry(QRect(370, 370, 281, 31))
        self.btn_administrarRepositorioPrincipal.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.label_7 = QLabel(self.page_adminCreaRepo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(430, 160, 171, 41))
        self.label_7.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.btn_atrasOpcionesAdmin = QPushButton(self.page_adminCreaRepo)
        self.btn_atrasOpcionesAdmin.setObjectName(u"btn_atrasOpcionesAdmin")
        self.btn_atrasOpcionesAdmin.setGeometry(QRect(430, 590, 171, 31))
        self.btn_atrasOpcionesAdmin.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_adminCreaRepo)
        self.page_userCreaRepo = QWidget()
        self.page_userCreaRepo.setObjectName(u"page_userCreaRepo")
        self.label_8 = QLabel(self.page_userCreaRepo)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(430, 140, 171, 41))
        self.label_8.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.btn_crearRepoUser = QPushButton(self.page_userCreaRepo)
        self.btn_crearRepoUser.setObjectName(u"btn_crearRepoUser")
        self.btn_crearRepoUser.setGeometry(QRect(380, 260, 271, 31))
        self.btn_crearRepoUser.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_administrarRepositorioUser = QPushButton(self.page_userCreaRepo)
        self.btn_administrarRepositorioUser.setObjectName(u"btn_administrarRepositorioUser")
        self.btn_administrarRepositorioUser.setGeometry(QRect(340, 350, 341, 31))
        self.btn_administrarRepositorioUser.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_atrasOpcionesUser = QPushButton(self.page_userCreaRepo)
        self.btn_atrasOpcionesUser.setObjectName(u"btn_atrasOpcionesUser")
        self.btn_atrasOpcionesUser.setGeometry(QRect(430, 590, 171, 31))
        self.btn_atrasOpcionesUser.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_userCreaRepo)
        self.page_carpetas = QWidget()
        self.page_carpetas.setObjectName(u"page_carpetas")
        self.label_9 = QLabel(self.page_carpetas)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(440, 60, 171, 41))
        self.label_9.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.btn_AdministrarCarpeta = QPushButton(self.page_carpetas)
        self.btn_AdministrarCarpeta.setObjectName(u"btn_AdministrarCarpeta")
        self.btn_AdministrarCarpeta.setGeometry(QRect(400, 550, 241, 31))
        self.btn_AdministrarCarpeta.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.frame_2 = QFrame(self.page_carpetas)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(280, 150, 471, 341))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.tbCarpetas = QTableWidget(self.frame_2)
        if (self.tbCarpetas.columnCount() < 1):
            self.tbCarpetas.setColumnCount(1)
        font = QFont()
        font.setPointSize(8)
        font.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(0, 0, 0));
        self.tbCarpetas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tbCarpetas.rowCount() < 17):
            self.tbCarpetas.setRowCount(17)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(9, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(10, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(11, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(12, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(13, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(14, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(15, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbCarpetas.setVerticalHeaderItem(16, __qtablewidgetitem17)
        self.tbCarpetas.setObjectName(u"tbCarpetas")
        self.tbCarpetas.setGeometry(QRect(0, 0, 471, 341))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.tbCarpetas.sizePolicy().hasHeightForWidth())
        self.tbCarpetas.setSizePolicy(sizePolicy)
        self.tbCarpetas.horizontalHeader().setDefaultSectionSize(450)
        self.btn_atrasCarpetas = QPushButton(self.page_carpetas)
        self.btn_atrasCarpetas.setObjectName(u"btn_atrasCarpetas")
        self.btn_atrasCarpetas.setGeometry(QRect(430, 620, 171, 31))
        self.btn_atrasCarpetas.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_carpetas)
        self.page_administrarCarpetasUser = QWidget()
        self.page_administrarCarpetasUser.setObjectName(u"page_administrarCarpetasUser")
        self.label_10 = QLabel(self.page_administrarCarpetasUser)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(290, 20, 471, 41))
        self.label_10.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.btn_asignarPermisos = QPushButton(self.page_administrarCarpetasUser)
        self.btn_asignarPermisos.setObjectName(u"btn_asignarPermisos")
        self.btn_asignarPermisos.setGeometry(QRect(300, 580, 211, 31))
        self.btn_asignarPermisos.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_commit = QPushButton(self.page_administrarCarpetasUser)
        self.btn_commit.setObjectName(u"btn_commit")
        self.btn_commit.setGeometry(QRect(300, 510, 211, 31))
        self.btn_commit.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_update = QPushButton(self.page_administrarCarpetasUser)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setGeometry(QRect(560, 510, 211, 31))
        self.btn_update.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_recuperarArchivos = QPushButton(self.page_administrarCarpetasUser)
        self.btn_recuperarArchivos.setObjectName(u"btn_recuperarArchivos")
        self.btn_recuperarArchivos.setGeometry(QRect(560, 580, 211, 31))
        self.btn_recuperarArchivos.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.frame = QFrame(self.page_administrarCarpetasUser)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(290, 80, 471, 341))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tbContenido = QTableWidget(self.frame)
        if (self.tbContenido.columnCount() < 1):
            self.tbContenido.setColumnCount(1)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        __qtablewidgetitem18.setFont(font);
        __qtablewidgetitem18.setBackground(QColor(0, 0, 0));
        self.tbContenido.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        if (self.tbContenido.rowCount() < 17):
            self.tbContenido.setRowCount(17)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(8, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(9, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(10, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(11, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(12, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(13, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(14, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(15, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tbContenido.setVerticalHeaderItem(16, __qtablewidgetitem35)
        self.tbContenido.setObjectName(u"tbContenido")
        self.tbContenido.setGeometry(QRect(0, 0, 471, 341))
        sizePolicy.setHeightForWidth(self.tbContenido.sizePolicy().hasHeightForWidth())
        self.tbContenido.setSizePolicy(sizePolicy)
        self.tbContenido.horizontalHeader().setDefaultSectionSize(450)
        self.btn_agregarArchivo = QPushButton(self.page_administrarCarpetasUser)
        self.btn_agregarArchivo.setObjectName(u"btn_agregarArchivo")
        self.btn_agregarArchivo.setGeometry(QRect(300, 450, 211, 28))
        self.btn_agregarArchivo.setStyleSheet(u"background-color: #ffffff;\n"
"font-family: ebrima;\n"
"color:rgb(0,0,0);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_eliminarArchivo = QPushButton(self.page_administrarCarpetasUser)
        self.btn_eliminarArchivo.setObjectName(u"btn_eliminarArchivo")
        self.btn_eliminarArchivo.setGeometry(QRect(560, 450, 211, 28))
        self.btn_eliminarArchivo.setStyleSheet(u"background-color: #ffffff;\n"
"font-family: ebrima;\n"
"color:rgb(0,0,0);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_atrasAdminCarp = QPushButton(self.page_administrarCarpetasUser)
        self.btn_atrasAdminCarp.setObjectName(u"btn_atrasAdminCarp")
        self.btn_atrasAdminCarp.setGeometry(QRect(450, 640, 171, 31))
        self.btn_atrasAdminCarp.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_administrarCarpetasUser)
        self.page_recuperacionArchivos = QWidget()
        self.page_recuperacionArchivos.setObjectName(u"page_recuperacionArchivos")
        self.label_13 = QLabel(self.page_recuperacionArchivos)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(280, 50, 461, 41))
        self.label_13.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_recuperacionArchivos)
        self.page_asignarPermisosUser = QWidget()
        self.page_asignarPermisosUser.setObjectName(u"page_asignarPermisosUser")
        self.label_11 = QLabel(self.page_asignarPermisosUser)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(280, 160, 481, 51))
        self.label_11.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.text_usuarioPermiso = QLineEdit(self.page_asignarPermisosUser)
        self.text_usuarioPermiso.setObjectName(u"text_usuarioPermiso")
        self.text_usuarioPermiso.setGeometry(QRect(490, 290, 191, 31))
        self.text_usuarioPermiso.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 18px;\n"
"font-weight: bold;")
        self.label_12 = QLabel(self.page_asignarPermisosUser)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(380, 290, 111, 21))
        self.label_12.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.btn_crearPermiso = QPushButton(self.page_asignarPermisosUser)
        self.btn_crearPermiso.setObjectName(u"btn_crearPermiso")
        self.btn_crearPermiso.setGeometry(QRect(480, 490, 171, 31))
        self.btn_crearPermiso.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.check_lectura = QRadioButton(self.page_asignarPermisosUser)
        self.check_lectura.setObjectName(u"check_lectura")
        self.check_lectura.setGeometry(QRect(420, 400, 141, 20))
        self.check_lectura.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.check_escritura = QRadioButton(self.page_asignarPermisosUser)
        self.check_escritura.setObjectName(u"check_escritura")
        self.check_escritura.setGeometry(QRect(590, 400, 141, 20))
        self.check_escritura.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.btn_atrasPermisos = QPushButton(self.page_asignarPermisosUser)
        self.btn_atrasPermisos.setObjectName(u"btn_atrasPermisos")
        self.btn_atrasPermisos.setGeometry(QRect(480, 550, 171, 31))
        self.btn_atrasPermisos.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_asignarPermisosUser)
        Git.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Git)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1003, 21))
        Git.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Git)
        self.statusbar.setObjectName(u"statusbar")
        Git.setStatusBar(self.statusbar)

        self.retranslateUi(Git)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Git)
    # setupUi

    def retranslateUi(self, Git):
        Git.setWindowTitle(QCoreApplication.translate("Git", u"Git", None))
        self.btn_iniciarSesion.setText(QCoreApplication.translate("Git", u"Iniciar sesi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Git", u"Bienvenido a Git Papus", None))
        self.label_2.setText(QCoreApplication.translate("Git", u"Usuario:", None))
        self.label_3.setText(QCoreApplication.translate("Git", u"Password:", None))
        self.btn_registrar.setText(QCoreApplication.translate("Git", u"Registrarse", None))
        self.label_4.setText(QCoreApplication.translate("Git", u"Password:", None))
        self.label_5.setText(QCoreApplication.translate("Git", u"Usuario:", None))
        self.label_6.setText(QCoreApplication.translate("Git", u"Registro", None))
        self.btn_registrarse.setText(QCoreApplication.translate("Git", u"Registrarse", None))
        self.btn_atrasRegistro.setText(QCoreApplication.translate("Git", u"Atr\u00e1s", None))
        self.btn_crearRepoPrincipal.setText(QCoreApplication.translate("Git", u"Crear Repositorio Principal", None))
        self.btn_administrarRepositorioPrincipal.setText(QCoreApplication.translate("Git", u"Administrar Repositorio", None))
        self.label_7.setText(QCoreApplication.translate("Git", u"Opciones", None))
        self.btn_atrasOpcionesAdmin.setText(QCoreApplication.translate("Git", u"Atr\u00e1s", None))
        self.label_8.setText(QCoreApplication.translate("Git", u"Opciones", None))
        self.btn_crearRepoUser.setText(QCoreApplication.translate("Git", u"Crear carpeta repositorio", None))
        self.btn_administrarRepositorioUser.setText(QCoreApplication.translate("Git", u"Administrar Repositorio Usuario", None))
        self.btn_atrasOpcionesUser.setText(QCoreApplication.translate("Git", u"Atr\u00e1s", None))
        self.label_9.setText(QCoreApplication.translate("Git", u"Carpetas", None))
        self.btn_AdministrarCarpeta.setText(QCoreApplication.translate("Git", u"Administrar Carpeta", None))
        ___qtablewidgetitem = self.tbCarpetas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Git", u"Nombre", None));
        self.btn_atrasCarpetas.setText(QCoreApplication.translate("Git", u"Atr\u00e1s", None))
        self.label_10.setText(QCoreApplication.translate("Git", u"Administracion de carpeta", None))
        self.btn_asignarPermisos.setText(QCoreApplication.translate("Git", u"Asignar permisos", None))
        self.btn_commit.setText(QCoreApplication.translate("Git", u"Commit", None))
        self.btn_update.setText(QCoreApplication.translate("Git", u"Update", None))
        self.btn_recuperarArchivos.setText(QCoreApplication.translate("Git", u"Recuperar archivos", None))
        ___qtablewidgetitem1 = self.tbContenido.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Git", u"Nombre", None));
        self.btn_agregarArchivo.setText(QCoreApplication.translate("Git", u"Agregar Archivo", None))
        self.btn_eliminarArchivo.setText(QCoreApplication.translate("Git", u"Eliminar Archivo", None))
        self.btn_atrasAdminCarp.setText(QCoreApplication.translate("Git", u"Atr\u00e1s", None))
        self.label_13.setText(QCoreApplication.translate("Git", u"Recuperaci\u00f3n de archivos", None))
        self.label_11.setText(QCoreApplication.translate("Git", u"Asignar permisos a usuario", None))
        self.label_12.setText(QCoreApplication.translate("Git", u"Usuario:", None))
        self.btn_crearPermiso.setText(QCoreApplication.translate("Git", u"Crear Permiso", None))
        self.check_lectura.setText(QCoreApplication.translate("Git", u"Lectura", None))
        self.check_escritura.setText(QCoreApplication.translate("Git", u"Escritura", None))
        self.btn_atrasPermisos.setText(QCoreApplication.translate("Git", u"Atr\u00e1s", None))
    # retranslateUi

