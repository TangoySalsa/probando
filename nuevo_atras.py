import sys
import os

from PyQt4 import  uic, QtGui, QtCore  # Import the PyQt4 module we'll need
from PyQt4.QtGui import *
import probando_atras

import datetime
from datetime import date

import time
from time import gmtime, strftime

import MySQLdb

from escposprinter import *

db_host = 'localhost'
db_user = 'root'
db_pass = 'pametequieromucho'
db_db = 'senorbowl'


#variables globales
lista_precios = {}
tipo_de_precios = []
items_de_tipo = []
adc_de_tipo = []
texto_factura = ''

cantidad_pb_nuevos = 10
cantidad_pb_item = 15
cantidad_pb_adc = 24
cantidad_cb_ingredientes = 12


main_dialog = uic.loadUiType("probando_atras.ui")[0]
#warnings.filterwarnings('error', category=MySQLdb.Warning)


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
        self.producto_pedido = {}
        self.adicional_pedido = []
        self.cantidad = []
        self.precio_lista = []
        self.descuentos = []
        self.forma_de_pago = ''
        self.comentario = ''
        self.forma_de_entrega = ''

    def clear(self):
        self.numero_factura = '0'
        self.item = []
        self.fecha_pedido = datetime.datetime.now()
        self.creado_pedido = False
        self.entregado_pedido = False
        self.pagado = False
        self.nombre_cliente = ''
        self.telefono_cliente = ''
        self.direccion_pedido = ''
        self.producto_pedido = {}
        self.adicional_pedido = []
        self.cantidad = []
        self.precio_lista = []
        self.descuentos = []
        self.forma_de_pago = ''
        self.comentario = ''
        self.forma_de_entrega = ''









class LoadingApp(QtGui.QMainWindow, probando_atras.Ui_MainWindow):
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


        self.PB_Nuevo.setText ('1 ' + tipo_de_precios[0])
        self.PB_Nuevo_2.setText('2 ' + tipo_de_precios[1])
        self.PB_Nuevo_3.setText('3 ' + tipo_de_precios[2])
        self.PB_Nuevo_4.setText('4 ' + tipo_de_precios[3])
        self.PB_Nuevo_5.setText('5 ' + tipo_de_precios[4])
        self.PB_Nuevo_6.setText('6 ' + tipo_de_precios[5])
        self.PB_Nuevo_7.setText('7 ' + tipo_de_precios[6])
        self.PB_Nuevo_8.setText('8 ' + tipo_de_precios[7])
        self.PB_Nuevo_9.setText('9 ' + tipo_de_precios[8])
        self.PB_Nuevo_10.setText('10 ' + tipo_de_precios[9])

        self.PB_Nuevo_click()
        self.previa_impresion()

        #self.PB_Nuevo.setFlat(True)
        #self.PB_Nuevo.setStyleSheet()
        #self.PB_Nuevo.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')

        self.PB_Nuevo.clicked.connect(self.PB_Nuevo_click)
        self.PB_Nuevo_2.clicked.connect(self.PB_Nuevo_2_click)
        self.PB_Nuevo_3.clicked.connect(self.PB_Nuevo_3_click)
        self.PB_Nuevo_4.clicked.connect(self.PB_Nuevo_4_click)
        self.PB_Nuevo_5.clicked.connect(self.PB_Nuevo_5_click)
        self.PB_Nuevo_6.clicked.connect(self.PB_Nuevo_6_click)
        self.PB_Nuevo_7.clicked.connect(self.PB_Nuevo_7_click)
        self.PB_Nuevo_8.clicked.connect(self.PB_Nuevo_8_click)
        self.PB_Nuevo_9.clicked.connect(self.PB_Nuevo_9_click)
        self.PB_Nuevo_10.clicked.connect(self.PB_Nuevo_10_click)


        self.PB_Item.clicked.connect(self.PB_Item_clickl)
        self.PB_Item_2.clicked.connect(self.PB_Item_2_clickl)
        self.PB_Item_3.clicked.connect(self.PB_Item_3_clickl)
        self.PB_Item_4.clicked.connect(self.PB_Item_4_clickl)
        self.PB_Item_5.clicked.connect(self.PB_Item_5_clickl)
        self.PB_Item_6.clicked.connect(self.PB_Item_6_clickl)
        self.PB_Item_7.clicked.connect(self.PB_Item_7_clickl)
        self.PB_Item_8.clicked.connect(self.PB_Item_8_clickl)
        self.PB_Item_9.clicked.connect(self.PB_Item_9_clickl)
        self.PB_Item_10.clicked.connect(self.PB_Item_10_clickl)
        self.PB_Item_11.clicked.connect(self.PB_Item_11_clickl)
        self.PB_Item_12.clicked.connect(self.PB_Item_12_clickl)
        self.PB_Item_13.clicked.connect(self.PB_Item_13_clickl)
        self.PB_Item_14.clicked.connect(self.PB_Item_14_clickl)


        self.PB_Adc.clicked.connect(self.PB_Adc_click)
        self.PB_Adc_2.clicked.connect(self.PB_Adc_2_click)
        self.PB_Adc_3.clicked.connect(self.PB_Adc_3_click)
        self.PB_Adc_4.clicked.connect(self.PB_Adc_4_click)
        self.PB_Adc_5.clicked.connect(self.PB_Adc_5_click)
        self.PB_Adc_6.clicked.connect(self.PB_Adc_6_click)
        self.PB_Adc_7.clicked.connect(self.PB_Adc_7_click)
        self.PB_Adc_8.clicked.connect(self.PB_Adc_8_click)
        self.PB_Adc_9.clicked.connect(self.PB_Adc_9_click)
        self.PB_Adc_10.clicked.connect(self.PB_Adc_10_click)
        self.PB_Adc_11.clicked.connect(self.PB_Adc_11_click)
        self.PB_Adc_12.clicked.connect(self.PB_Adc_12_click)
        self.PB_Adc_13.clicked.connect(self.PB_Adc_13_click)
        self.PB_Adc_14.clicked.connect(self.PB_Adc_14_click)
        self.PB_Adc_15.clicked.connect(self.PB_Adc_15_click)
        self.PB_Adc_16.clicked.connect(self.PB_Adc_16_click)
        self.PB_Adc_17.clicked.connect(self.PB_Adc_17_click)
        self.PB_Adc_18.clicked.connect(self.PB_Adc_18_click)
        self.PB_Adc_19.clicked.connect(self.PB_Adc_19_click)
        self.PB_Adc_20.clicked.connect(self.PB_Adc_20_click)
        self.PB_Adc_21.clicked.connect(self.PB_Adc_21_click)
        #self.PB_Adc_22.clicked.connect(self.PB_Adc_22_click)
        #self.PB_Adc_23.clicked.connect(self.PB_Adc_23_click)
        #self.PB_Adc_24.clicked.connect(self.PB_Adc_24_click)

        self.TE_Nombre.textChanged.connect(self.previa_impresion)
        self.TE_Telefono.textChanged.connect(self.previa_impresion)
        self.TE_Direccion.textChanged.connect(self.previa_impresion)
        self.TE_Uber.textChanged.connect(self.previa_impresion)
        self.TE_Comentario.textChanged.connect(self.previa_impresion)

        self.RB_Forma_pago.toggled.connect(self.previa_impresion)
        self.RB_Forma_pago_2.toggled.connect(self.previa_impresion)
        self.RB_Forma_pago_3.toggled.connect(self.previa_impresion)
        self.RB_Forma_pago_4.toggled.connect(self.previa_impresion)

        self.combo_box_entrega.addItem("Salon")
        self.combo_box_entrega.addItem("Terraza")
        self.combo_box_entrega.addItem("Para llevar")
        self.combo_box_entrega.addItem("Express")
        self.combo_box_entrega.addItem("Uber")

        self.combo_box_entrega.currentIndexChanged.connect(self.previa_impresion)

        self.listWidget_ticket.itemDoubleClicked.connect(self.dobleclick_ticket)


        #seteo de los botones de F

        self.PB_Imprimir.clicked.connect(self.imprimir_venta)
        self.PB_Limpiar.clicked.connect(self.limpiar_orden)

        self.PB_ultimo_cliente.clicked.connect(self.ultimo_cliente)
        self.PB_buscar.clicked.connect(self.buscar_cliente)




    def dobleclick_ticket(self):

        item_row = self.listWidget_ticket.currentRow()
        item_text = self.listWidget_ticket.currentItem().text()

        print item_row
        print item_text



    def PB_Nuevo_click(self):
        self.PB_Nuevo.setFlat(True)
        self.PB_Nuevo_2.setFlat(False)
        self.PB_Nuevo_3.setFlat(False)
        self.PB_Nuevo_4.setFlat(False)
        self.PB_Nuevo_5.setFlat(False)
        self.PB_Nuevo_6.setFlat(False)
        self.PB_Nuevo_7.setFlat(False)
        self.PB_Nuevo_8.setFlat(False)
        self.PB_Nuevo_9.setFlat(False)
        self.PB_Nuevo_10.setFlat(False)

        self.PB_tipo_precios(0)



    def PB_Nuevo_2_click(self):
        self.PB_Nuevo.setFlat(False)
        self.PB_Nuevo_2.setFlat(True)
        self.PB_Nuevo_3.setFlat(False)
        self.PB_Nuevo_4.setFlat(False)
        self.PB_Nuevo_5.setFlat(False)
        self.PB_Nuevo_6.setFlat(False)
        self.PB_Nuevo_7.setFlat(False)
        self.PB_Nuevo_8.setFlat(False)
        self.PB_Nuevo_9.setFlat(False)
        self.PB_Nuevo_10.setFlat(False)

        self.PB_tipo_precios(1)

    def PB_Nuevo_3_click(self):
        self.PB_Nuevo.setFlat(False)
        self.PB_Nuevo_2.setFlat(False)
        self.PB_Nuevo_3.setFlat(True)
        self.PB_Nuevo_4.setFlat(False)
        self.PB_Nuevo_5.setFlat(False)
        self.PB_Nuevo_6.setFlat(False)
        self.PB_Nuevo_7.setFlat(False)
        self.PB_Nuevo_8.setFlat(False)
        self.PB_Nuevo_9.setFlat(False)
        self.PB_Nuevo_10.setFlat(False)

        self.PB_tipo_precios(2)

    def PB_Nuevo_4_click(self):
        self.PB_Nuevo.setFlat(False)
        self.PB_Nuevo_2.setFlat(False)
        self.PB_Nuevo_3.setFlat(False)
        self.PB_Nuevo_4.setFlat(True)
        self.PB_Nuevo_5.setFlat(False)
        self.PB_Nuevo_6.setFlat(False)
        self.PB_Nuevo_7.setFlat(False)
        self.PB_Nuevo_8.setFlat(False)
        self.PB_Nuevo_9.setFlat(False)
        self.PB_Nuevo_10.setFlat(False)

        self.PB_tipo_precios(3)

    def PB_Nuevo_5_click(self):
        self.PB_Nuevo.setFlat(False)
        self.PB_Nuevo_2.setFlat(False)
        self.PB_Nuevo_3.setFlat(False)
        self.PB_Nuevo_4.setFlat(False)
        self.PB_Nuevo_5.setFlat(True)
        self.PB_Nuevo_6.setFlat(False)
        self.PB_Nuevo_7.setFlat(False)
        self.PB_Nuevo_8.setFlat(False)
        self.PB_Nuevo_9.setFlat(False)
        self.PB_Nuevo_10.setFlat(False)

        self.PB_tipo_precios(4)

    def PB_Nuevo_6_click(self):
        self.PB_Nuevo.setFlat(False)
        self.PB_Nuevo_2.setFlat(False)
        self.PB_Nuevo_3.setFlat(False)
        self.PB_Nuevo_4.setFlat(False)
        self.PB_Nuevo_5.setFlat(False)
        self.PB_Nuevo_6.setFlat(True)
        self.PB_Nuevo_7.setFlat(False)
        self.PB_Nuevo_8.setFlat(False)
        self.PB_Nuevo_9.setFlat(False)
        self.PB_Nuevo_10.setFlat(False)

        self.PB_tipo_precios(5)

    def PB_Nuevo_7_click(self):
        self.PB_Nuevo.setFlat(False)
        self.PB_Nuevo_2.setFlat(False)
        self.PB_Nuevo_3.setFlat(False)
        self.PB_Nuevo_4.setFlat(False)
        self.PB_Nuevo_5.setFlat(False)
        self.PB_Nuevo_6.setFlat(False)
        self.PB_Nuevo_7.setFlat(True)
        self.PB_Nuevo_8.setFlat(False)
        self.PB_Nuevo_9.setFlat(False)
        self.PB_Nuevo_10.setFlat(False)

        self.PB_tipo_precios(6)

    def PB_Nuevo_8_click(self):
        self.PB_Nuevo.setFlat(False)
        self.PB_Nuevo_2.setFlat(False)
        self.PB_Nuevo_3.setFlat(False)
        self.PB_Nuevo_4.setFlat(False)
        self.PB_Nuevo_5.setFlat(False)
        self.PB_Nuevo_6.setFlat(False)
        self.PB_Nuevo_7.setFlat(False)
        self.PB_Nuevo_8.setFlat(True)
        self.PB_Nuevo_9.setFlat(False)
        self.PB_Nuevo_10.setFlat(False)

        self.PB_tipo_precios(7)

    def PB_Nuevo_9_click(self):
        self.PB_Nuevo.setFlat(False)
        self.PB_Nuevo_2.setFlat(False)
        self.PB_Nuevo_3.setFlat(False)
        self.PB_Nuevo_4.setFlat(False)
        self.PB_Nuevo_5.setFlat(False)
        self.PB_Nuevo_6.setFlat(False)
        self.PB_Nuevo_7.setFlat(False)
        self.PB_Nuevo_8.setFlat(False)
        self.PB_Nuevo_9.setFlat(True)
        self.PB_Nuevo_10.setFlat(False)

        self.PB_tipo_precios(8)

    def PB_Nuevo_10_click(self):
        self.PB_Nuevo.setFlat(False)
        self.PB_Nuevo_2.setFlat(False)
        self.PB_Nuevo_3.setFlat(False)
        self.PB_Nuevo_4.setFlat(False)
        self.PB_Nuevo_5.setFlat(False)
        self.PB_Nuevo_6.setFlat(False)
        self.PB_Nuevo_7.setFlat(False)
        self.PB_Nuevo_8.setFlat(False)
        self.PB_Nuevo_9.setFlat(False)
        self.PB_Nuevo_10.setFlat(True)

        self.PB_tipo_precios(9)



    def PB_Item_clickl(self):

        if len(items_de_tipo[0]) > 0:
            if len(self.pedido.producto_pedido)<9:
                indice = '0' + str(len(self.pedido.producto_pedido) + 1) + ' ' + items_de_tipo[0]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[0]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_2_clickl(self):
        if len(items_de_tipo[1]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[1]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[1]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_3_clickl(self):
        if len(items_de_tipo[2]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[2]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[2]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_4_clickl(self):
        if len(items_de_tipo[3]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[3]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[3]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_5_clickl(self):
        if len(items_de_tipo[4]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[4]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[4]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_6_clickl(self):
        if len(items_de_tipo[5]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[5]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[5]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_7_clickl(self):
        if len(items_de_tipo[6]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[6]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[6]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_8_clickl(self):
        if len(items_de_tipo[7]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[7]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[7]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_9_clickl(self):
        if len(items_de_tipo[8]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[8]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[8]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_10_clickl(self):
        if len(items_de_tipo[9]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[9]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[9]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_11_clickl(self):
        if len(items_de_tipo[10]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[10]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[10]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_12_clickl(self):
        if len(items_de_tipo[11]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[11]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[11]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_13_clickl(self):
        if len(items_de_tipo[12]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[12]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[12]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()

    def PB_Item_14_clickl(self):
        if len(items_de_tipo[13]) > 0:
            if len(self.pedido.producto_pedido) < 9:
                indice = '0' + str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[13]
            else:
                indice = str(len(self.pedido.producto_pedido)+ 1) + ' ' + items_de_tipo[13]

            arreglo_item_nuevo = []
            self.pedido.producto_pedido[indice] = arreglo_item_nuevo
            self.previa_impresion()


    def Ultimo_indice(self):
        if bool(self.pedido.producto_pedido):
            items_en_el_pedido = []
            for bowls in self.pedido.producto_pedido:
                items_en_el_pedido.append(bowls)
            items_en_el_pedido.sort()
        return(items_en_el_pedido[len(items_en_el_pedido)-1])


    def PB_Adc_click(self):
        ind_adc = 0
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_2_click(self):
        ind_adc = 1
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_3_click(self):
        ind_adc = 2
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_4_click(self):
        ind_adc = 3
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_5_click(self):
        ind_adc = 4
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_6_click(self):
        ind_adc = 5
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_7_click(self):
        ind_adc = 6
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_8_click(self):
        ind_adc = 7
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_9_click(self):
        ind_adc = 8
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_10_click(self):
        ind_adc = 9
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_11_click(self):
        ind_adc = 10
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_12_click(self):
        ind_adc = 11
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_13_click(self):
        ind_adc = 12
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_14_click(self):
        ind_adc = 13
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_15_click(self):
        ind_adc = 14
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_16_click(self):
        ind_adc = 15
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_17_click(self):
        ind_adc = 16
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_18_click(self):
        ind_adc = 17
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_19_click(self):
        ind_adc = 18
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_20_click(self):
        ind_adc = 19
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    def PB_Adc_21_click(self):
        ind_adc = 20
        if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
            indice = self.Ultimo_indice()
            self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
            self.previa_impresion()
    # def PB_Adc_22_click(self):
    #     ind_adc = 21
    #     if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
    #         indice = self.Ultimo_indice()
    #         self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
    #         self.previa_impresion()
    # def PB_Adc_23_click(self):
    #     ind_adc = 22
    #     if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
    #         indice = self.Ultimo_indice()
    #         self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
    #         self.previa_impresion()
    # def PB_Adc_24_click(self):
    #     ind_adc = 23
    #     if len(adc_de_tipo[ind_adc]) > 0 and bool(self.pedido.producto_pedido):
    #         indice = self.Ultimo_indice()
    #         self.pedido.producto_pedido[indice].append(adc_de_tipo[ind_adc])
    #         self.previa_impresion()



    def limpiar_orden(self):

        self.TE_Nombre.setPlainText('')
        self.TE_Telefono.setPlainText('')
        self.TE_Direccion.setPlainText('')
        self.TE_Uber.setPlainText('')
        self.TE_Comentario.setPlainText('')

        self.pedido.clear()
        self.previa_impresion()




    def PB_tipo_precios(self, cual):
        tipo = tipo_de_precios[cual]
        # items_de_tipo = []
        # adc_de_tipo = []


        for i in range(0,len(items_de_tipo)):
            items_de_tipo.pop()

        for i in range(0,len(adc_de_tipo)):
            adc_de_tipo.pop()



        for cadauno in lista_precios:
            if lista_precios[cadauno][0] == tipo:

                if lista_precios[cadauno][1] == "adic":
                    adc_de_tipo.append(cadauno)
                else:
                    items_de_tipo.append(cadauno)


        cantidad_item_de_este_tipo = len(items_de_tipo)
        for i in range(cantidad_item_de_este_tipo,14,1):
            items_de_tipo.append("")

        cantidad_adicionales = len(adc_de_tipo)
        for i in range(cantidad_adicionales,24,1):
            adc_de_tipo.append("")


        self.PB_Item.setText(items_de_tipo[0])
        self.PB_Item_2.setText(items_de_tipo[1])
        self.PB_Item_3.setText(items_de_tipo[2])
        self.PB_Item_4.setText(items_de_tipo[3])
        self.PB_Item_5.setText(items_de_tipo[4])
        self.PB_Item_6.setText(items_de_tipo[5])
        self.PB_Item_7.setText(items_de_tipo[6])
        self.PB_Item_8.setText(items_de_tipo[7])
        self.PB_Item_9.setText(items_de_tipo[8])
        self.PB_Item_10.setText(items_de_tipo[9])
        self.PB_Item_11.setText(items_de_tipo[10])
        self.PB_Item_12.setText(items_de_tipo[11])
        self.PB_Item_13.setText(items_de_tipo[12])
        self.PB_Item_14.setText(items_de_tipo[13])


        self.PB_Adc.setText(adc_de_tipo[0])
        self.PB_Adc_2.setText(adc_de_tipo[1])
        self.PB_Adc_3.setText(adc_de_tipo[2])
        self.PB_Adc_4.setText(adc_de_tipo[3])
        self.PB_Adc_5.setText(adc_de_tipo[4])
        self.PB_Adc_6.setText(adc_de_tipo[5])
        self.PB_Adc_7.setText(adc_de_tipo[6])
        self.PB_Adc_8.setText(adc_de_tipo[7])
        self.PB_Adc_9.setText(adc_de_tipo[8])
        self.PB_Adc_10.setText(adc_de_tipo[9])
        self.PB_Adc_11.setText(adc_de_tipo[10])
        self.PB_Adc_12.setText(adc_de_tipo[11])
        self.PB_Adc_13.setText(adc_de_tipo[12])
        self.PB_Adc_14.setText(adc_de_tipo[13])
        self.PB_Adc_15.setText(adc_de_tipo[14])
        self.PB_Adc_16.setText(adc_de_tipo[15])
        self.PB_Adc_17.setText(adc_de_tipo[16])
        self.PB_Adc_18.setText(adc_de_tipo[17])
        self.PB_Adc_19.setText(adc_de_tipo[18])
        self.PB_Adc_20.setText(adc_de_tipo[19])
        self.PB_Adc_21.setText(adc_de_tipo[20])
        #self.PB_Adc_22.setText(adc_de_tipo[21])
        #self.PB_Adc_23.setText(adc_de_tipo[22])
        #self.PB_Adc_24.setText(adc_de_tipo[23])





    def imprimir_comandas(self):

        self.listWidget_comanda.clear()

        espacios = [' '] * 12
        renglon = 'FACTURA No: 1001-' + '{:08}'.format(int(self.pedido.numero_factura)) + ''.join(espacios)

        fecha = self.pedido.fecha_pedido.date()
        renglon += '{:02}'.format(fecha.day) + '-' + '{:02}'.format(fecha.month) + '-' + str(fecha.year)
        self.listWidget_comanda.addItem(renglon)

        if not self.combo_box_entrega.currentText() == "Uber":
            renglon_tipo_pago = 'Forma de pago : ' + str(self.pedido.forma_de_pago)
            self.listWidget_comanda.addItem(renglon_tipo_pago)

        separador = ['_'] * 48
        self.listWidget_comanda.addItem(''.join(separador))

        self.listWidget_comanda.addItem('')
        renglon = 'Cliente : ' + self.TE_Nombre.toPlainText()
        self.listWidget_comanda.addItem(renglon)
        renglon = 'Telefono: ' + self.TE_Telefono.toPlainText()
        self.listWidget_comanda.addItem(renglon)

        if self.combo_box_entrega.currentText() == "Salon":
            renglon = 'Salon'
            self.listWidget_comanda.addItem(renglon)

        if self.combo_box_entrega.currentText() == "Para llevar":
            renglon = 'Para llevar en empaque de material 100% vegetal - 100% compostable.'
            self.listWidget_comanda.addItem(renglon)

        if self.combo_box_entrega.currentText() == "Terraza":
            renglon = 'Entregar en la terraza'
            self.listWidget_comanda.addItem(renglon)

        if self.combo_box_entrega.currentText() == "Express":
            renglon = 'Direccion : ' + self.TE_Direccion.toPlainText()
            self.listWidget_comanda.addItem(renglon)

        if self.combo_box_entrega.currentText() == "Uber":
            renglon = 'Codigo UberEATS : ' + self.TE_Uber.toPlainText()
            self.listWidget_comanda.addItem(renglon)

        self.pedido.comentario = ''
        if len(self.TE_Comentario.toPlainText()) > 0:
            self.listWidget_comanda.addItem('')
            renglon = 'Comentario : ' + self.TE_Comentario.toPlainText()
            self.listWidget_comanda.addItem(renglon)
            self.pedido.comentario = self.TE_Comentario.toPlainText()

        separador = ['_'] * 48
        self.listWidget_comanda.addItem(''.join(separador))
        self.listWidget_comanda.addItem('')


        items_en_el_pedido = []
        for bowls in self.pedido.producto_pedido:
            items_en_el_pedido.append(bowls)
        items_en_el_pedido.sort()

        for i in range(0, len(items_en_el_pedido)):

            renglon = items_en_el_pedido[i][0:2]
            nombre_item = items_en_el_pedido[i][3:len(items_en_el_pedido[i])]
            renglon = renglon + '. ' + lista_precios[nombre_item][4]
            self.listWidget_comanda.addItem(renglon)

            for x in range(0, len(self.pedido.producto_pedido[items_en_el_pedido[i]])):
                renglon = "    " + lista_precios[self.pedido.producto_pedido[items_en_el_pedido[i]][x]][4]

                if len(renglon) < 48:
                    espacios = [' '] * (48 - len(renglon))
                    renglon = renglon + ''.join(espacios)
                else:
                    self.listWidget_comanda.addItem(renglon)
                    espacios = [' '] * 48
                    renglon = ''.join(espacios)

                self.listWidget_comanda.addItem(renglon)

            self.listWidget_comanda.addItem('')


        # Epson = printer.Usb(0x0fe6, 0x811e,0,0x81,0x02)
        # a = 0
        Epson = printer.Usb(0x0fe6, 0x811e, 0, 0x81, 0x02)
        #Epson = printer.Usb(0x04b8, 0x0e15)

        Epson.set(codepage='cp1251', bold=True, align='center', size='normal')
        Epson.image('/share/SB-negro-2.png')
        Epson.set(codepage=None, bold=True, align='center')
        Epson.text('\n')
        Epson.set(codepage=None, align='left', bold=True)

        Epson.set(codepage='cp1251', bold=False, align='left', size='normal')

        for i in range(0, self.listWidget_comanda.count()):
            # print self.listWidget_ticket.item(i).text()
            texto = str(self.listWidget_comanda.item(i).text()) + '\n'
            Epson.text(texto)

        Epson.cut()


    def imprimir_venta(self):
        self.cargar_numero_facturo()
        self.previa_impresion()
        self.salvar_pedido()

        self.previa_impresion()

        if self.CB_Imprimir_Comandas.isChecked():
            self.imprimir_comandas()
        self.imprimir_ticket()

        self.limpiar_orden()


    def ultimo_cliente(self):

        sql = "SELECT * FROM pedido ORDER BY fecha_pedido DESC LIMIT 1"

        db = MySQLdb.connect(host=db_host,  # your host, usually localhost
                             user=db_user,  # your username
                             passwd=db_pass,  # your password
                             db=db_db)  # name of the data base
        cur = db.cursor()
        cur.execute(sql)
        registro = cur.fetchall()

        db.close()

        self.TE_Nombre.setPlainText(registro[0][6])
        self.TE_Telefono.setPlainText(registro[0][7])
        self.TE_Direccion.setPlainText(registro[0][8])

    def buscar_cliente(self):
        # self.buscar_tel()

        sql = "SELECT * FROM pedido Where telefono_cliente ='"

        sql += str(self.TE_Telefono.toPlainText())
        sql += "'"

        db = MySQLdb.connect(host=db_host,  # your host, usually localhost
                             user=db_user,  # your username
                             passwd=db_pass,  # your password
                             db=db_db)  # name of the data base
        cur = db.cursor()
        cur.execute(sql)
        registro = cur.fetchall()
        db.close()

        #cantidad_registros = len(registro) - 1
        self.TE_Nombre.setPlainText(registro[0][6])
        # self.text_telefono.setText(registro[0][7])
        self.TE_Direccion.setPlainText(registro[0][8])

    def keyPressEvent(self, event):


        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F2:
            self.imprimir_venta()

        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F3:
            self.imprimir_comandas()


        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F4:
            self.limpiar_orden()

        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F8:
            self.ultimo_cliente()

        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_F10:
            self.buscar_cliente()

        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Delete:
            item_row = self.listWidget_ticket.currentRow()
            item_text = self.listWidget_ticket.currentItem().text()

            print item_row
            print item_text

        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_1: self.PB_Nuevo_click()

        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_2: self.PB_Nuevo_2_click()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_3: self.PB_Nuevo_3_click()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_4: self.PB_Nuevo_4_click()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_5: self.PB_Nuevo_5_click()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_6: self.PB_Nuevo_6_click()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_7: self.PB_Nuevo_7_click()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_8: self.PB_Nuevo_8_click()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_9: self.PB_Nuevo_9_click()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_0: self.PB_Nuevo_10_click()

    def corregir_tel(self):

        tel = str(self.TE_Telefono.toPlainText())
        if len(tel) >0:
            if not tel[0] == "+":
                if len(tel) == 8 and tel.isdigit():
                    nuevo = tel[0:4] + '-' + tel[4:8]
                    self.TE_Telefono.setPlainText(nuevo)
                else:
                    if len(tel) == 9 and not (tel[4:5] == "-"):
                        nuevo = tel[0:4] + '-' + tel[5:9]
                        self.TE_Telefono.setPlainText(nuevo)



    def previa_impresion(self):

        #chequeo si estoy haciendo algun descuento.
        #en caso de algun descuento, agregar a la OR el checkbox correspondiente

 #       any_promo = False
 #       if self.checkBox_promo_lanz.checkState() or self.checkBox_promo_3x2.checkState():

        self.corregir_tel()

        any_promo = False

        #self.fecha_entrega.setDateTime(datetime.datetime.now())

        self.listWidget_ticket.clear()

        espacios = [' '] * 12
        renglon = 'FACTURA No: 1001-' + '{:08}'.format(int(self.pedido.numero_factura)) + ''.join(espacios)


        fecha = self.pedido.fecha_pedido.date()
        renglon += '{:02}'.format(fecha.day) + '-' + '{:02}'.format(fecha.month) + '-' + str(fecha.year)
        self.listWidget_ticket.addItem(renglon)


        if self.RB_Forma_pago.isChecked():
            self.pedido.forma_de_pago = "Efectivo"

        if self.RB_Forma_pago_2.isChecked():
            self.pedido.forma_de_pago = "Tarjeta"

        if self.RB_Forma_pago_3.isChecked():
            self.pedido.forma_de_pago = "Transferencia"

        if self.RB_Forma_pago_4.isChecked():
            self.pedido.forma_de_pago = "Cortesia"

        if not self.combo_box_entrega.currentText() == "Uber":
            renglon_tipo_pago = 'Forma de pago : ' + str(self.pedido.forma_de_pago)
            self.listWidget_ticket.addItem(renglon_tipo_pago)
        else:
            self.pedido.forma_de_pago = "Transferencia"


        con_cuanto = self.TE_Efectivo.toPlainText()
        if self.RB_Forma_pago.isChecked() and len(con_cuanto) > 0:
            self.listWidget_ticket.addItem('')

            renglon_con_cuanto = 'Canecla con : ' + con_cuanto
            self.listWidget_ticket.addItem(renglon_con_cuanto)


        separador = ['_'] * 48
        self.listWidget_ticket.addItem(''.join(separador))
        #self.listWidget_ticket.addItem('')

        #Seccion con los datos del cliente

        self.listWidget_ticket.addItem('')
        renglon = 'Cliente : ' + self.TE_Nombre.toPlainText()
        self.listWidget_ticket.addItem(renglon)
        renglon = 'Telefono: ' + self.TE_Telefono.toPlainText()
        self.listWidget_ticket.addItem(renglon)


        if self.combo_box_entrega.currentText() == "Salon":
            renglon = 'Salon'
            self.listWidget_ticket.addItem(renglon)

        if self.combo_box_entrega.currentText() == "Para llevar":
            renglon = 'Para llevar en empaque de material 100% vegetal - 100% compostable.'
            self.listWidget_ticket.addItem(renglon)

        if self.combo_box_entrega.currentText() == "Terraza":
            renglon = 'Entregar en la terraza'
            self.listWidget_ticket.addItem(renglon)

        if self.combo_box_entrega.currentText() == "Express":
            renglon = 'Direccion : ' + self.TE_Direccion.toPlainText()
            self.listWidget_ticket.addItem(renglon)

        if self.combo_box_entrega.currentText() == "Uber":
            renglon = 'Codigo UberEATS : ' + self.TE_Uber.toPlainText()
            self.listWidget_ticket.addItem(renglon)

        self.pedido.comentario = ''
        if len(self.TE_Comentario.toPlainText()) > 0:
            self.listWidget_ticket.addItem('')
            renglon = 'Comentario : ' + self.TE_Comentario.toPlainText()
            self.listWidget_ticket.addItem(renglon)
            self.pedido.comentario = self.TE_Comentario.toPlainText()

        separador = ['_'] * 48
        self.listWidget_ticket.addItem(''.join(separador))
        self.listWidget_ticket.addItem('')

        subotal = 0
        descuento = 0

#parte pedido
#parte pedido
#parte pedido


        items_en_el_pedido = []
        for bowls in self.pedido.producto_pedido:
            items_en_el_pedido.append(bowls)
        items_en_el_pedido.sort()


        for i in range(0,len(items_en_el_pedido)):

            renglon = items_en_el_pedido[i][0:2]
            nombre_item = items_en_el_pedido[i][3:len(items_en_el_pedido[i])]
            renglon = renglon + '. ' + lista_precios[nombre_item][4]
            self.listWidget_ticket.addItem(renglon)

            valor = "{0:,}".format(float(lista_precios[nombre_item][2]))
            renglon = '    Item @ ' + valor
            espacios = [' '] * (48 - len(renglon) - len(valor))
            renglon = renglon +  ''.join(espacios) + valor
            self.listWidget_ticket.addItem(renglon)

            suma_bowl = float(lista_precios[nombre_item][2])

            for x in range(0, len(self.pedido.producto_pedido[items_en_el_pedido[i]])):
                suma_bowl = suma_bowl + float(lista_precios[self.pedido.producto_pedido[items_en_el_pedido[i]][x]][2])

                renglon = "    " + lista_precios[self.pedido.producto_pedido[items_en_el_pedido[i]][x]][4]
                valor_adc = "{0:,}".format(float(lista_precios[self.pedido.producto_pedido[items_en_el_pedido[i]][x]][2]))


                if len(renglon) + len(valor_adc) < 48:
                    espacios = [' '] * (48 - len(renglon) - len(valor_adc))
                    renglon = renglon + ''.join(espacios) + valor_adc
                else:
                    self.listWidget_ticket.addItem(renglon)
                    espacios = [' '] * (48  - len(valor_adc))
                    renglon = ''.join(espacios) + valor_adc

                self.listWidget_ticket.addItem(renglon)


            subotal = subotal + suma_bowl

            self.listWidget_ticket.addItem('')



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
            self.TE_Total.setText(valor)
        else:
            total_cuenta = subotal  # - descuento
            valor = "{0:,}".format(float(total_cuenta))
            self.TE_Total.setText(valor)

        #self.text_total_items.setText(str(len(self.pedido.item)))
        #self.text_total_items.setAlignment(QtCore.Qt.AlignCenter)
        #self.text_total.setAlignment(QtCore.Qt.AlignRight)


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

        Epson = printer.Usb(0x0fe6, 0x811e,0,0x81,0x02)
        #Epson = printer.Usb(0x04b8, 0x0e15)

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


    def cargar_numero_facturo(self):

        db = MySQLdb.connect(host=db_host,  # your host, usually localhost
                             user=db_user,  # your username
                             passwd=db_pass,  # your password
                             db=db_db)  # name of the data base
        cur = db.cursor()

        sql = "SELECT * FROM pedido ORDER BY numero_factura DESC LIMIT 1"
        cur.execute(sql)
        registro = cur.fetchall()
        #self.pedido.numero_factura = str(int(registro[0][0]) + 1)
        self.pedido.numero_factura = str(int(registro[0][0]) + 1)

    def salvar_pedido(self):

        db = MySQLdb.connect(host=db_host,  # your host, usually localhost
                             user=db_user,  # your username
                             passwd=db_pass,  # your password
                             db=db_db)  # name of the data base
        cur = db.cursor()

        #sql = "SELECT * FROM pedido ORDER BY fecha_pedido DESC LIMIT 1"
        #cur.execute(sql)
        #registro = cur.fetchall()

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
        col += 'promo,'
        col += 'forma_de_pago,'
        col += 'comentario,'
        col += 'como_se_entrega,'
        col += 'quien_entrega'

        #self.pedido.numero_factura = str(int(registro[0][0]) + 1)

        fecha = "'" + str(self.pedido.fecha_pedido.date())

        hora = strftime(" %H:%M:%S", time.localtime()) + "'"

        items_en_el_pedido = []
        for bowls in self.pedido.producto_pedido:
            items_en_el_pedido.append(bowls)
        items_en_el_pedido.sort()

        for i in range(0, len(items_en_el_pedido)):

            numero_item = int(items_en_el_pedido[i][0:2])
            nombre_item = items_en_el_pedido[i][3:len(items_en_el_pedido[i])]
            suma_bowl = float(lista_precios[nombre_item][2])

            producto_adicional = ''

            for x in range(0, len(self.pedido.producto_pedido[items_en_el_pedido[i]])):
                suma_bowl = suma_bowl + float(lista_precios[self.pedido.producto_pedido[items_en_el_pedido[i]][x]][2])
                producto_adicional += "+" + self.pedido.producto_pedido[items_en_el_pedido[i]][x]

            #registro = "'" + self.pedido.numero_factura  + "',"
            registro = ",'" + str(numero_item) + "',"
            registro += fecha + hora + ',' + fecha + hora + ',' + fecha + hora + ','
            #registro += "'', '',"
            registro += "'0'" + ","

            registro += "'" + str(self.TE_Nombre.toPlainText())  + "',"
            registro += "'" + str(self.TE_Telefono.toPlainText()) + "',"
            registro += "'" + str(self.TE_Direccion.toPlainText()) + "',"
            registro += "'" + str(nombre_item) + "',"
            registro += "'" + str(producto_adicional) + "',"
            registro += "1" + ','

            registro += str(suma_bowl) + ','
            registro += str(suma_bowl) + ','

            #promo
            registro += "'',"

            registro += "'" + str(self.pedido.forma_de_pago) + "',"
            registro += "'" + str(self.pedido.comentario) + "',"

            if self.combo_box_entrega.currentText() == "Salon": registro += "'salon',"
            if self.combo_box_entrega.currentText() == "Para llevar": registro += "'llevar',"
            if self.combo_box_entrega.currentText() == "Terraza": registro += "'terraza',"
            if self.combo_box_entrega.currentText() == "Express": registro += "'express',"
            if self.combo_box_entrega.currentText() == "Uber": registro += "'uber',"

            #quien_entrega
            registro += "''"

            sql = "INSERT INTO pedido (" + col + ") VALUES (" +  "'" + str(self.pedido.numero_factura) + "'" + registro + ")"

            try:
                cur.execute(sql)
            except:
                self.pedido.numero_factura = int(self.pedido.numero_factura) + 1
                sql = "INSERT INTO pedido (" + col + ") VALUES (" + "'" + str(self.pedido.numero_factura) + "'" + registro + ")"
                cur.execute(sql)




            db.commit()

            cwd = os.getcwd()
            archivo_control = cwd + "/control.csv"
            f = open(archivo_control, 'a+')
            f.write(registro + '\r')
            f.close()


        db.close()


def main():


    db = MySQLdb.connect(host=db_host,  # your host, usually localhost
                         user=db_user,  # your username
                         passwd=db_pass,  # your password
                         db=db_db)  # name of the data base
    cur = db.cursor()

    #sql = "select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='pedido'"
    sql = "select * from precios"
    cur.execute(sql)
    for row in cur.fetchall():
        precio_nuevo = []

        precio_nuevo.append(row[3]) #Categoria
        precio_nuevo.append(row[2]) #Tipo
        precio_nuevo.append(row[4]) #precio_lista
        precio_nuevo.append(row[5]) #precio_descuento
        precio_nuevo.append(row[6]) #descripcion_producto

        lista_precios[row[0]] = precio_nuevo

        if not row[3] in tipo_de_precios:
            tipo_de_precios.append(row[3])
            #print row[3]


    #print len(tipo_de_precios)
    for i in range(len(tipo_de_precios),cantidad_pb_nuevos):
        tipo_de_precios.append("")


    db.close()


    global app
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = LoadingApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app

if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
