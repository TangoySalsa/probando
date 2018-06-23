# -*- coding: utf-8 -*-
import MySQLdb

from PyQt4 import  uic, QtGui, QtCore  # Import the PyQt4 module we'll need

from PyQt4.QtGui import *

from escposprinter import *

import sys  # We need sys so that we can pass argv to QApplication
import senor_bowl_gui_2  # This file holds our MainWindow and all design related things
#import prueba


import datetime
from datetime import date

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods

import time
from time import gmtime, strftime


lista_precios = {}
texto_factura = ''


#ultimo_numero_factura = 0

cwd = os.getcwd()
ini_file = cwd + '/senor_bowl.ini'
if not os.path.isfile(ini_file) :
    f = open(ini_file , 'w')
    f.close()

arch_pedido = cwd + '/pedido.tmp'
if not os.path.isfile(arch_pedido) :
    f = open(arch_pedido , 'w')
    f.close()




class pedidos():
    def __init__(self):
        self.numero_factura = ''
        self.item = []
        self.fecha_pedido = datetime.datetime.now()
        self.creado_pedido = False
        self.entregado_pedido = False
        self.pagado  = False
        self.nombre_cliente = ''
        self.telefono_cliente = ''
        self.direccion_pedido = ''
        self.producto_pedido = []
        self.adicional_pedido = []
        self.cantidad = []
        self.precio_lista = []
        self.descuentos = []
        self.forma_de_pago = ''
        self.comentario = ''

    def clear(self):
        self.numero_factura = ''
        self.item = []
        self.fecha_pedido = datetime.datetime.now()
        self.creado_pedido = False
        self.entregado_pedido = False
        self.pagado = False
        self.nombre_cliente = ''
        self.telefono_cliente = ''
        self.direccion_pedido = ''
        self.producto_pedido = []
        self.adicional_pedido = []
        self.cantidad = []
        self.precio_lista = []
        self.descuentos = []
        self.forma_de_pago = ''
        self.comentario = ''

main_dialog = uic.loadUiType("senor_bowl_gui_2.ui")[0]

class LoadingApp(QtGui.QMainWindow, senor_bowl_gui_2.Ui_MainWindow):
    pedido = pedidos()
    pedido.clear()

    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined


        #sql = "SELECT * FROM pedido ORDER BY numero_factura DESC LIMIT 1"

        sql = "SELECT * FROM pedido ORDER BY fecha_pedido DESC LIMIT 1"

        db = MySQLdb.connect(host='localhost',  # your host, usually localhost
                             user="root",  # your username
                             passwd="Success2018",  # your password
                             db="senorbowl")  # name of the data base
        cur = db.cursor()
        cur.execute(sql)
        registro = cur.fetchall()

        self.text_numero_pedido.setText(str(int(registro[0][0]) + 1))



        self.cargar_pedido()


        self.calendarWidget.hide()
        self.calendarWidget.clicked[QtCore.QDate].connect(self.setear_fecha)
        self.fecha_entrega.setDateTime(datetime.datetime.now())


        self.combo_forma_pago.addItem("Efectivo")
        self.combo_forma_pago.addItem("Tarjeta")
        self.combo_forma_pago.addItem("Trasnferencia")

        self.text_Nombre.textChanged.connect(self.cargar_pedido)
        self.text_telefono.textChanged.connect(self.cargar_pedido)

        #self.text_trabaja.textChanged.connect(self.cargar_pedido)
        self.text_entrega.textChanged.connect(self.cargar_pedido)
        self.text_comentario.textChanged.connect(self.cargar_pedido)

        self.combo_forma_pago.currentIndexChanged.connect(self.cargar_pedido)



        self.pb_para_hoy.clicked.connect(self.fecha_hoy)
        self.pb_para_manana.clicked.connect(self.fecha_manana)

        tipos = []
        for t in lista_precios['tipo']:
            if t not in tipos: tipos.append(t)

        for tipo in tipos:

            renglon = 'Tipo : ' + tipo
            espacios1 = [' '] * (30 - len(renglon))
            self.listWidget_menu.addItem(renglon + ''.join(espacios1) + '|')

            Columnas = ["Nombre Producto",'Precio Lista','Promocion']

            espacios1 = [' '] * (30 - len(Columnas[0]))
            espacios2 = [' '] * (17 - len(Columnas[1]))
            espacios3 = [' '] * (12 - len(Columnas[2]))

            renglon = Columnas[0] + ''.join(espacios1) + '|' + ''.join(espacios2) + Columnas[1] + ''.join(espacios3) +  Columnas[2]
            self.listWidget_menu.addItem(renglon)

            espacios1 = [' '] * 30
            espacios2 = [' '] * 29
            self.listWidget_menu.addItem(''.join(espacios1) + '|'+ ''.join(espacios2))


            for nombre in lista_precios['nombre_producto']:
                indice = lista_precios['nombre_producto'].index(nombre)

                if lista_precios['tipo'][indice] == tipo:
                    valor1 = "{0:,}".format(float(lista_precios['precio_lista'][indice]))
                    valor2 = "{0:,}".format(float(lista_precios['precio_descuento'][indice]))

                    if valor2 == valor1: valor2 = ''

                    espacios1 = [' '] * (30 - len(nombre))
                    espacios2 = [' '] * (17 - len(valor1))
                    espacios3 = [' '] * (12 - len(valor2))

                    renglon = nombre + ''.join(espacios1) +'|'+  ''.join(espacios2) +  valor1 + ''.join(espacios3)  + valor2
                    self.listWidget_menu.addItem(renglon)

            espacios1 = [' '] * 30
            espacios2 = [' '] * 29
            self.listWidget_menu.addItem(''.join(espacios1) + '|' + ''.join(espacios2))

        #self.listWidget_ticket.addItem('123456789012345678901234567890123456789012345678')

        self.listWidget_menu.itemDoubleClicked.connect(self.dobleclick_menu)

        self.listWidget_ticket.itemDoubleClicked.connect(self.dobleclick_ticket)

    def RepresentsInt(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def dobleclick_menu(self):

        nombre = str(self.listWidget_menu.currentItem().text())
        nombre = nombre[0:nombre.find(' ',0,len(nombre))]

        if nombre in lista_precios['nombre_producto']:
            indice = lista_precios['nombre_producto'].index(nombre)

            cantidad_items = len(self.pedido.item)
            self.pedido.item.append(cantidad_items + 1)

            self.pedido.producto_pedido.append(nombre)
            self.pedido.cantidad.append(1)
            self.pedido.precio_lista.append(float(lista_precios['precio_lista'][indice]))
            self.pedido.descuentos.append(float(lista_precios['precio_descuento'][indice]))
            self.pedido.adicional_pedido.append('')

            self.previa_impresion()

            #self.listWidget_ticket.addItem(lista_precios['descripcion_producto'][indice])
            #valor1 = "{0:,}".format(float(lista_precios['precio_lista'][indice]))
            #renglon = '1     @ '  + valor1
            #espacios1 = [' '] * (48 - len(valor1)- len(renglon))
            #self.listWidget_ticket.addItem(renglon + ''.join(espacios1) + valor1)


    def dobleclick_ticket(self):

        item_row = self.listWidget_ticket.currentRow()
        item_text = self.listWidget_ticket.currentItem().text()

        if item_text[0:1] == ' ': item_row += -1
        item_texto = self.listWidget_ticket.item(item_row).text()
        valor_item = int(item_texto[0:1]) - 1

        if self.radioButton.isChecked(): self.pedido.adicional_pedido[valor_item] = 'adc_pollo'
        if self.radioButton_2.isChecked(): self.pedido.adicional_pedido[valor_item] = 'adc_trucha'
        if self.radioButton_3.isChecked() : self.pedido.adicional_pedido[valor_item] = 'adc_camaron'

        print item_texto

    def cargar_pedido(self):


        """
        Campos del Pedido

        numero_factura
        item
        fecha_pedido
        creado_pedido
        entregado_pedido
        pagado
        nombre_cliente
        telefono_cliente
        direccion_pedido
        producto_pedido
        adicional_pedido
        cantidad
        precio_lista
        descuento
        forma_de_pago
        """

        self.corregir_tel()

        #self.pedido.numero_factura = ultimo_numero_factura
        self.pedido.fecha_pedido = self.fecha_entrega.dateTime()
        self.pedido.nombre_cliente = self.text_Nombre.toPlainText()
        self.pedido.telefono_cliente = self.text_telefono.toPlainText()
        self.pedido.direccion_pedido = self.text_entrega.toPlainText()
        self.pedido.comentario = self.text_comentario.toPlainText()

        if self.combo_forma_pago.currentText() == "Efectivo":
            self.pedido.forma_de_pago = 'efectivo'
        if self.combo_forma_pago.currentText() == "Tarjeta":
            self.pedido.forma_de_pago = 'tarjeta'
        if self.combo_forma_pago.currentText() == "Trasnferencia":
            self.pedido.forma_de_pago = 'transfer'

       # sql = "SELECT * FROM pedido ORDER BY numero_factura DESC LIMIT 1"

        #db = MySQLdb.connect(host='localhost',  # your host, usually localhost
        #                     user="root",  # your username
        #                     passwd="Success2018",  # your password
        #                     db="senorbowl")  # name of the data base
        #cur = db.cursor()
        #cur.execute(sql)
        #registro = cur.fetchall()
        self.pedido.numero_factura = int(   self.text_numero_pedido.toPlainText())

        #self.text_numero_pedido.setText(str(self.pedido.numero_factura))

        self.previa_impresion()



    def previa_impresion(self):

        #chequeo si estoy haciendo algun descuento.
        #en caso de algun descuento, agregar a la OR el checkbox correspondiente

        any_promo = False

        if self.checkBox_promo_lanz.checkState() or self.checkBox_promo_3x2.checkState():
            any_promo = True

        self.fecha_entrega.setDateTime(datetime.datetime.now())

        self.listWidget_ticket.clear()

        espacios = [' '] * 12
        renglon = 'FACTURA No: 1001-' + '{:08}'.format(int(self.text_numero_pedido.toPlainText())) + ''.join(espacios)
        fecha = self.pedido.fecha_pedido.date().toPyDate()
        renglon += '{:02}'.format(fecha.day) + '-' + '{:02}'.format(fecha.month) + '-' + str(fecha.year)
        self.listWidget_ticket.addItem(renglon)


        renglon_tipo_pago = 'Forma de pago : ' + str(self.combo_forma_pago.currentText())
        self.listWidget_ticket.addItem(renglon_tipo_pago)


        separador = ['_'] * 48
        self.listWidget_ticket.addItem(''.join(separador))
        #self.listWidget_ticket.addItem('')

        #Seccion con los datos del cliente

        self.listWidget_ticket.addItem('')
        renglon = 'Cliente : ' + self.text_Nombre.toPlainText()
        self.listWidget_ticket.addItem(renglon)
        renglon = 'Telefono: ' + self.text_telefono.toPlainText()
        self.listWidget_ticket.addItem(renglon)
        #renglon = 'Entregar : ' + self.text_trabaja.toPlainText()
        #self.listWidget_ticket.addItem(renglon)
        renglon = 'Direccion : ' + self.text_entrega.toPlainText()
        self.listWidget_ticket.addItem(renglon)

        if len(self.text_comentario.toPlainText()) > 0:
            self.listWidget_ticket.addItem('')
            renglon = 'Comentario : ' + self.text_comentario.toPlainText()
            self.listWidget_ticket.addItem(renglon)

        separador = ['_'] * 48
        self.listWidget_ticket.addItem(''.join(separador))
        self.listWidget_ticket.addItem('')


        #seteando el precio
        for i in range(0, len(self.pedido.item)):
            indice = lista_precios['nombre_producto'].index(self.pedido.producto_pedido[i])
            if self.checkBox_promo_lanz.checkState():
                self.pedido.precio_lista[i] = float(lista_precios['precio_lista'][indice])
                self.pedido.descuentos[i] = float(lista_precios['precio_descuento'][indice])
            else:
                self.pedido.precio_lista[i] = float(lista_precios['precio_lista'][indice])
                self.pedido.descuentos[i] = float(lista_precios['precio_lista'][indice])


        subotal = 0
        descuento = 0


        if self.checkBox_promo_3x2.checkState():
            cantidad_pedidos = 0
            for i in range(0, len(self.pedido.item)):
                indice = lista_precios['nombre_producto'].index(self.pedido.producto_pedido[i])

                if lista_precios['tipo'][indice] == 'bowl':
                    cantidad_pedidos +=1

            promo = cantidad_pedidos/3

            lista_promo = []
            item = 0
            for p in range(0,promo):
                valor_minimo = 0
                for i in range(0, len(self.pedido.item)):
                    indice = lista_precios['nombre_producto'].index(self.pedido.producto_pedido[i])
                    precio = float(lista_precios['precio_lista'][indice])

                    if (valor_minimo == 0 or valor_minimo > precio) and (not i in lista_promo):
                        valor_minimo = precio
                        item = i

                lista_promo.append(item)
                descuento += float(self.pedido.precio_lista[item])
                self.pedido.descuentos[item] = 0


        for i in range(0, len(self.pedido.item)):

            indice = lista_precios['nombre_producto'].index(self.pedido.producto_pedido[i])

            renglon = str(self.pedido.item[i]) + '. ' + lista_precios['descripcion_producto'][indice]
            self.listWidget_ticket.addItem(renglon)
            # self.listWidget_ticket.addItem(lista_precios['descripcion_producto'][indice])
            valor1 = "{0:,}".format(float(lista_precios['precio_lista'][indice]))
            renglon = '   ' + str(self.pedido.cantidad[i]) + '  @ ' + valor1

            subotal += int(self.pedido.cantidad[i]) * float(lista_precios['precio_lista'][indice])
            if not self.checkBox_promo_3x2.checkState():
                descuento += int(self.pedido.cantidad[i]) * (
                    float(lista_precios['precio_lista'][indice]) - float(lista_precios['precio_descuento'][indice]))

            espacios1 = [' '] * (48 - len(valor1) - len(renglon))
            self.listWidget_ticket.addItem(renglon + ''.join(espacios1) + valor1)

            if len(self.pedido.adicional_pedido[i]) > 0:
                indice_adc = lista_precios['nombre_producto'].index(self.pedido.adicional_pedido[i])
                renglon = '   + ' + lista_precios['descripcion_producto'][indice_adc]
                valor1 = "{0:,}".format(float(lista_precios['precio_lista'][indice_adc]))

                subotal += float(lista_precios['precio_lista'][indice_adc])
                espacios1 = [' '] * (48 - len(renglon) - len(valor1))
                self.listWidget_ticket.addItem(renglon + ''.join(espacios1) + valor1)





        separador = ['_'] * 48
        self.listWidget_ticket.addItem(''.join(separador))
        self.listWidget_ticket.addItem('')

        renglon_subtotal = '                         SUBTOTAL'
        valor = "{0:,}".format(subotal)
        espacios = [' '] * (48 - len(renglon_subtotal) - len(valor))
        self.listWidget_ticket.addItem(renglon_subtotal + ''.join(espacios) + valor)

        if any_promo:
            self.listWidget_ticket.addItem('')
            renglon_descuento = '                        DESCUENTO'
            valor = "{0:,}".format(descuento)
            espacios = [' '] * (48 - len(renglon_descuento) - len(valor))
            self.listWidget_ticket.addItem(renglon_descuento + ''.join(espacios) + valor)


        espacios = [' '] * 35
        subrayado = ['_'] * 13
        self.listWidget_ticket.addItem(''.join(espacios) + ''.join(subrayado) )
        self.listWidget_ticket.addItem('')
        self.listWidget_ticket.addItem('                 IMP. DE SERVICIO         0.00')
        self.listWidget_ticket.addItem('')
        self.listWidget_ticket.addItem('                    IMP. DE VENTA         0.00')
        self.listWidget_ticket.addItem(''.join(espacios) + ''.join(subrayado))
        self.listWidget_ticket.addItem('')

        if any_promo:
            total_cuenta = subotal - descuento
            valor = "{0:,}".format(float(total_cuenta))
            self.text_total.setText(valor)
        else:
            total_cuenta = subotal  # - descuento
            valor = "{0:,}".format(float(total_cuenta))
            self.text_total.setText(valor)

        self.text_total_items.setText(str(len(self.pedido.item)))
        self.text_total_items.setAlignment(QtCore.Qt.AlignCenter)
        self.text_total.setAlignment(QtCore.Qt.AlignRight)


        renglon_total = '                            TOTAL'
        valor = "{0:,}".format(total_cuenta)
        espacios = [' '] * (48 - len(renglon_total) - len(valor))
        self.listWidget_ticket.addItem(renglon_total + ''.join(espacios) + valor)

        self.listWidget_ticket.addItem('')
        self.listWidget_ticket.addItem('')
        self.listWidget_ticket.addItem('')

        renglon_centrado = 'MUCHAS GRACIAS POR SU COMPRA'
        cantidad_espacios = 48 - len(renglon_centrado)
        if (cantidad_espacios % 2 == 0):  # even
            cantidad_espacios = cantidad_espacios/2
        else:  # odd
            cantidad_espacios = (cantidad_espacios-1) / 2

        espacios = [' '] * cantidad_espacios
        renglon_centrado = ''.join(espacios) + renglon_centrado
        self.listWidget_ticket.addItem(renglon_centrado)
        self.listWidget_ticket.addItem('')

        renglon = 'Cuenta BAC Col.: 932361280'
        self.listWidget_ticket.addItem(renglon)
        renglon = 'SIMPE BAC Col.: 10200009323612807'
        self.listWidget_ticket.addItem(renglon)

        self.listWidget_ticket.addItem('')
        renglon_emitida = 'Emitida conforme a lo establecido en el regimen'
        self.listWidget_ticket.addItem(renglon_emitida)
        renglon_emitida = '   de tributacion simplificada de Costa Rica'
        self.listWidget_ticket.addItem(renglon_emitida)



    def imprimir_ticket(self):

        #Epson = printer.Usb(0x0fe6, 0x811e,0,0x81,0x02)

	Epson = printer.Usb(0x04b8, 0x0e15)

        Epson.set(codepage='cp1251', bold=True, align='center', size='normal')
        Epson.image('/share/SB-negro-2.png')
        Epson.set(codepage=None, bold=True, align='center')
        Epson.text('\n')
        Epson.text('SENOR BOWL LIMITADA\n')
        Epson.text('SANTA ANA - COSTA RICA\n')
        Epson.text('CED. JURIDICA: 3-102-741654\n')
        Epson.text('WhatsApp: 8455-2191 \n')
        Epson.text('Facebook: /senorbowl\n')
        Epson.text('\n')
        Epson.set(codepage=None, align='left', bold=True)


        Epson.set(codepage='cp1251', bold=False, align='left', size='normal')

        for i in range(0,self.listWidget_ticket.count()):
            #print self.listWidget_ticket.item(i).text()
            texto = str(self.listWidget_ticket.item(i).text()) + '\n'
            Epson.text(texto)

        Epson.cut()


    def limpiar_venta(self):
        self.pedido.clear()

        self.fecha_entrega.setDateTime(datetime.datetime.now())

        self.pedido.fecha_pedido = self.fecha_entrega.dateTime()
        self.text_Nombre.setText('')
        self.text_telefono.setText('')
        #self.text_trabaja.setText('')
        self.text_entrega.setText('')
        self.text_comentario.setText('')

        #sql = "SELECT * FROM pedido ORDER BY numero_factura DESC LIMIT 1"
        sql = "SELECT * FROM pedido ORDER BY fecha_pedido DESC LIMIT 1"

        db = MySQLdb.connect(host='localhost',  # your host, usually localhost
                             user="root",  # your username
                             passwd="Success2018",  # your password
                             db="senorbowl")  # name of the data base
        cur = db.cursor()
        cur.execute(sql)
        registro = cur.fetchall()

        self.text_numero_pedido.setText(str(int(registro[0][0]) + 1))



    def salvar_venta(self):

        db = MySQLdb.connect(host='localhost',  # your host, usually localhost
                             user="root",  # your username
                             passwd="Success2018",  # your password
                             db="senorbowl")  # name of the data base
        cur = db.cursor()

        col = 'numero_factura,'
        col += 'item,'
        col += 'fecha_pedido,'
        col += 'creado_pedido,'
        col += 'entregado_pedido,'
        col += 'pagado,'
        col += 'nombre_cliente,'
        col += 'telefono_cliente,'
        col += 'direccion_pedido,'
        col += 'producto_pedido,'
        col += 'adicional_pedido,'
        col += 'cantidad,'
        col += 'precio_lista,'
        col += 'descuento,'
        col += 'forma_de_pago,'
        col += 'comentario'

        fecha = "'" + str(self.pedido.fecha_pedido.date().toPyDate())

        hora = strftime(" %H:%M:%S", time.localtime()) + "'"

        for i in range(0, len(self.pedido.item)):
            registro = ''

            registro = "'" + str(self.pedido.numero_factura) + "',"
            registro += "'" + str(self.pedido.item[i]) + "',"
            registro += fecha + hora + ','
            registro += "'', '',"
            registro += str(self.pedido.pagado) + ","
            registro += "'" + str(self.pedido.nombre_cliente) + "',"
            registro += "'" + str(self.pedido.telefono_cliente) + "',"
            registro += "'" + str(self.pedido.direccion_pedido) + "',"
            registro += "'" + str(self.pedido.producto_pedido[i]) + "',"
            registro += "'" + str(self.pedido.adicional_pedido[i]) + "',"
            registro += str(self.pedido.cantidad[i]) + ','
            registro += str(self.pedido.precio_lista[i]) + ','
            registro += str(self.pedido.descuentos[i]) + ','
            registro += "'" + str(self.pedido.forma_de_pago) + "',"
            registro += "'" + str(self.pedido.comentario) + "'"

            sql = "INSERT IGNORE INTO pedido (" + col + ") VALUES (" + registro + ")"

            cur.execute(sql)
            db.commit()
        db.close()

    def setear_fecha(self):
        fecha = datetime.datetime.now()
        #a = self.calendarWidget.

        print a
        #self.fecha_entrega.setDateTime()

    def fecha_hoy(self):
        self.fecha_entrega.setDateTime(datetime.datetime.now())
        #Epson.text(str(date.today()))

    def fecha_manana(self):
        manana = datetime.datetime.now() + datetime.timedelta(days=1)
        self.fecha_entrega.setDateTime(manana)



    def corregir_tel(self):
        self.pedido.telefono_cliente = self.text_telefono.toPlainText()

        tel = str(self.pedido.telefono_cliente)
        if len(self.pedido.telefono_cliente) == 8 and tel.isdigit():
            nuevo = self.pedido.telefono_cliente[0:4] + '-' + self.pedido.telefono_cliente[4:8]
            self.pedido.telefono_cliente = nuevo
            self.text_telefono.setText(nuevo)
            print nuevo

        else:
            if len(self.pedido.telefono_cliente) == 9 and not (self.pedido.telefono_cliente[4:5] == "-"):
                nuevo = self.pedido.telefono_cliente[0:4] + '-' + self.pedido.telefono_cliente[5:9]
                self.pedido.telefono_cliente = nuevo
                self.text_telefono.setText(nuevo)
                print nuevo

    def buscar_tel(self):
        tel = str(self.pedido.telefono_cliente)
        db = MySQLdb.connect(host='localhost',  # your host, usually localhost
                             user="root",  # your username
                             passwd="Success2018",  # your password
                             db="senorbowl")  # name of the data base
        cur = db.cursor()

        sql = "select * from pedido where telefono_cliente = " + tel
        cur.execute(sql)

        db.close()

    def keyPressEvent(self, event):


        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Right:
            #self.listWidget_menu.setCurrentRow(40)
            self.dobleclick_menu()


        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Left:

            nombre = str(self.listWidget_menu.currentItem().text())
            nombre = nombre[0:nombre.find(' ', 0, len(nombre))]

            if nombre in self.pedido.producto_pedido:
                indice = lista_precios['nombre_producto'].index(nombre)
                self.pedido.item.pop()
                self.pedido.producto_pedido.remove(nombre)
                self.pedido.cantidad.pop()
                self.pedido.precio_lista.remove(float(lista_precios['precio_lista'][indice]))
                self.pedido.descuentos.remove(float(lista_precios['precio_descuento'][indice]))
                self.pedido.adicional_pedido.pop()
                self.previa_impresion()
                self.previa_impresion()





        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F2:
            self.imprimir_ticket()
            self.salvar_venta()
            self.limpiar_venta()

        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F3:
            self.salvar_venta()

        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F4:
            self.limpiar_venta()

        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F5:

            items = []
            for index in xrange(self.listWidget.count()):
                items.append(self.listWidget.item(index).text())

            for item in items:
                print item

        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Delete:

            item_ticket = str(self.listWidget_ticket.currentItem().text())
            item_row = self.listWidget_ticket.currentRow()
            if item_ticket[0] == ' ' :
                self.listWidget_ticket.setCurrentRow(item_row - 1)
            item_ticket = str(self.listWidget_ticket.currentItem().text())


            w = QWidget()
            result = QMessageBox.question(w, 'Seguro?', "Desea eleminiar " + item_ticket + "de la orden?", QMessageBox.Yes | QMessageBox.No,
                                          QMessageBox.No)
            if result == QMessageBox.Yes:
                #self.listWidget_ticket.removeItemWidget(self.listWidget_ticket.currentItem())

                descripcion = item_ticket[item_ticket.find('.', 0, len(item_ticket))+1:len(item_ticket)].strip()
                indice = lista_precios['descripcion_producto'].index(descripcion)    #self.pedido.producto_pedido[i])
                nombre = lista_precios['nombre_producto'][indice]

                cantidad_items = len(self.pedido.item) - 1
                self.pedido.item.pop()
                self.pedido.producto_pedido.remove(nombre)
                self.pedido.cantidad.pop()
                self.pedido.precio_lista.remove(float(lista_precios['precio_lista'][indice]))
                self.pedido.descuentos.remove(float(lista_precios['precio_descuento'][indice]))
                self.pedido.adicional_pedido.pop()
                self.previa_impresion()
                self.previa_impresion()

            else:
                a = 0

        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F8:

            sql = "SELECT * FROM pedido ORDER BY fecha_pedido DESC LIMIT 1"

            db = MySQLdb.connect(host='localhost',  # your host, usually localhost
                                 user="root",  # your username
                                 passwd="Success2018",  # your password
                                 db="senorbowl")  # name of the data base
            cur = db.cursor()
            cur.execute(sql)
            registro = cur.fetchall()

            self.text_Nombre.setText(registro[0][6])
            self.text_telefono.setText(registro[0][7])
            self.text_entrega.setText(registro[0][8])


        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F10:

            #self.buscar_tel()

            sql = "SELECT * FROM pedido Where telefono_cliente ='"

            sql += str(self.text_telefono.toPlainText())
            sql += "'"

            db = MySQLdb.connect(host='localhost',  # your host, usually localhost
                                 user="root",  # your username
                                 passwd="Success2018",  # your password
                                 db="senorbowl")  # name of the data base
            cur = db.cursor()
            cur.execute(sql)
            registro = cur.fetchall()

            cantidad_registros = len(registro) - 1
            self.text_Nombre.setText(registro[cantidad_registros][6])
            #self.text_telefono.setText(registro[0][7])
            self.text_entrega.setText(registro[cantidad_registros][8])

#        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F12:

#            comando = 'sudo pt-table-sync --execute h=127.0.0.1,u=root,p=pametequieromucho,D=senorbowl,t=pedido h=192.168.86.57,u=root,p=pametequieromucho'
#            os.system(comando)



def Imprimir_ticket_completo(self):

        items = []
        for index in xrange(self.listWidget.count()):
            items.append(self.listWidget.item(index).text())


        Epson = printer.Usb(0x04b8, 0x0e15)
        Epson.set(codepage='cp1251', bold=True, align='center', size='normal')
        Epson.image('/share/SB-negro.png')

        Epson.set(codepage=None, align='center', bold=True)
        Epson.text('\n')
        Epson.text('SENOR BOWL LIMITADA\n')
        Epson.text('CED. JURIDICA: 3-102-741654\n')
        Epson.text('TELEFONO: 8455-2191\n')
        Epson.set(codepage=None, bold=False)
        Epson.text('________________________________________________\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(codepage=None, align='left', bold=True)
        Epson.text('Cliente : ')
        Epson.set(codepage=None, bold=False)
        Epson.text('Javier\n')
        Epson.text('\n')

        #Epson.set(codepage=None, align='left', bold=True)
        #Epson.text('Pedido : ')
        #Epson.set(codepage=None, bold=False)
        #Epson.text('Sushi Bowl de Trucha Ahumada\n')
        #Epson.text('\n')

        Epson.set(codepage=None, align='left', bold=True)
        Epson.text('Telefono : ')
        Epson.set(codepage=None, bold=False)
        Epson.text('+54911 4401 9493\n')
        Epson.text('\n')

        Epson.set(codepage=None, align='left', bold=True)
        Epson.text('Direccion : ')
        Epson.set(codepage=None, bold=False)
        Epson.text('Emerson - Multipark\n')

        for item in items:
            Epson.text(str(item) +'\n')


        #Epson.text('________________________________________________\n')




        Epson.cut()


def main():
    db = MySQLdb.connect(host='localhost',  # your host, usually localhost
                         user="root",  # your username
                         passwd="Success2018",  # your password
                         db="senorbowl")  # name of the data base
    cur = db.cursor()

    sql = "select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='pedido'"
    cur.execute(sql)

    col = ''
    for row in cur.fetchall():
        col += row[3] + ','
    col = col[0:len(col) - 1]
    columnas = col.split(',')


    os.system('python /share/query.py precios')

    archivo_salida = '/share/salida.csv'
    salida = open(archivo_salida, 'r')
    archivo_precios = salida.readlines()
    salida.close()

    indice_columnas = {}
    primer_linea = archivo_precios[0][0:len(archivo_precios[0])-1]
    lista_columnas = primer_linea.split(',')

    db.close()


    for col in lista_columnas:
        lista_precios[col] = []
        indice_columnas[col] = lista_columnas.index(col)

    for i in range(1, len(archivo_precios)):
        linea = archivo_precios[i][0:len(archivo_precios[i])-1]
        row = linea.split(',')

        if not row[indice_columnas['nombre_producto']] in lista_precios['nombre_producto']:

            lista_precios['nombre_producto'].append(row[indice_columnas['nombre_producto']])
            lista_precios['descripcion_producto'].append(row[indice_columnas['descripcion_producto']])
            lista_precios['tipo'].append(row[indice_columnas['tipo']])

            lista_precios['precio_lista'].append(row[indice_columnas['precio_lista']])
            lista_precios['precio_descuento'].append(row[indice_columnas['precio_descuento']])


        else:

            indice = lista_precios['nombre_producto'].index(row[indice_columnas['nombre_producto']])
            lista_precios['precio_lista'][indice] = row[indice_columnas['precio_lista']]
            lista_precios['precio_descuento'][indice] = row[indice_columnas['precio_descuento']]

    global app
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = LoadingApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
