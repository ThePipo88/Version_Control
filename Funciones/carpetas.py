from PyQt5 import QtWidgets, uic,QtGui
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import Funciones.Mensajes as sms
from os import remove
from Funciones.permisos import permiso
import os
import json
import sys
import shutil
import Funciones.login as log

carpSelect = ''
commitSelect = ''
class carpeta():

    def crearCapetaUsuario(self,nombre):
        directorio = 'repositorio/'+nombre
        directorio_permanente = directorio+"/permanente"
        directorio_temporal = directorio+"/temporal"
        print("creado")
        try:
            os.mkdir(directorio)
            os.mkdir(directorio_permanente)
            os.mkdir(directorio_temporal)
        except OSError:
            print("La creación del directorio %s falló" % directorio)
        else:
            print("Se ha creado el directorio: %s " % directorio+" y sus carpetas hijas")
    
    def llenarTablaCarpetas(self,table,nombre):
          table.clearContents()
          if nombre == 'admin':
              contenidos = os.listdir('repositorio')
          else: 
              contenidos = permiso.verificarPermisosUsuario(nombre) 
          us = 0
          for elemento in contenidos:
              table.setItem(us,0, QTableWidgetItem(contenidos[us]))
              us += 1
              
    def llenarTablaRecuperacion(self,table,nombre):
        table.clearContents()
        directorio = 'repositorio/'+ nombre+'/permanente'
        contenidos=os.listdir(directorio)
        us = 0
        for elemento in contenidos:
            table.setItem(us,0, QTableWidgetItem(contenidos[us]))
            us += 1

    def llenarTabla(self,table,nombre,tCarpetas):

        table.clearContents()
        #contenidos=os.listdir(directorio_temporal)
        filaSeleccionada = tCarpetas.selectedItems()
        fila = filaSeleccionada[0].row()
        if nombre != 'admin':
           contenidosC= permiso.verificarPermisosUsuario(nombre)
        else:
           directorio = 'repositorio'
           contenidosC=os.listdir(directorio)

        usuario = contenidosC[fila]

        global carpSelect

        carpSelect = usuario
        print(carpSelect)
        directorio_temporal = 'repositorio/'+usuario+'/temporal'
        contenidos=os.listdir(directorio_temporal)
        us = 0
        for elemento in contenidos:
            table.setItem(us,0, QTableWidgetItem(contenidos[us]))
            us += 1
        #table.currentItemChanged.connect(self.seleccionar(table))

    def llenarTablaCarpCommit(self,table,nombre,tCarpetas):
        table.clearContents()
        #contenidos=os.listdir(directorio_temporal)
        filaSeleccionada = tCarpetas.selectedItems()
        fila = filaSeleccionada[0].row()
        directorio = 'repositorio/'+nombre+'/permanente'
        contenidosC=os.listdir(directorio) 
        global carpSelect
        global commitSelect
        commitSelect = contenidosC[fila]

        print(commitSelect)
        directorio_commit = 'repositorio/'+carpSelect+'/permanente/'+commitSelect
        contenidos=os.listdir(directorio_commit)
        us = 0
        for elemento in contenidos:
            table.setItem(us,0, QTableWidgetItem(contenidos[us]))
            us += 1
        #table.currentItemChanged.connect(self.seleccionar(table))
    def updateArchivo(self,table):   
        global carpSelect 
        global commitSelect   
        filaSeleccionada = table.selectedItems()
        directorio_temporal = 'repositorio/'+carpSelect+'/temporal'
        directorio_permanente = 'repositorio/'+carpSelect+'/permanente/'+commitSelect
        contenidos = os.listdir(directorio_permanente)
        try:
            fila = filaSeleccionada[0].row()
            elemento = contenidos[fila]
            print(elemento)
            directorio_permanente_or = 'repositorio/'+carpSelect+'/permanente/'+commitSelect+'/'+elemento
            print(directorio_permanente_or)
            src = os.path.join(directorio_permanente, elemento) # origen
            dst = os.path.join(directorio_temporal, elemento) # destino
            shutil.copy(src, dst)
            print("Correcto")
        except:
            print("Falló")
            print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")

    def update(self,table):
        self.eliminarArchivos(carpeta)
        table.clearContents()
        global carpSelect
        global commitSelect
        updateUltimo = log.login.verificaNumeroCommit(carpSelect)
        directorio_temporal = 'repositorio/'+carpSelect+'/temporal'
        directorio_permanente = 'repositorio/'+carpSelect+'/permanente/'+'commit'+str(updateUltimo)
        contenidos=os.listdir(directorio_permanente)
        self.eliminarArchivos(carpeta)
        for elemento in contenidos:
            try:
                print(f"Copiando {elemento} --> {directorio_temporal} ... ", end="")
                src = os.path.join(directorio_permanente, elemento) # origen
                dst = os.path.join(directorio_temporal, elemento) # destino
                shutil.copy(src, dst)
                print("Correcto")
            except:
                print("Falló")
                print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")

        nuevos = os.listdir(directorio_temporal)
        us = 0
        for elemento in nuevos:
            table.setItem(us,0, QTableWidgetItem(nuevos[us]))
            us += 1
        
    def eliminarFila(self,table,carpetas):   
        global carpSelect    
        filaSeleccionada = table.selectedItems()

        directorio_temporal = 'repositorio/'+carpSelect+'/temporal'
        contenidos = os.listdir(directorio_temporal)

        if filaSeleccionada:
            fila = filaSeleccionada[0].row()
            table.removeRow(fila)
            remove('repositorio/'+carpSelect+'/temporal/'+contenidos[fila])
            table.clearSelection()
        else:
            sms.MessageBox(QtWidgets.QWidget).show_message(1,'Error','Selecciones un archivo a eliminar')
    def crearCarpeta(self,directorio):
        try:
            os.mkdir(directorio)
        except OSError:
            print("La creación del directorio %s falló" % directorio)
        else:
            print("Se ha creado el directorio: %s " % directorio)
    def commit(self,nombre):
        directorio_temporal = 'repositorio/'+nombre+'/temporal'
        log.login.actualizarNumeroCommit(nombre)
        directorio_permanente = 'repositorio/'+nombre+'/permanente/commit'+str(log.login.verificaNumeroCommit(nombre))
        self.crearCarpeta(self,directorio_permanente)
        contenidos=os.listdir(directorio_temporal)
        for elemento in contenidos:
            try:
                print(f"Copiando {elemento} --> {directorio_permanente} ... ", end="")
                src = os.path.join(directorio_temporal, elemento) # origen
                dst = os.path.join(directorio_permanente, elemento) # destino
                shutil.copy(src, dst)
                print("Correcto")
            except:
                print("Falló")
                print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")
    def eliminarArchivos(self):   
        global carpSelect
        global commitSelect
        directorio_temporal = 'repositorio/'+carpSelect+'/temporal'
        contenidos = os.listdir(directorio_temporal)
        for elemento in contenidos:
            try:
                remove('repositorio/'+carpSelect+'/temporal/'+elemento)
            except:
                print("Falló recuperacion")
    def updateCommit(self):
        global carpSelect
        global commitSelect
        directorio_temporal = 'repositorio/'+carpSelect+'/temporal'
        directorio_permanente = 'repositorio/'+carpSelect+'/permanente/'+commitSelect
        contenidos=os.listdir(directorio_permanente)
        self.eliminarArchivos(carpeta)
        for elemento in contenidos:
            try:
                print(f"Copiando {elemento} --> {directorio_temporal} ... ", end="")
                src = os.path.join(directorio_permanente, elemento) # origen
                dst = os.path.join(directorio_temporal, elemento) # destino
                shutil.copy(src, dst)
                print("Correcto")
            except:
                print("Falló")
                print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")
    def cargarArchivo(nombre, direccion_origen,table):
        
        directorio_temporal = 'repositorio/'+nombre+'/temporal'
       
        try:
            shutil.copy(direccion_origen, directorio_temporal)
            contenidos = os.listdir(directorio_temporal)
            table.clearContents()
            us = 0
            for elemento in contenidos:
               table.setItem(us,0, QTableWidgetItem(contenidos[us]))
               us += 1
               print("Correcto")
        except:
            print("Falló")
            print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")