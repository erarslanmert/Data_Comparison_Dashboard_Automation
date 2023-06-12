from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QTableView, QFrame, QVBoxLayout, QComboBox, QMainWindow, QStyleFactory, \
    QAbstractItemView, QFileDialog, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sqlite3
import os
import sys
from PyQt5.QtWidgets import QApplication
from openpyxl import Workbook


coordinates_db = []
response = ()
weapon_coordinates = []
sensor_num = []
sensor_posts = []
sensor_names = []
sensor_positions = []
unit_names = []



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 960)
        self.tableWidget = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget.setGeometry(QtCore.QRect(5, 40, 1240, 900))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(5, 5, 1240, 21))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        file_filter = 'Text File (*.db)'
        response = QFileDialog.getOpenFileName(
            parent=None,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Database Files (*.db)',
        )
        print(response)

        self.list_db_tables(response[0])
        
    def list_db_tables(self,database_name):
        global coordinates_db, sensor_num
        table_list = []
        # Open connection to the database
        conn = sqlite3.connect(database_name)
        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        # Execute a query to get the list of tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        # Fetch the results of the query
        tables = cursor.fetchall()
        # Print the table names
        for table in tables:
            table_list.append(table[0])
        # Create a QSqlDatabase object to connect to the database
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(database_name)
        # Create a QSqlTableModel to represent the data from the database table
        model = QSqlTableModel()
        model.setTable(table_list[0])
        model.setEditStrategy(QSqlTableModel.OnFieldChange)  # Set the edit strategy
        # Set the model for the table view
        table_view = QTableView(self.tableWidget)
        table_view.setGeometry(0, 0,1240, 900)
        table_view.setModel(model)
        table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.comboBox.addItems(table_list)  # Replace with your actual table names
        model.setTable(table_list[0])
        model.select()
        self.comboBox.currentIndexChanged.connect(lambda: change_combo())
        def change_combo():
            model.setTable(self.comboBox.currentText())
            model.select()
        # Close the connection to the database

        self.comboBox.setCurrentIndex(1)

        cursor.execute("SELECT * FROM detection")
        rows = cursor.fetchall()

        # Create Excel workbook and sheet
        wb = Workbook()
        ws = wb.active

        # Write data to Excel sheet
        for row in rows:
            ws.append(row)

        # Save Excel file
        wb.save('mission_analyses.xlsx')

        # read data from SQL table into a pandas dataframe
        df = pd.read_sql_query("SELECT time, leveldb FROM detection WHERE sensorid ='125894713' ", conn)

        # plot line graph
        plt.plot(df['time'], df['leveldb'])
        plt.scatter(df['time'], df['leveldb'])
        plt.xlabel('time')
        plt.ylabel('level')
        plt.title('Filtered Data Line Graph')

        # show the plot
        plt.show()

        # Close database connection
        conn.close()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SQL viewer"))



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
