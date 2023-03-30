import json
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import scipy.io
import oct2py
import numpy as np
import matplotlib.pyplot as plt
import folium, io
from PyQt5 import QtWebEngineWidgets
from folium.plugins import Draw, MousePosition, MeasureControl,MiniMap
from matplotlib.animation import FuncAnimation
from scipy.interpolate import interp1d
from PyQt5.QtWidgets import QApplication, QTableView, QFrame, QVBoxLayout, QComboBox, QMainWindow, QStyleFactory, \
    QAbstractItemView, QFileDialog
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sqlite3
import coordinate_cartesian
import os
import sys
from PyQt5.QtWidgets import QApplication

coordinates_db = []
response = ()

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
        self.horizontalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 520, 601, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(MainWindow)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 601, 501))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
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
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3, clicked = lambda : set_model_parameters())
        self.pushButton_8.setGeometry(QtCore.QRect(200, 460, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_8.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../savesettings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_3)
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
        self.tableWidget = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget.setGeometry(QtCore.QRect(630, 40, 631, 751))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(630, 12, 631, 21))
        self.comboBox.setObjectName("comboBox")

        self.lineEdit_5.setText('500')
        self.lineEdit_6.setText('1000*[1 1]')
        self.lineEdit_7.setText('2000*[1 1]')
        self.lineEdit_8.setText('10')
        self.lineEdit_9.setText('1.2466')
        self.lineEdit_10.setText('nan')
        self.lineEdit_11.setText('[0,0,0]')
        self.lineEdit_12.setText('36')
        self.lineEdit_13.setText('18.2812')
        self.lineEdit_14.setText('926')
        self.lineEdit_23.setText('43.7')
        self.lineEdit_24.setText('0.155')
        self.lineEdit_17.setText('0.8787')
        self.lineEdit_21.setText('181')
        self.lineEdit_18.setText('194')
        self.lineEdit_15.setText('0.04')
        self.lineEdit_16.setText('0')

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

        def list_db_tables(database_name):
            global coordinates_db
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
            table_view.setGeometry(0, 0, 631, 751)
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
            conn.close()

        def get_position_db(database_name):
            global response
            global coordinates_db
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
            coordinates_db = []
            sensor_num = []
            for row in results:
                coordinates_db.append(list(row))
            print(coordinates_db)
            for row in sensor_id:
                sensor_num.append(list(row)[-1])
            print(sensor_num)
            # Close the connection to the database
            conn.close()

        get_position_db(response[0])
        list_db_tables(response[0])
        createMainMap(self.horizontalLayout)

        def set_model_parameters():
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.pushButton_9.setText(_translate("MainWindow", "Create Graph"))
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


def evaulate_scenario():
    oc = oct2py.Oct2Py()
    sensor_positions = []
    def run_octave_function(m_file, function_name, *args):
        # Build the command to run the Octave function
        cmd = ['octave', '--eval', f'{function_name}({",".join(args)}); save my_data.mat -mat']

        # Change the current directory to the location of the .m file
        # so that Octave can find it
        with open(m_file, 'r') as f:
            subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(f.name)), capture_output=True)

    #run_octave_function(r'C:\Users\Eraslan\PycharmProjects\mdtProject1\forward_model/fwdCompute.m','[resSW , resSE] = fwdCompute.exampleSimple')

    data = scipy.io.loadmat(r'C:\Users\Eraslan\PycharmProjects\mdtProject1\forward_model\my_data.mat')

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
    ax.scatter(proj_F_x[0][-1], proj_F_x[1][-1], proj_F_x[2][-1], c = 'red')
    coordinate_cartesian.mgrs_to_latlon(['35UMA3241096412'],['35UMB2850403535','35UMB2899003931','35UMB2626403309',
                                        '35UMB2496603017','35UMB2425402105', '35UMA2209199292','35UMB2273302010',
                                        '35UMB2195500272','35UMB2371404445'])

    sensor_positions = coordinate_cartesian.sensor_posts
    sensor_names = ['S2','S1','S3','S4','S5','S9','S6','S7','S8']


    for j in range(len(sensor_positions)):
        ax.scatter(sensor_positions[j][0],sensor_positions[j][1], sensor_positions[j][2], c= 'blue', s=10)
        ax.text(sensor_positions[j][0],sensor_positions[j][1], sensor_positions[j][2], sensor_names[j])
    for i in range(len(ray_S_valid[0])):
        if ray_S_valid[0][i][0][0] == 0:
            pass
        else:
            ax.plot3D(ray_S_x[0][i][0], ray_S_x[0][i][1], ray_S_x[0][i][2], linestyle = 'dotted')


    ax.autoscale_view()

    proj, = ax.plot3D(xs=proj_F_x[0], ys=proj_F_x[1], zs=proj_F_x[2] ,c= '#9DDFDD')
    x = np.array(proj_F_x[0])
    y = np.array(proj_F_x[1])
    z = np.array(proj_F_x[2])

    def animate_projection(i):
        proj.set_data(x[:i], y[:i])
        proj.set_3d_properties(z[:i])
        #cone.set_data(x_2[:i], y_2[:i])
        #cone.set_3d_properties(z_2[:i])
        #doa.set_data(x_3[:i], y_3[:i])
        #doa.set_3d_properties(z_3[:i])
        #ax.set_xlim(0, 50000)
        #ax.set_ylim(0, 50000)
        #ax.set_zlim(0, 20000)
        ax.set_title("Trajectory Simulation of the Event - t({})s".format(i))


    # create an animation using the animate function and
    # specify the number of frames and the length of the animation
    #anim = FuncAnimation(fig, animate_projection, frames=500, interval=10, repeat = True)

    ax.set_xlim(0, 10000)
    ax.set_ylim(0, 12000)
    ax.set_zlim(0, 5000)
    #plt.show()

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
        folium.Marker(location=(sensor[0],sensor[1]), icon=folium.features.CustomIcon('icon_sensor.png', icon_size=(19, 22))).add_to(mainmap)

    view = QtWebEngineWidgets.QWebEngineView()
    view.setContentsMargins(2, 5, 28, 50)
    view.setFixedSize(630, 320)
    page = WebEnginePage(view)
    view.setPage(page)
    data = io.BytesIO()
    mainmap.save(data, close_file=False)
    view.setHtml(data.getvalue().decode())
    layout.addWidget(view)


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