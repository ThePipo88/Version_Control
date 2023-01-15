import json
import sys
import Funciones.Mensajes as sms
from PyQt5 import QtWidgets
import os
data = {}
data['usuarios'] = []
class login:
    def leerUsuarios():
        with open('Usuarios/usuarios.txt') as file:
           global data
           data = json.load(file)

    def registrarUsuario(nombre, password):
        bandera = True
        if nombre and password:
            global data
            data['usuarios'].append({
                'nombre' : nombre,
                'password': password,
                'numero': 0,
                'creado': 'No'
            })
            with open('Usuarios/usuarios.txt') as file:
                info = json.load(file)
                for usuario in info['usuarios']:
                    if(usuario['nombre'] == nombre):
                        bandera = False

            if bandera == True:   
                with open('Usuarios/usuarios.txt', 'w') as outfile:          
                   outfile.write(json.dumps(data))
                   sms.MessageBox(QtWidgets.QWidget).show_message(2,'Registro','Usuario registrado con exito')
            else:
                sms.MessageBox(QtWidgets.QWidget).show_message(1,'Error','Lo sentimos, ya existe un usuario registrado con ese nombre')
    def autenficarUsuario(nombre, password):
        with open('Usuarios/usuarios.txt') as file:
            data = json.load(file)
            for usuario in data['usuarios']:
                if(usuario['nombre']==nombre and usuario['password']==password):
                    print("Autenticado")
                    break
                else:
                    print("No autenticado")
    def actualizarUsuarios(nombre):
        with open('Usuarios/usuarios.txt') as file:
            data = json.load(file)
            for usuario in data['usuarios']:
                if(usuario['nombre']==nombre and usuario['creado']=='No'):
                    usuario['creado']= 'Si'
                    with open('Usuarios/usuarios.txt', 'w') as outfile:          
                        outfile.write(json.dumps(data))
                    break
    def actualizarNumeroCommit(nombre):
        with open('Usuarios/usuarios.txt') as file:
            data = json.load(file)
            for usuario in data['usuarios']:
                if(usuario['nombre']==nombre):
                    usuario['numero']=usuario['numero']+1
                    with open('Usuarios/usuarios.txt', 'w') as outfile:          
                        outfile.write(json.dumps(data))
                    break
    def verificaNumeroCommit(nombre):
        with open('Usuarios/usuarios.txt') as file:
            data = json.load(file)
            for usuario in data['usuarios']:
                if(usuario['nombre']==nombre):
                   return usuario['numero']
    def crearCarpeta(directorio):
        try:
            os.mkdir(directorio)
        except OSError:
            print("La creación del directorio %s falló" % directorio)
        else:
            print("Se ha creado el directorio: %s " % directorio)
                