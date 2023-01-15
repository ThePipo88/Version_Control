import json
import sys
import Funciones.Mensajes as sms
from PyQt5 import QtWidgets
import os
data = {}
data['permisos'] = []
formaPermiso = ''
class permiso:
    def leerPermisos():
        with open('Usuarios/permisos.txt') as file:
           global data
           data = json.load(file)
    def registrarPermiso(nombreDueno, nombreInvitado, permiso):
        bandera = True
        banderaUser = False
        banderaActualizar = False
        global data
        if nombreDueno and nombreInvitado and permiso:
            with open('Usuarios/permisos.txt') as file:
                data = json.load(file)
            data['permisos'].append({
                'nombreDueno' : nombreDueno,
                'nombreInvitado': nombreInvitado,
                'permiso': permiso
            })
            with open('Usuarios/permisos.txt') as file:
                info = json.load(file)
                for permisoc in info['permisos']:
                    if(permisoc['nombreDueno'] == nombreDueno and permisoc['nombreInvitado'] == nombreInvitado and permisoc['permiso'] == permiso):
                        bandera = False
                        break
                    if(permisoc['nombreDueno'] == nombreDueno and permisoc['nombreInvitado'] == nombreInvitado):
                        
                        permisoc['permiso'] = permiso
                        with open('Usuarios/permisos.txt', 'w') as outfile1: 
                            outfile1.write(json.dumps(info))
                        banderaActualizar = True
                        break
            with open('Usuarios/usuarios.txt') as file:
                infou = json.load(file)
                for usuario in infou['usuarios']:
                    if(usuario['nombre'] == nombreInvitado):
                        banderaUser = True

            if bandera == True: 
                if banderaActualizar == True:
                    print("Se actualizo el permiso")
                else:
                    with open('Usuarios/permisos.txt', 'w') as outfile:          
                        outfile.write(json.dumps(data))
                        sms.MessageBox(QtWidgets.QWidget).show_message(2,'Registro','Permiso guardado con exito')
            else:
                if(banderaUser == False):
                    sms.MessageBox(QtWidgets.QWidget).show_message(1,'Error','Lo sentimos, el usuario al cual se le asignara el permiso no existe')
                else:
                    sms.MessageBox(QtWidgets.QWidget).show_message(1,'Error','Lo sentimos, ya existe ese permiso')

    def verificarPermisosUsuario(nombre):
        perm = []
        ingresado = False
        with open('Usuarios/permisos.txt') as file:
            data = json.load(file)
            for permiso in data['permisos']:
                if(permiso['nombreInvitado']==nombre):
                    perm.append(permiso['nombreDueno'])
                else:
                    if ingresado == False:
                      perm.append(nombre)  
                      ingresado = True  
        return perm
    def verificarTipoPermiso(nombreInvitado, nombreDueno):
        global data
        with open('Usuarios/permisos.txt') as file:
            data = json.load(file)
            formaPermiso=''
            for permiso in data['permisos']:
                if(permiso['nombreInvitado']==nombreInvitado and permiso['nombreDueno']==nombreDueno and permiso['permiso']=='lectura'):
                    formaPermiso='lectura'
                    return formaPermiso+''
                if(permiso['nombreInvitado']==nombreInvitado and permiso['nombreDueno']==nombreDueno and permiso['permiso']=='escritura'):
                    formaPermiso = 'escritura'
                    return formaPermiso+''

        