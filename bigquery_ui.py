from PyQt4.QtGui import *
from PyQt4 import QtGui
import google_api
__author__ = 'z.liu'


class bigquery_panel(QtGui.QWidget):
    def __init__(self,project_text):
        super(bigquery_panel, self).__init__()
        self.table_text = QtGui.QLineEdit()
        self.sql_text = QtGui.QLineEdit()
        self.show_all_btn = QtGui.QPushButton("&Show all")
        self.search_btn = QtGui.QPushButton("&search")
        self._bq_interface = google_api.bq_interface(project_text)
        self.result_table = QtGui.QTableWidget()
        self.mainframe_width = 800
        self.mainframe_height = 600
        self.button_width = 90
        self.button_height =20
        self.package_len = 87500
        self.result_table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.__init_ui()

    def bigquery_init(self):
        self.search_btn.clicked.connect(self.search)
        self.show_all_btn.clicked.connect(self.showall)
        main_layout = QtGui.QGridLayout()
        btn_layout = QtGui.QGridLayout()
        main_layout.addLayout(btn_layout, 0, 0)
        main_layout.addWidget(QtGui.QLabel("Result table:"))
        main_layout.addWidget(self.result_table,2, 0)
        btn_layout.addWidget(self.sql_text, 0, 0)
        btn_layout.addWidget(self.search_btn, 0, 1)
        btn_layout.addWidget(self.show_all_btn, 1, 0)
        return main_layout

    def __init_ui(self):
        self.port_text = QtGui.QLineEdit()
        self.address_text = QtGui.QLineEdit()
        self.username_text = QtGui.QLineEdit()
        self.pwd_text = QtGui.QLineEdit()
        self.pwd_text.setEchoMode(QLineEdit.Password)
        mainlayout = QtGui.QGridLayout()
        mainlayout.addLayout(self.bigquery_init(),1, 0)

        self.setLayout(mainlayout)
        self.setWindowTitle("Bigquery control Panel")
        self.resize(self.mainframe_width,self.mainframe_height)

    def set_projectid(self, project_id):
        self._bq_interface.set_projectid(project_id)

    def search(self):
        return 0

    def insert_data_2_table(self,start,end):
        data = self._bq_interface.get_userdate(start,end)
        if self.head_init_flag == False:
            self.__init_header(data)
            self.head_init_flag == True
        i = 1
        for row in data['rows']:
            j = 0
            for field in row['f']:
                self.result_table.setItem(i, j, QTableWidgetItem(field['v']))
                j += 1
            i += 1
        return len( data['rows'])

    def pull_data(self):
        done_len = 0
        recordlen = self._bq_interface.getcustomer_num()
        #self.result_table.setRowCount(recordlen);
        #self.result_table.setColumnCount(len(data['schema']['fields']))
        self.head_init_flag = False
        while done_len < recordlen:
            end = recordlen
            if end - done_len > self.package_len:
               end = self.package_len + done_len
            done_len += self.insert_data_2_table(done_len,end)

    def showall(self):
        self.pull_data()

    def __init_header(self,data):
        i = 0
        for row in data['schema']['fields']:
                self.result_table.setItem(0,i, QTableWidgetItem(row['name']))
                i += 1