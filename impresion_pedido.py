import sys

import datetime
from datetime import date

import time
from time import gmtime, strftime

import MySQLdb

from escposprinter import *


db_host = 'localhost'
db_user = 'root'
db_pass = 'Success2018'
db_db = 'senorbowl'


lista_precios = {}

db = MySQLdb.connect(host=db_host,  # your host, usually localhost
                     user=db_user,  # your username
                     passwd=db_pass,  # your password
                     db=db_db)  # name of the data base
cur = db.cursor()

# sql = "select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='pedido'"
sql = "select * from precios"
cur.execute(sql)
for row in cur.fetchall():
    precio_nuevo = []

    precio_nuevo.append(row[3])  # Categoria
    precio_nuevo.append(row[2])  # Tipo
    precio_nuevo.append(row[4])  # precio_lista
    precio_nuevo.append(row[5])  # precio_descuento
    precio_nuevo.append(row[6])  # descripcion_producto

    lista_precios[row[0]] = precio_nuevo


archivo_pedido = '/share/pedido.csv'


pedido = open(archivo_pedido, 'r')
datos_archivo = pedido.readlines()
pedido.close()

# Epson = printer.Usb(0x0fe6, 0x811e,0,0x81,0x02)
# a = 0
Epson = printer.Usb(0x04b8, 0x0e15)



suma = 0
bowls = 1
for lineas in datos_archivo:

    #if bowls < 3:

    if not bowls % 2 == 0 :
        Epson.set(codepage='cp1251', bold=True, align='center', size='normal')
        Epson.text('\n')
        Epson.image('/share/SB-negro-2.png')
        Epson.set(codepage=None, bold=True, align='center')
        Epson.text('SENOR BOWL LIMITADA\n')
        Epson.text('SANTA ANA - COSTA RICA\n')
        Epson.text('CED. JURIDICA: 3-102-741654\n')
        Epson.text('WhatsApp: 8455-2191 \n')
        Epson.text('Facebook: /senorbowl\n')



       # Epson.text('\n')

    Epson.text('\n')
    #Epson.set(codepage=None, align='left', bold=True)

    separado = lineas.split(',')
    Epson.set(codepage='cp1251', bold=False, align='left', size='normal')
    subrayado = ['_'] * 48
    Epson.text(''.join(subrayado) + '\n')
    Epson.text('\n')
    Epson.text('Pedido de : ' + separado[0]+ '\n')
    Epson.text('\n')
    Epson.text(lista_precios[separado[1]][4] + '\n')

    for i in range(2,len(separado)-1):
        if len(separado[i]) >0:
            if len(separado[i])>0 and (separado[i] in lista_precios):
                Epson.text('     ' + lista_precios[separado[i]][4] + '\n')
            else:
                Epson.text('     ' + separado[i] + '\n')

    if bowls % 2 == 0 :
        Epson.text('\n')
        Epson.text(''.join(subrayado) + '\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.cut()

    bowls += 1

Epson.text('\n')
Epson.cut()

