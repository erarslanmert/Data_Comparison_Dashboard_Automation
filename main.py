import json
import math
from math import radians, cos, sin, atan2, sqrt
import pygeodesy
from PyQt5 import QtCore, QtGui, QtWidgets
import folium, io
from PyQt5 import QtWebEngineWidgets
from folium.plugins import MousePosition, MeasureControl
from PyQt5.QtWidgets import  QTableView, QMainWindow, QStyleFactory, \
    QAbstractItemView, QFileDialog, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sqlite3
import sys
from PyQt5.QtWidgets import QApplication
from matplotlib.animation import FuncAnimation
from openpyxl import Workbook
import loc_id_enterence
import pandas as pd
import subprocess
import os
import scipy.io
import oct2py
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import coordinate_cartesian
import matplotlib.patches as patches

coordinates_db = []
response = ()
weapon_coordinates = []
sensor_num = []
sensor_posts = []
sensor_names = []
sensor_positions = []
unit_names = []
sensor_names_2 = []
id_det_list = []
unit_names_ordered = []
ordered_ids = []
ordered_doa = []
ordered_level = []
ordered_toa = []

class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        global last_list
        global lat_temp
        global long_temp
        global temp_cumulative
        coords_dict = json.loads(msg)
        lon = coords_dict['geometry']['coordinates'][0]
        lat = coords_dict['geometry']['coordinates'][1]
        lat_temp = lat
        long_temp = lon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1274, 809)
        MainWindow.setWindowIcon(QtGui.QIcon("Microflownlogo.png"))
        MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.WindowMaximizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.centralwidget.setGeometry(QtCore.QRect(20, 20, 601, 501))
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 601, 501))
        self.frame_3.setFixedSize(601,501)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(165, 60, 100, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(165, 105, 100, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(165, 150, 100, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(165, 195, 100, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(165, 240, 100, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(165, 285, 100, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(165, 330, 100, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(165, 375, 100, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(165, 415, 100, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(480, 55, 100, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(480, 325, 100, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_16.setGeometry(QtCore.QRect(480, 370, 100, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_17.setGeometry(QtCore.QRect(480, 190, 100, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_18.setGeometry(QtCore.QRect(480, 280, 100, 20))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_21.setGeometry(QtCore.QRect(480, 235, 100, 20))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_23.setGeometry(QtCore.QRect(480, 100, 100, 20))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_24.setGeometry(QtCore.QRect(480, 145, 100, 20))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(20, 60, 121, 21))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(20, 105, 121, 21))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(20, 195, 121, 21))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(20, 150, 121, 21))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(20, 375, 121, 21))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(20, 330, 121, 21))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(20, 285, 131, 21))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(20, 415, 121, 21))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(335, 145, 121, 21))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(335, 320, 121, 41))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        self.label_21.setGeometry(QtCore.QRect(335, 270, 121, 41))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(325, 370, 151, 21))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setGeometry(QtCore.QRect(335, 100, 121, 21))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect(335, 55, 121, 21))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect(335, 220, 121, 41))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setWordWrap(True)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_3)
        self.label_26.setGeometry(QtCore.QRect(335, 190, 121, 21))
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame_3)
        self.label_27.setGeometry(QtCore.QRect(20, 240, 121, 21))
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_3)
        self.label_28.setGeometry(QtCore.QRect(250, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3, clicked = lambda:set_model_parameters())
        self.pushButton_8.setGeometry(QtCore.QRect(200, 460, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_8.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../savesettings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_3, clicked = lambda : filet_loc_det(response[0]))
        self.pushButton_9.setGeometry(QtCore.QRect(310, 460, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_9.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../defaultsettings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_19.setGeometry(QtCore.QRect(480, 405, 101, 16))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_29 = QtWidgets.QLabel(self.frame_3)
        self.label_29.setGeometry(QtCore.QRect(340, 400, 121, 41))
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setWordWrap(True)
        self.label_29.setObjectName("label_29")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_22.setGeometry(QtCore.QRect(480, 420, 101, 16))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(700, 12, 500, 21))
        self.comboBox.setObjectName("comboBox")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        #self.tableWidget.setGeometry(QtCore.QRect(630, 40, 631, 751))
        self.tableWidget.setMinimumSize(631, 751)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayoutWidget.setFixedWidth(621)

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.addWidget(self.frame_3,0,0,1,1)
        self.gridLayout.addWidget(self.horizontalLayoutWidget, 1, 0,1,1)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 2, 1)


        # Set the layout stretch for the main layout
        self.gridLayout.setColumnStretch(0, 0)  # Set the stretch factor for frame_3 column to 0
        self.gridLayout.setColumnStretch(1, 1)  # Set the stretch factor for tableWidget column to 1
        self.gridLayout.setRowStretch(0, 0)  # Set the stretch factor for frame_3 row to 0
        self.gridLayout.setRowStretch(1, 1)  # Set the stretch factor for horizontalLayoutWidget row to 1

        self.gridLayout.setContentsMargins(20, 40, 20, 30)

        self.lineEdit_5.setText('500')
        self.lineEdit_6.setText('1000*[1 1]')
        self.lineEdit_7.setText('2000*[1 1]')
        self.lineEdit_8.setText('15')
        self.lineEdit_9.setText('1.2466')
        self.lineEdit_10.setText('nan')
        self.lineEdit_11.setText('[0,0,0]')
        self.lineEdit_12.setText('44.55')
        self.lineEdit_13.setText('22.33125')
        self.lineEdit_14.setText('532.8')
        self.lineEdit_23.setText('43.7')
        self.lineEdit_24.setText('0.155')
        self.lineEdit_17.setText('0.8787')
        self.lineEdit_21.setText('181')
        self.lineEdit_18.setText('194')
        self.lineEdit_15.setText('0.04')
        self.lineEdit_16.setText('0')
        self.lineEdit_19.setText('55.0099826')
        self.lineEdit_22.setText('25.9431195')

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



        def filet_loc_det(database_name):
            global sensor_num, sensor_names
            conn = sqlite3.connect(database_name)
            loc_id_enterence.open_loc_id()
            id_loc = loc_id_enterence.loc_id
            # Define an empty list to store the values of id_det
            id_det_list = []

            # Execute the SQL query to select the values from id_det where id_loc matches the user input
            cursor = conn.cursor()
            cursor.execute("SELECT id_det FROM loc_det WHERE id_loc = ?", (id_loc,))
            # Loop through the results and append the values to the list
            for row in cursor:
                id_det_list.append(row[0])

            id_values = id_det_list
            list_units = []
            sensor_ids_int = []
            sensor_ids = list(cursor.execute(f"SELECT sensorid FROM detection WHERE id IN ({', '.join(str(id) for id in id_values)})"))

            for row in sensor_ids:
                sensor_ids_int.append(int(row[0]))
            for integer in sensor_ids_int:
                if integer in sensor_num:
                    list_units.append(sensor_names_2[sensor_num.index(integer)])
                else:
                    pass
            query = f"SELECT sensorid,time,azimuth,leveldb FROM detection WHERE id IN ({', '.join(str(id) for id in id_values)})"
                # Save the DataFrame to an Excel file with the same headers as the detection table

            count = 0
            for id in id_det_list:
                o_id = list(cursor.execute(
                    f"SELECT sensorid FROM detection WHERE id = ?", (id,)))
                ordered_ids.append(o_id[0])
                # Close the database connection
                o_doa = list(cursor.execute(
                    f"SELECT azimuth FROM detection WHERE id = ?", (id,)))
                ordered_doa.append(o_doa[0])
                # Close the database connection
                o_level = list(cursor.execute(
                    f"SELECT leveldb FROM detection WHERE id = ?", (id,)))
                ordered_level.append(o_level[0])
                # Close the database connection
                o_toa = list(cursor.execute(
                    f"SELECT time FROM detection WHERE id = ?", (id,)))
                ordered_toa.append(o_toa[0])
                # Close the database connection`
                count = count + 1
            conn.close()

            print(ordered_ids)
            print(id_det_list)
            print(ordered_doa)
            print(ordered_toa)
            print(ordered_level)


        def list_db_tables(database_name):
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
            table_view.setModel(model)
            table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.gridLayout.addWidget(table_view, 0, 1, 2, 1)
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

            # Close database connection
            conn.close()

        def get_position_db(database_name):
            global response
            global coordinates_db, sensor_num
            # Open connection to the database
            conn = sqlite3.connect(database_name)
            # Create a QSqlDatabase object to connect to the database
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(database_name)
            cursor = conn.cursor()
            cursor.execute("SELECT latitude, longitude, deviceid FROM device_position GROUP BY deviceid;")
            sensor_id = cursor.fetchall()
            cursor.execute("SELECT latitude, longitude FROM device_position GROUP BY deviceid;")
            results = cursor.fetchall()
            cursor.execute("SELECT deviceId FROM firmware_info;")
            units = cursor.fetchall()
            coordinates_db = []
            sensor_num = []
            for row in sensor_id:
                sensor_num.append(list(row)[-1])
            for row in units:
                unit_names.append(list(row)[-1])
            for row in results:
                coordinates_db.append(list(row))
            # Close the connection to the database

            conn.close()
        get_position_db(response[0])
        list_db_tables(response[0])

        for number in sensor_num:
            self.convert_last_two_digits(number)
        set1 = set(sensor_names)
        set2 = set(unit_names)
        extra_element = set1.difference(set2)
        for sensor in extra_element:
            coordinates_db.pop(sensor_names.index(sensor))
            sensor_names.remove(sensor)

        set1 = set(sensor_names)
        set2 = set(unit_names)
        extra_element = set1.difference(set2)
        for sensor in extra_element:
            coordinates_db.pop(sensor_names.index(sensor))
            sensor_names.remove(sensor)


        createMainMap(self.horizontalLayout)

        def set_model_parameters():
            global weapon_coordinates
            filet_loc_det(response[0])
            msgBox = QMessageBox()
            msgBox.setWindowIcon(QtGui.QIcon("Microflownlogo.png"))
            msgBox.setText("WARNING.")
            msgBox.setInformativeText("Are you sure to set parameters as filled?")
            msgBox.setWindowTitle("Warning")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.exec_()
            weapon_coordinates.append(float(self.lineEdit_19.text()))
            weapon_coordinates.append(float(self.lineEdit_22.text()))
            latlon_to_cartesian(weapon_coordinates, coordinates_db)

            change_variable_octave('        senRes     =', self.lineEdit_5.text())
            change_variable_octave('        gridRes    =', self.lineEdit_6.text())
            change_variable_octave('        gridSenRes =', self.lineEdit_7.text())
            change_variable_octave('        tempC =', self.lineEdit_8.text())
            change_variable_octave('            pr.density =', self.lineEdit_9.text())
            change_variable_octave('            ps.refPoint =', self.lineEdit_10.text())
            change_variable_octave('            ps.pos  =', self.lineEdit_11.text())
            change_variable_octave('            ps.azim =', self.lineEdit_12.text())
            change_variable_octave('            ps.elev =', self.lineEdit_13.text())
            change_variable_octave('            ps.v0 =', self.lineEdit_14.text())
            change_variable_octave('            pr.mass    =', self.lineEdit_23.text())
            change_variable_octave('            pr.caliber =', self.lineEdit_24.text())
            change_variable_octave('            pr.length  =', self.lineEdit_17.text())
            change_variable_octave('            srcLevelSph_dB_SPL =', self.lineEdit_21.text())
            change_variable_octave('            srcLevelSw_dB_SPL =', self.lineEdit_18.text())
            change_variable_octave('            ps.attnCoef =', self.lineEdit_15.text())
            change_variable_octave('            paramSw.impPosZ =', self.lineEdit_16.text())
            change_variable_octave('            sensorInfo.position =', sensor_positions)

            create_graph_animation()



        def latlon_to_cartesian(ref_latlon, latlon_list):
            global sensor_posts, sensor_names, sensor_positions
            # Convert reference lat-lon point to radians
            ref_lat = radians(ref_latlon[0])
            ref_lon = radians(ref_latlon[1])
            # Calculate reference Cartesian coordinates
            ref_x = cos(ref_lat) * cos(ref_lon)
            ref_y = cos(ref_lat) * sin(ref_lon)
            ref_z = 0
            for latlon in latlon_list:
                lat = radians(latlon[0])
                lon = radians(latlon[1])
                # Calculate distance between lat-lon points in meters
                d_lat = lat - ref_lat
                d_lon = lon - ref_lon
                a = sin(d_lat / 2) ** 2 + cos(ref_lat) * cos(lat) * sin(d_lon / 2) ** 2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                d = pygeodesy.haversine(ref_latlon[0], ref_latlon[1], latlon[0], latlon[1], radius=6371008.77141,
                                        wrap=False)
                theta = pygeodesy.bearing(ref_latlon[0], ref_latlon[1], latlon[0], latlon[1], wrap=False)
                # Calculate corresponding Cartesian coordinates
                x = d * cos(math.radians(360 - theta))
                y = d * sin(math.radians(360 - theta))
                z = 0
                sensor_posts.append([x, y, z])

            sensor_position = np.array(sensor_posts).T
            sensor_positions = "[" + ";".join([" ".join(map(str, row)) for row in sensor_position]) + "]"

        self.comboBox.setCurrentText('detection')

    def convert_last_two_digits(self,num):
        hex_num = hex(num)
        last_two_digits = hex_num[-2:]
        decimal_num = int(last_two_digits, 16)
        sensor_names.append('UNIT-01-000{}'.format(decimal_num))
        sensor_names_2.append('UNIT-01-000{}'.format(decimal_num))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Automated Forward Model Tester"))
        self.label_11.setText(_translate("MainWindow", "Sensor Resolution:"))
        self.label_12.setText(_translate("MainWindow", "Grid Resolution:"))
        self.label_13.setText(_translate("MainWindow", "Temperature [°C]:"))
        self.label_14.setText(_translate("MainWindow", "Gird-Sensor Resolution:"))
        self.label_15.setText(_translate("MainWindow", "Azimuth [mils]:"))
        self.label_16.setText(_translate("MainWindow", "Weapon Position [m]:"))
        self.label_17.setText(_translate("MainWindow", "Weapon Ref. Point [UTM]:"))
        self.label_18.setText(_translate("MainWindow", "Elevation [mils]:"))
        self.label_19.setText(_translate("MainWindow", "Caliber Diameter [m]:"))
        self.label_20.setText(_translate("MainWindow", "Attenuation Coefficient [dB/100m]:"))
        self.label_21.setText(_translate("MainWindow", "Shockwave Source Level [dB SPL]:"))
        self.label_22.setText(_translate("MainWindow", "Impact Position Height [m]:"))
        self.label_23.setText(_translate("MainWindow", "Caliber Mass [kg]:"))
        self.label_24.setText(_translate("MainWindow", "Muzzle Velocity [m/s]:"))
        self.label_25.setText(_translate("MainWindow", "Spherical Wave Source Level [dB SPL]:"))
        self.label_26.setText(_translate("MainWindow", "Caliber Lenght [m]:"))
        self.label_27.setText(_translate("MainWindow", "Air Density [kg/m3]"))
        self.label_28.setText(_translate("MainWindow", "Advanced Settings"))
        self.pushButton_8.setText(_translate("MainWindow", "Run Calculation"))
        self.pushButton_9.setText(_translate("MainWindow", "New Database"))
        self.label_29.setText(_translate("MainWindow", "Weapon Latitude - Longitude:"))

def change_variable_octave(variable, temp_input):
    var = ''
    with open('forward_model/fwdCompute.m', 'r') as f:
        for line in f:
            if variable in line:
                var = line
            else:
                pass

    with open('forward_model/fwdCompute.m', 'r') as f:
        code = f.read()

    code = code.replace(var, variable + ' {}; \n'.format(temp_input))

    with open('forward_model/fwdCompute.m', 'w') as f:
        f.write(code)


def createMainMap(layout):
    global coordinates_db
    mainmap = folium.Map(location=(float(coordinates_db[-1][0]),float(coordinates_db[-1][1])), control_scale=True,
                         tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                         attr='Esri', name='Esri Satellite', overlay=False, control=True, zoom_start=12,
                       detect_retina=True)


    formatter = "function(num) {return L.Util.formatNum(num, 6) + ' º ';};"
    MousePosition(position="topright", separator=" | ", empty_string="NaN", lat_first=True, num_digits=20,
                  prefix="Coordinates:",
                  lat_formatter=formatter, lng_formatter=formatter, ).add_to(mainmap)

    mainmap.add_child(MeasureControl())
    for sensor in coordinates_db:
        folium.Marker(location=(sensor[0],sensor[1]), icon=folium.features.CustomIcon('icon_sensor.png',
                      icon_size=(19, 22)), popup=sensor_names[coordinates_db.index(sensor)]).add_to(mainmap)
        unit_names_ordered.append(sensor_names[coordinates_db.index(sensor)])

    view = QtWebEngineWidgets.QWebEngineView()
    view.setContentsMargins(2, 5, 28, 5)
    view.resize(630, 320)
    page = WebEnginePage(view)
    view.setPage(page)
    data = io.BytesIO()
    mainmap.save(data, close_file=False)
    view.setHtml(data.getvalue().decode())
    layout.addWidget(view)

def create_graph_animation():
    global sensor_names
    oc = oct2py.Oct2Py()

    sensor_positions = []

    def run_octave_function(m_file, function_name, *args):
        # Build the command to run the Octave function
        cmd = ['octave', '--eval', f'{function_name}({",".join(args)}); save my_data.mat -mat']

        # Change the current directory to the location of the .m file
        # so that Octave can find it
        with open(m_file, 'r') as f:
            subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(f.name)), capture_output=True)

    #run_octave_function('forward_model/fwdCompute.m', 'clear classes')
    #run_octave_function('forward_model/fwdCompute.m', '[resSW , resSE] = fwdCompute.exampleSimple')

    data = scipy.io.loadmat('forward_model\my_data.mat')

    validity_SE = data['resSE']['valid']
    toa_SE = data['resSE']['toa']
    doa_SE = data['resSE']['doa']
    level_SE = data['resSE']['lev']

    validity_SW = data['resSW']['valid']
    toa_SW = data['resSW']['toaP']
    doa_SW = data['resSW']['doaP']
    impact_SW = data['resSW']['impact']
    level_SW = data['resSW']['lev']
    time_of_flight = data['resSW']['ToF']
    debug = data['resSW']['debug']

    proj_F = debug[0][0][0][0][0][0]['projF']
    proj_F_N = proj_F['N'][0][0]
    proj_F_x = proj_F['x'][0][0]
    proj_F_vel = proj_F['vel'][0][0]
    proj_F_t = proj_F['t'][0][0]
    proj_F_state = proj_F['state'][0][0]
    proj_F_T = proj_F['T'][0][0]
    proj_F_wind = proj_F['wind'][0][0]
    proj_F_c0 = proj_F['c0'][0][0]
    proj_F_velRel = proj_F['velRel'][0][0]
    proj_F_MAbs = proj_F['MAbs'][0][0]
    proj_F_MRel = proj_F['MRel'][0][0]
    proj_F_relLev0CPA = proj_F['relLev0CPA'][0][0]

    proj_S = debug[0][0][0][0][0][0]['projs']
    proj_S_valid = proj_S['valid']
    proj_S_t = proj_S['t']
    proj_S_x = proj_S['x']
    proj_S_vel = proj_S['vel']
    proj_S_T = proj_S['T']
    proj_S_N = proj_S['N']
    proj_S_wind = proj_S['wind']
    proj_S_relLev0CPA = proj_S['relLev0CPA']

    ray_S = debug[0][0][0][0][0][0]['rays']
    ray_S_valid = ray_S['valid']
    ray_S_t = ray_S['t']
    ray_S_x = ray_S['x']
    ray_S_p = ray_S['p']
    ray_S_T = ray_S['T']
    ray_S_N = ray_S['N']
    ray_S_relLev_TravD = ray_S['relLev_TravD']

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot3D(proj_F_x[0], proj_F_x[1], proj_F_x[2])
    ax.scatter(proj_F_x[0][-1], proj_F_x[1][-1], proj_F_x[2][-1], c='red')

    coordinate_cartesian.latlon_to_cartesian(weapon_coordinates, coordinates_db)

    sensor_positions = coordinate_cartesian.sensor_posts
    for j in range(len(sensor_positions)):
        ax.scatter(sensor_positions[j][0], sensor_positions[j][1], sensor_positions[j][2], c='blue', s=10)
        ax.text(sensor_positions[j][0], sensor_positions[j][1], sensor_positions[j][2], unit_names_ordered[j])
    for i in range(len(ray_S_valid[0])):
        if ray_S_valid[0][i][0][0] == 0:
            pass
        else:
            ax.plot3D(ray_S_x[0][i][0], ray_S_x[0][i][1], ray_S_x[0][i][2], linestyle='dotted')

    ax.autoscale_view()

    proj, = ax.plot3D(xs=proj_F_x[0], ys=proj_F_x[1], zs=proj_F_x[2], c='#9DDFDD')
    x = np.array(proj_F_x[0])
    y = np.array(proj_F_x[1])
    z = np.array(proj_F_x[2])


    def animate_projection(i):
        proj.set_data(x[:i], y[:i])
        proj.set_3d_properties(z[:i])
        # cone.set_data(x_2[:i], y_2[:i])
        # cone.set_3d_properties(z_2[:i])
        # doa.set_data(x_3[:i], y_3[:i])
        # doa.set_3d_properties(z_3[:i])
        # ax.set_xlim(0, 50000)
        # ax.set_ylim(0, 50000)
        # ax.set_zlim(0, 20000)
        ax.set_title("Trajectory Simulation of the Event - t({})s".format(i))

    # create an animation using the animate function and
    # specify the number of frames and the length of the animation
    #anim = FuncAnimation(fig, animate_projection, frames=500, interval=10, repeat = True)

    ax.set_xlim(0, 10000)
    ax.set_ylim(0, 12000)
    ax.set_zlim(0, 5000)
    plt.show()
    unit_names_ordered.clear()
    sensor_positions.clear()

    def comparison_graph():
        # First dataset
        angles1 = []
        times1 = []
        bar_values1 = []


        #print (actual_angle_degrees)

        # Second dataset
        angles2 = []
        times2 = []
        bar_values2 = []

        # Convert angles to radians

        for i in range(len(doa_SW[0][0][0])):
            radian_angle = math.atan2(float(doa_SW[0][0][0][i]), float(doa_SW[0][0][1][i]))
            angles1.append(-1*math.degrees(radian_angle))
            times1.append(toa_SW[0][0][0][i])
            bar_values1.append(level_SW[0][0][0][i])
        print(angles1)
        print(times1)
        print(bar_values1)

        angles_radians1 = np.radians(angles1)
        angles_radians2 = np.radians(angles2)


        # Create the figure and subplots
        fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)

        # Set aspect ratio to equal for the angle graph subplot
        ax1.set_aspect('equal')

        # Plot the arcs and arrows for the first dataset in the angle graph subplot
        for angle, x, y in zip(angles_radians1, times1, np.zeros_like(times1)):
            arc = patches.Arc((x, y), 0.2, 0.2, 0, 0, math.degrees(angle))
            ax1.add_patch(arc)
            ax1.annotate("", xy=(x + np.cos(angle), y + np.sin(angle)), xytext=(x, y),
                         arrowprops=dict(arrowstyle="->"))
            ax1.text(x + 0.5 * np.cos(angle), y + 0.5 * np.sin(angle),
                     f"{int(np.degrees(angle))}°", ha='center', va='center')

        # Create vertical dashed lines on the angle graph subplot for the first dataset
        for t in times1:
            ax1.axvline(x=t, linestyle='dashed', color='gray')

        # Plot the bar chart for the first dataset in the second subplot
        ax2.bar(times1, bar_values1, width=0.2, align='center', color='blue')

        # Create vertical dashed lines on the bar chart subplot for the first dataset
        for t in times1:
            ax2.axvline(x=t, linestyle='dashed', color='gray')
            ax2.text(t, bar_values1[times1.index(t)] + 1.2, f"{int(bar_values1[times1.index(t)])}", ha='center',
                     va='center')

        # Plot the arcs and arrows for the second dataset in the angle graph subplot
        for angle, x, y in zip(angles_radians2, times2, np.zeros_like(times2)):
            arc = patches.Arc((x, y), 0.2, 0.2, 0, 0, math.degrees(angle))
            ax1.add_patch(arc)
            ax1.annotate("", xy=(x + np.cos(angle), y + np.sin(angle)), xytext=(x, y),
                         arrowprops=dict(arrowstyle="->", color='green'))
            ax1.text(x + 0.5 * np.cos(angle), y + 0.5 * np.sin(angle),
                     f"{int(np.degrees(angle))}°", ha='center', va='center', color='green')

        # Create vertical dashed lines on the angle graph subplot for the second dataset
        for t in times2:
            ax1.axvline(x=t, linestyle='dashed', color='gray')
            ax2.text(t, bar_values2[times2.index(t)] + 1.2, f"{int(bar_values2[times2.index(t)])}", ha='center',
                     va='center')

        # Plot the bar chart for the second dataset in the second subplot
        ax2.bar(times2, bar_values2, width=0.2, align='center', color='green')

        # Create vertical dashed lines on the bar chart subplot for the second dataset
        for t in times2:
            ax2.axvline(x=t, linestyle='dashed', color='gray')

        # Set labels and title for the angle graph subplot
        ax1.set_ylabel('Y')
        ax1.set_title('Angles in Degrees (°)', pad=20)

        # Set labels and title for the bar chart subplot
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Value')
        ax2.set_title('SPL Sound Pressure Level (dB)', pad=20)

        # Adjust the spacing between subplots
        plt.subplots_adjust(hspace=0.3)

        # Display the graph
        plt.show()
    comparison_graph()


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
