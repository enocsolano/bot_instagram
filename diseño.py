# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diseño.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_control = QFrame(self.frame)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setStyleSheet(u"QPushButton{\n"
"padding: 13% 0;\n"
"border: 1px solid rgb(31, 118, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(31, 118, 255);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(212, 212, 212);\n"
"color: rgb(8, 0, 20);\n"
"border: 1px solid rgb(212, 212, 212);\n"
"}\n"
"")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_control)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bt_inicio = QPushButton(self.frame_control)
        self.bt_inicio.setObjectName(u"bt_inicio")

        self.verticalLayout.addWidget(self.bt_inicio)

        self.bt_registros = QPushButton(self.frame_control)
        self.bt_registros.setObjectName(u"bt_registros")

        self.verticalLayout.addWidget(self.bt_registros)

        self.bt_base_datos = QPushButton(self.frame_control)
        self.bt_base_datos.setObjectName(u"bt_base_datos")

        self.verticalLayout.addWidget(self.bt_base_datos)

        self.verticalSpacer = QSpacerItem(20, 291, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_control)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_control)

        self.frame_contenedor = QFrame(self.frame)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.verticalLayout_3 = QVBoxLayout(self.page_inicio)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_head_inicio = QFrame(self.page_inicio)
        self.frame_head_inicio.setObjectName(u"frame_head_inicio")
        self.frame_head_inicio.setStyleSheet(u"QFrame{\n"
"background-color: rgb(31, 118, 255);\n"
"color: #fff;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.frame_head_inicio.setFrameShape(QFrame.StyledPanel)
        self.frame_head_inicio.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_head_inicio)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(261, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_head_inicio = QLabel(self.frame_head_inicio)
        self.label_head_inicio.setObjectName(u"label_head_inicio")
        self.label_head_inicio.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_head_inicio)

        self.horizontalSpacer_2 = QSpacerItem(261, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_head_inicio)

        self.frame_body_inicio = QFrame(self.page_inicio)
        self.frame_body_inicio.setObjectName(u"frame_body_inicio")
        self.frame_body_inicio.setStyleSheet(u"")
        self.frame_body_inicio.setFrameShape(QFrame.StyledPanel)
        self.frame_body_inicio.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_body_inicio)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(96, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.frame_body_inicio_seleccionar_equipo_trabajar = QFrame(self.frame_body_inicio)
        self.frame_body_inicio_seleccionar_equipo_trabajar.setObjectName(u"frame_body_inicio_seleccionar_equipo_trabajar")
        self.frame_body_inicio_seleccionar_equipo_trabajar.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(212, 212, 212);\n"
"background-color: rgb(212, 212, 212);\n"
"}")
        self.frame_body_inicio_seleccionar_equipo_trabajar.setFrameShape(QFrame.StyledPanel)
        self.frame_body_inicio_seleccionar_equipo_trabajar.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_body_inicio_seleccionar_equipo_trabajar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 5, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.comboBox_body_inicio_seleccionar = QComboBox(self.frame_body_inicio_seleccionar_equipo_trabajar)
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.addItem("")
        self.comboBox_body_inicio_seleccionar.setObjectName(u"comboBox_body_inicio_seleccionar")
        self.comboBox_body_inicio_seleccionar.setStyleSheet(u"")

        self.gridLayout.addWidget(self.comboBox_body_inicio_seleccionar, 3, 1, 1, 1)

        self.label_body_inicio_seleccionar_equipo_trabajar = QLabel(self.frame_body_inicio_seleccionar_equipo_trabajar)
        self.label_body_inicio_seleccionar_equipo_trabajar.setObjectName(u"label_body_inicio_seleccionar_equipo_trabajar")
        self.label_body_inicio_seleccionar_equipo_trabajar.setStyleSheet(u"QFrame{\n"
"border: 0;\n"
"}")
        self.label_body_inicio_seleccionar_equipo_trabajar.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_body_inicio_seleccionar_equipo_trabajar, 1, 1, 1, 1)

        self.bt_body_inicio_seleccionar_equipo_trabajar_bt = QPushButton(self.frame_body_inicio_seleccionar_equipo_trabajar)
        self.bt_body_inicio_seleccionar_equipo_trabajar_bt.setObjectName(u"bt_body_inicio_seleccionar_equipo_trabajar_bt")

        self.gridLayout.addWidget(self.bt_body_inicio_seleccionar_equipo_trabajar_bt, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_body_inicio_seleccionar_equipo_trabajar, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(96, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 87, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_body_inicio)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 9)
        self.stackedWidget.addWidget(self.page_inicio)
        self.page_inicio_IMM_1000 = QWidget()
        self.page_inicio_IMM_1000.setObjectName(u"page_inicio_IMM_1000")
        self.stackedWidget.addWidget(self.page_inicio_IMM_1000)
        self.page_inicio_IMM_2000 = QWidget()
        self.page_inicio_IMM_2000.setObjectName(u"page_inicio_IMM_2000")
        self.stackedWidget.addWidget(self.page_inicio_IMM_2000)
        self.page_inicio_ATELLICA_CH = QWidget()
        self.page_inicio_ATELLICA_CH.setObjectName(u"page_inicio_ATELLICA_CH")
        self.stackedWidget.addWidget(self.page_inicio_ATELLICA_CH)
        self.page_inicio_ATELLICA_IM = QWidget()
        self.page_inicio_ATELLICA_IM.setObjectName(u"page_inicio_ATELLICA_IM")
        self.stackedWidget.addWidget(self.page_inicio_ATELLICA_IM)
        self.page_inicio_DIMENSION = QWidget()
        self.page_inicio_DIMENSION.setObjectName(u"page_inicio_DIMENSION")
        self.stackedWidget.addWidget(self.page_inicio_DIMENSION)
        self.page_inicio_DIMENSION2 = QWidget()
        self.page_inicio_DIMENSION2.setObjectName(u"page_inicio_DIMENSION2")
        self.stackedWidget.addWidget(self.page_inicio_DIMENSION2)
        self.page_inicio_DIMENSION3 = QWidget()
        self.page_inicio_DIMENSION3.setObjectName(u"page_inicio_DIMENSION3")
        self.stackedWidget.addWidget(self.page_inicio_DIMENSION3)
        self.page_inicio_DIMENSION4 = QWidget()
        self.page_inicio_DIMENSION4.setObjectName(u"page_inicio_DIMENSION4")
        self.stackedWidget.addWidget(self.page_inicio_DIMENSION4)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.stackedWidget.addWidget(self.page_9)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_registros = QWidget()
        self.page_registros.setObjectName(u"page_registros")
        self.horizontalLayout_3 = QHBoxLayout(self.page_registros)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.page_registros)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.page_registros)
        self.page_registros_IMM_1000 = QWidget()
        self.page_registros_IMM_1000.setObjectName(u"page_registros_IMM_1000")
        self.stackedWidget.addWidget(self.page_registros_IMM_1000)
        self.page_registros_IMM_2000 = QWidget()
        self.page_registros_IMM_2000.setObjectName(u"page_registros_IMM_2000")
        self.stackedWidget.addWidget(self.page_registros_IMM_2000)
        self.page_registros_ATELLICA_CH = QWidget()
        self.page_registros_ATELLICA_CH.setObjectName(u"page_registros_ATELLICA_CH")
        self.stackedWidget.addWidget(self.page_registros_ATELLICA_CH)
        self.page_registros_ATELLICA_IM = QWidget()
        self.page_registros_ATELLICA_IM.setObjectName(u"page_registros_ATELLICA_IM")
        self.stackedWidget.addWidget(self.page_registros_ATELLICA_IM)
        self.page_registros_DIMENSION = QWidget()
        self.page_registros_DIMENSION.setObjectName(u"page_registros_DIMENSION")
        self.stackedWidget.addWidget(self.page_registros_DIMENSION)
        self.page_registros_ADVIA_2120 = QWidget()
        self.page_registros_ADVIA_2120.setObjectName(u"page_registros_ADVIA_2120")
        self.stackedWidget.addWidget(self.page_registros_ADVIA_2120)
        self.page_registros_CA_660 = QWidget()
        self.page_registros_CA_660.setObjectName(u"page_registros_CA_660")
        self.stackedWidget.addWidget(self.page_registros_CA_660)
        self.page_registros_CLINITEK = QWidget()
        self.page_registros_CLINITEK.setObjectName(u"page_registros_CLINITEK")
        self.stackedWidget.addWidget(self.page_registros_CLINITEK)
        self.page_registros_ADVANTUS = QWidget()
        self.page_registros_ADVANTUS.setObjectName(u"page_registros_ADVANTUS")
        self.stackedWidget.addWidget(self.page_registros_ADVANTUS)
        self.page_registros_LIASION_XL = QWidget()
        self.page_registros_LIASION_XL.setObjectName(u"page_registros_LIASION_XL")
        self.stackedWidget.addWidget(self.page_registros_LIASION_XL)
        self.page_registros_CM_250 = QWidget()
        self.page_registros_CM_250.setObjectName(u"page_registros_CM_250")
        self.stackedWidget.addWidget(self.page_registros_CM_250)
        self.page_registros_COUNTER_XS = QWidget()
        self.page_registros_COUNTER_XS.setObjectName(u"page_registros_COUNTER_XS")
        self.stackedWidget.addWidget(self.page_registros_COUNTER_XS)
        self.page_registros_COUNTER_19 = QWidget()
        self.page_registros_COUNTER_19.setObjectName(u"page_registros_COUNTER_19")
        self.stackedWidget.addWidget(self.page_registros_COUNTER_19)
        self.page_registros_FUJI_500 = QWidget()
        self.page_registros_FUJI_500.setObjectName(u"page_registros_FUJI_500")
        self.stackedWidget.addWidget(self.page_registros_FUJI_500)
        self.page_registros_NOVUS = QWidget()
        self.page_registros_NOVUS.setObjectName(u"page_registros_NOVUS")
        self.stackedWidget.addWidget(self.page_registros_NOVUS)
        self.page_base_datos = QWidget()
        self.page_base_datos.setObjectName(u"page_base_datos")
        self.horizontalLayout_4 = QHBoxLayout(self.page_base_datos)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.page_base_datos)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.stackedWidget.addWidget(self.page_base_datos)
        self.page_base_datos_IMM_1000 = QWidget()
        self.page_base_datos_IMM_1000.setObjectName(u"page_base_datos_IMM_1000")
        self.stackedWidget.addWidget(self.page_base_datos_IMM_1000)
        self.page_30 = QWidget()
        self.page_30.setObjectName(u"page_30")
        self.stackedWidget.addWidget(self.page_30)
        self.page_31 = QWidget()
        self.page_31.setObjectName(u"page_31")
        self.stackedWidget.addWidget(self.page_31)
        self.page_32 = QWidget()
        self.page_32.setObjectName(u"page_32")
        self.stackedWidget.addWidget(self.page_32)
        self.page_33 = QWidget()
        self.page_33.setObjectName(u"page_33")
        self.stackedWidget.addWidget(self.page_33)
        self.page_34 = QWidget()
        self.page_34.setObjectName(u"page_34")
        self.stackedWidget.addWidget(self.page_34)
        self.page_35 = QWidget()
        self.page_35.setObjectName(u"page_35")
        self.stackedWidget.addWidget(self.page_35)
        self.page_36 = QWidget()
        self.page_36.setObjectName(u"page_36")
        self.stackedWidget.addWidget(self.page_36)
        self.page_37 = QWidget()
        self.page_37.setObjectName(u"page_37")
        self.stackedWidget.addWidget(self.page_37)
        self.page_38 = QWidget()
        self.page_38.setObjectName(u"page_38")
        self.stackedWidget.addWidget(self.page_38)
        self.page_39 = QWidget()
        self.page_39.setObjectName(u"page_39")
        self.stackedWidget.addWidget(self.page_39)
        self.page_40 = QWidget()
        self.page_40.setObjectName(u"page_40")
        self.stackedWidget.addWidget(self.page_40)
        self.page_41 = QWidget()
        self.page_41.setObjectName(u"page_41")
        self.stackedWidget.addWidget(self.page_41)
        self.page_29 = QWidget()
        self.page_29.setObjectName(u"page_29")
        self.stackedWidget.addWidget(self.page_29)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_contenedor)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 8)

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(32)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_inicio.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.bt_registros.setText(QCoreApplication.translate("MainWindow", u"REGISTROS", None))
        self.bt_base_datos.setText(QCoreApplication.translate("MainWindow", u"BASE DE DATOS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ENOC SOLANO", None))
        self.label_head_inicio.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.comboBox_body_inicio_seleccionar.setItemText(0, QCoreApplication.translate("MainWindow", u"IMM 1000", None))
        self.comboBox_body_inicio_seleccionar.setItemText(1, QCoreApplication.translate("MainWindow", u"IMM 2000", None))
        self.comboBox_body_inicio_seleccionar.setItemText(2, QCoreApplication.translate("MainWindow", u"ATELLICA CH", None))
        self.comboBox_body_inicio_seleccionar.setItemText(3, QCoreApplication.translate("MainWindow", u"ATELLICA IM", None))
        self.comboBox_body_inicio_seleccionar.setItemText(4, QCoreApplication.translate("MainWindow", u"DIMENSION", None))
        self.comboBox_body_inicio_seleccionar.setItemText(5, QCoreApplication.translate("MainWindow", u"ADVIA 2120", None))
        self.comboBox_body_inicio_seleccionar.setItemText(6, QCoreApplication.translate("MainWindow", u"CA 660", None))
        self.comboBox_body_inicio_seleccionar.setItemText(7, QCoreApplication.translate("MainWindow", u"CLINITEK ADVANTUS", None))
        self.comboBox_body_inicio_seleccionar.setItemText(8, QCoreApplication.translate("MainWindow", u"LIASION XL", None))
        self.comboBox_body_inicio_seleccionar.setItemText(9, QCoreApplication.translate("MainWindow", u"CM 250", None))
        self.comboBox_body_inicio_seleccionar.setItemText(10, QCoreApplication.translate("MainWindow", u"COUNTER XS", None))
        self.comboBox_body_inicio_seleccionar.setItemText(11, QCoreApplication.translate("MainWindow", u"COUNTER 19", None))
        self.comboBox_body_inicio_seleccionar.setItemText(12, QCoreApplication.translate("MainWindow", u"FUJI 500", None))
        self.comboBox_body_inicio_seleccionar.setItemText(13, QCoreApplication.translate("MainWindow", u"NOVUS", None))

        self.label_body_inicio_seleccionar_equipo_trabajar.setText(QCoreApplication.translate("MainWindow", u"SELECCIONE EQUIPO A TRABAJAR", None))
        self.bt_body_inicio_seleccionar_equipo_trabajar_bt.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"P\u00c1GINA REGISTROS", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"P\u00c1GINA BASE DATOS", None))
    # retranslateUi

