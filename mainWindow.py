# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 690)
        MainWindow.setMinimumSize(QtCore.QSize(1090, 690))
        MainWindow.setMaximumSize(QtCore.QSize(1090, 690))
        MainWindow.setWindowTitle("Просмотр Плана Секции")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #
        # self.myDict = {
        #     '110': ['Комната 111', '112', '113', '114', '115', '116', '117', '118', ],
        #     '210': ['211', '212', '213', '214', '215', '216', '217', '218', ],
        #     '120': ['121', '122', '123', '124', '125', '126', '127', '128', ],
        #     '220': ['221', '222', '223', '224', '225', '226', '227', '228', ],
        #     '130': ['131', '132', '133', '134', '135', '136', '137', '138', ],
        #     '230': ['231', '232', '233', '234', '235', '236', '237', '238', ],
        #     '140': ['141', '142', '143', '144', '145', '146', '147', '148', ],
        #     '240': ['241', '242', '243', '244', '245', '246', '247', '248', ],
        #     '150': ['151', '152', '153', '154', '155', '156', '157', '158', ],
        #     '250': ['251', '252', '253', '254', '255', '256', '257', '258', ],
        #     '160': ['161', '162', '163', '164', '165', '166', '167', '168', ],
        #     '260': ['261', '262', '263', '264', '265', '266', '267', '268', ],
        #     '170': ['171', '172', '173', '174', '175', '176', '177', '178', ],
        #     '270': ['271', '272', '273', '274', '275', '276', '277', '278', ],
        #     '180': ['181', '182', '183', '184', '185', '186', '187', '188', ],
        #     '280': ['281', '282', '283', '284', '285', '286', '287', '288', ],
        #     '190': ['191', '192', '193', '194', '195', '196', '197', '198', ],
        #     '290': ['291', '292', '293', '294', '295', '296', '297', '298', ],
        # }
        #
        # self.centralwidget = QtWidgets.QWidget()
        # self.centralwidget.setObjectName("centralwidget")
        # self.setCentralWidget(self.centralwidget)
        #
        # self.layout = QtWidgets.QGridLayout(self.centralwidget)
        #
        # self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        #
        #
        #
        # for c in self.myDict.keys():
        #     self.comboBox.addItem(f"секция {c}")
        # self.layout.addWidget(self.comboBox, 1, 0, 143, 0,)
        #
        # row = 1
        # column = 0
        # self.labels = []
        # for i, lbl in enumerate(self.myDict['110']):
        #     label = QLabel(lbl, alignment=QtCore.Qt.AlignCenter)
        #     label.setStyleSheet("background-color: rgb(245, 145, 45);")
        #     label.setFixedSize(105, 21)
        #     self.labels.append(label)
        #
        #     column = i
        #     if i > 3:
        #         row = 2
        #         column = i - 4
        #     self.layout.addWidget(self.labels[i], row, column, 1, 1)
        #
        # self.comboBox.currentTextChanged.connect(self.current_text_changed)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(420, 40, 209, 50))
        self.comboBox.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")


        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(845, 606, 209, 50))
        self.pushButton_4.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(845, 120, 209, 50))
        self.pushButton_7.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")

        # self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_9.setGeometry(QtCore.QRect(845, 445, 209, 50))
        # self.pushButton_9.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";")
        # self.pushButton_9.setObjectName("pushButton_9")
        #
        #
        # self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_10.setGeometry(QtCore.QRect(845, 185, 209, 50))
        # self.pushButton_10.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";")
        # self.pushButton_10.setObjectName("pushButton_10")
        #
        # self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_11.setGeometry(QtCore.QRect(845, 250, 209, 50))
        # self.pushButton_11.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";")
        # self.pushButton_11.setObjectName("pushButton_11")
        #
        # self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_12.setGeometry(QtCore.QRect(845, 315, 209, 50))
        # self.pushButton_12.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";")
        # self.pushButton_12.setObjectName("pushButton_12")
        #
        # self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_13.setGeometry(QtCore.QRect(845, 380, 209, 50))
        # self.pushButton_13.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";")
        # self.pushButton_13.setObjectName("pushButton_13")



        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 120, 775, 535))
        self.graphicsView.setObjectName("graphicsView")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 117, 105, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 117, 105, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(495, 117, 105, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(625, 117, 105, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(625, 540, 105, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")


        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(495, 540, 105, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 540, 105, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 540, 105, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 42, 200, 40))
        self.label_9.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    # def current_text_changed(self, text):
    #     lbl = self.myDict[text[-3:]]
    #     for i, l in enumerate(self.labels):
    #         l.setText(lbl[i])


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        self.comboBox.setItemText(0, _translate("MainWindow", "секция 110"))
        self.comboBox.setItemText(1, _translate("MainWindow", "секция 210"))
        self.comboBox.setItemText(2, _translate("MainWindow", "секция 120"))
        self.comboBox.setItemText(3, _translate("MainWindow", "секция 220"))
        self.comboBox.setItemText(4, _translate("MainWindow", "секция 130"))
        self.comboBox.setItemText(5, _translate("MainWindow", "секция 230"))
        self.comboBox.setItemText(6, _translate("MainWindow", "секция 140"))
        self.comboBox.setItemText(7, _translate("MainWindow", "секция 240"))
        self.comboBox.setItemText(8, _translate("MainWindow", "секция 150"))
        self.comboBox.setItemText(9, _translate("MainWindow", "секция 250"))
        self.comboBox.setItemText(10, _translate("MainWindow", "секция 160"))
        self.comboBox.setItemText(11, _translate("MainWindow", "секция 260"))
        self.comboBox.setItemText(12, _translate("MainWindow", "секция 170"))
        self.comboBox.setItemText(13, _translate("MainWindow", "секция 270"))
        self.comboBox.setItemText(14, _translate("MainWindow", "секция 180"))
        self.comboBox.setItemText(15, _translate("MainWindow", "секция 280"))
        self.comboBox.setItemText(16, _translate("MainWindow", "секция 190"))
        self.comboBox.setItemText(17, _translate("MainWindow", "секция 290"))



        self.pushButton_4.setText(_translate("MainWindow", "Выход"))
        self.pushButton_7.setText(_translate("MainWindow", "Студенты"))
        # self.pushButton_9.setText(_translate("MainWindow", "Комменданты"))
        # self.pushButton_10.setText(_translate("MainWindow", "Проживание"))
        # self.pushButton_11.setText(_translate("MainWindow", "Комнаты"))
        # self.pushButton_12.setText(_translate("MainWindow", "Секции"))
        # self.pushButton_13.setText(_translate("MainWindow", "Корпусы"))
        self.label.setText(_translate("MainWindow", "Комната 131"))
        self.label_2.setText(_translate("MainWindow", "Комната 132"))
        self.label_3.setText(_translate("MainWindow", "Комната 133"))
        self.label_4.setText(_translate("MainWindow", "Комната 134"))
        self.label_5.setText(_translate("MainWindow", "Комната 135"))
        self.label_6.setText(_translate("MainWindow", "Комната 136"))
        self.label_7.setText(_translate("MainWindow", "Комната 137"))
        self.label_8.setText(_translate("MainWindow", "Комната 138"))
        self.label_9.setText(_translate("MainWindow", "Выбор секции"))