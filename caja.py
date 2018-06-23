import sys

from PyQt4 import  uic, QtGui, QtCore  # Import the PyQt4 module we'll need
from PyQt4.QtGui import *
import caja_gui

import datetime
from datetime import date

import time
from time import gmtime, strftime

import MySQLdb


#db_host = 'localhost'
db_host = '192.168.0.10'
db_user = 'root'
#db_pass = 'Success2018'
db_pass = 'pametequieromucho'
db_db = 'senorbowl'


main_dialog = uic.loadUiType("caja.ui")[0]

ultimo_registro = []

class LoadingApp(QtGui.QMainWindow, caja_gui.Ui_MainWindow):

    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined

        self.pushButton_GO.clicked.connect(self.pushButton_GO_click)

        self.TE_Billete.setPlainText('0')
        self.TE_Billete_2.setPlainText('0')
        self.TE_Billete_3.setPlainText('0')
        self.TE_Billete_4.setPlainText('0')
        self.TE_Billete_5.setPlainText('0')

        self.TE_Moneda.setPlainText('0')
        self.TE_Moneda_2.setPlainText('0')
        self.TE_Moneda_3.setPlainText('0')
        self.TE_Moneda_4.setPlainText('0')
        self.TE_Moneda_5.setPlainText('0')
        self.TE_Moneda_6.setPlainText('0')

        self.TE_Datafono.setPlainText('0')
        self.TE_Datafono_2.setPlainText('0')
        self.TE_Datafono_3.setPlainText('0')
        self.TE_Datafono_4.setPlainText('0')

        self.TE_Provedores.setPlainText('0')


    def pushButton_GO_click(self):



        fecha = "'" + str(datetime.datetime.now())
        hora = strftime(" %H:%M:%S", time.localtime()) + "'"


        sql = "INSERT IGNORE INTO caja (fecha,20mil,10mil,5mil,2mil,1mil,500moneda,100moneda,50moneda,25moneda,10moneda,5moneda"

        sql += ",datafono_express_1,datafono_express_2,datafono_express_3,datafono_salon_1"

        sql += ",uber,pago_proveedores,pago_motos)"

        sql += "VALUES (" + fecha + hora + str(self.TE_Billete.toPlainText())
        sql += "," + str(self.TE_Billete_2.toPlainText())
        sql += "," + str(self.TE_Billete_3.toPlainText())
        sql += "," + str(self.TE_Billete_4.toPlainText())
        sql += "," + str(self.TE_Billete_5.toPlainText())

        sql += "," + str(self.TE_Moneda.toPlainText())
        sql += "," + str(self.TE_Moneda_2.toPlainText())
        sql += "," + str(self.TE_Moneda_3.toPlainText())
        sql += "," + str(self.TE_Moneda_4.toPlainText())
        sql += "," + str(self.TE_Moneda_5.toPlainText())
        sql += "," + str(self.TE_Moneda_6.toPlainText())

        sql += "," + str(self.TE_Datafono.toPlainText())
        sql += "," + str(self.TE_Datafono_2.toPlainText())
        sql += "," + str(self.TE_Datafono_3.toPlainText())
        sql += "," + str(self.TE_Datafono_4.toPlainText())

        sql += ",0," + str(self.TE_Provedores.toPlainText()) + ",0)"


        print sql

        db = MySQLdb.connect(host=db_host,  # your host, usually localhost
                             user=db_user,  # your username
                             passwd=db_pass,  # your password
                             db=db_db)  # name of the data base
        cur = db.cursor()

        cur.execute(sql)
        db.commit()
        db.close()


def main():


    db = MySQLdb.connect(host=db_host,  # your host, usually localhost
                         user=db_user,  # your username
                         passwd=db_pass,  # your password
                         db=db_db)  # name of the data base
    cur = db.cursor()

    # sql = "select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='pedido'"
    sql = "select * from caja ORDER BY fecha DESC LIMIT  1 "

    cur.execute(sql)
    for row in cur.fetchall():
        print row

    db.close()

    global app
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = LoadingApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app

if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
