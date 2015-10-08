import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui, uic, QtCore
import google_api
import bigquery_ui

__author__ = 'z.liu'
#! /usr/bin/env python
# -*- coding: utf-8 -*-

mainframe_width = 500
mainframe_height = 400
button_width = 90
button_height =20

project_id_def = "pialab-rdmp"

class main_frame(QtGui.QWidget):
    def __init__(self, parent=None):
        super(main_frame, self).__init__()
        self.bigquery_panel = bigquery_ui.bigquery_panel("")
        self.table_text = QtGui.QLineEdit()
        self.project_text = QtGui.QLineEdit(project_id_def)
        self.username_text = QtGui.QLineEdit()
        self.pwd_text = QtGui.QLineEdit()
        self.pwd_text.setEchoMode(QLineEdit.Password)
        self.mysql_connect_btn = QtGui.QPushButton("&Connect to Mysql")
        self.bq_connect_btn = QtGui.QPushButton("&Connect to bigquery")
        self.mysql_connect_btn.clicked.connect(self.msql_connect)
        self.bq_connect_btn.clicked.connect(self.bq_connect)
        self.port_text = QtGui.QLineEdit()
        self.address_text = QtGui.QLineEdit()
        self.username_text = QtGui.QLineEdit()
        self.pwd_text = QtGui.QLineEdit()
        self.pwd_text.setEchoMode(QLineEdit.Password)
        self.__init_ui()


    def bigquery_init(self):

        bigquery_layout = QtGui.QGridLayout()
        bigquery_layout.addWidget(QtGui.QLabel("project id::"), 1, 0)
        bigquery_layout.addWidget(QtGui.QLabel("Table name:"),2, 0)
        bigquery_layout.addWidget(self.project_text,1, 1)
        bigquery_layout.addWidget(self.table_text, 2,1)
        bigquery_layout.addWidget(self.bq_connect_btn,3,1)
        return bigquery_layout

    def mysql_panel_init(self):

        mysqlLayout = QtGui.QGridLayout()
        mysqlLayout.addWidget(QtGui.QLabel("Address:"), 1, 0)
        mysqlLayout.addWidget(QtGui.QLabel("Port:"),2, 0)
        mysqlLayout.addWidget(QtGui.QLabel("User Name:"), 1, 2)
        mysqlLayout.addWidget(QtGui.QLabel("Password:"), 2, 2)


        mysqlLayout.addWidget(self.address_text, 1, 1)
        mysqlLayout.addWidget(self.port_text, 2, 1)
        mysqlLayout.addWidget(self.username_text, 1, 3)
        mysqlLayout.addWidget(self.pwd_text, 2, 3)
        mysqlLayout.addWidget(self.mysql_connect_btn, 3, 1)
        return mysqlLayout

    def __init_ui(self):
        mainLayout = QtGui.QGridLayout()
        mysqlLayout = self.mysql_panel_init()
        bigquery_layout = self.bigquery_init()
        mainLayout.addWidget(QtGui.QLabel("MySql Setting:"), 0, 0)
        mainLayout.addLayout(mysqlLayout, 1, 0)
        mainLayout.addWidget(QtGui.QLabel("BigQuery Setting:"), 2, 0)
        mainLayout.addLayout(bigquery_layout, 3, 0)
        self.setLayout(mainLayout)
        self.setWindowTitle("Setting Panel")
        self.show()
    def msql_connect(self):
        return 0
    def bq_connect(self):
        self.bigquery_panel.set_projectid(self.project_text.text())
        self.bigquery_panel.show()
        return 0

def main():
    app = QtGui.QApplication(sys.argv)
    ex = main_frame()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()