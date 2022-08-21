import sys
from mainWindow import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
from getRooms import Lodgers
from Roms import Ui_Rooms


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.scene = QtWidgets.QGraphicsScene()
        self.setupUi(self)

        self.rоом_rect = {
            '131': 0,
            '132': 1,
            '133': 2,
            '134': 3,
            '135': 4,
            '136': 5,
            '137': 6,
            '138': 7,
        }


        self.lodgers = Lodgers()
        self.pushButton_7.clicked.connect(self.openlodgers)
        self.lodgers.pushButton_8.clicked.connect(self.returnMainWindow)

        # self.pushButton_11.clicked.connect(self.openrooms)

        self.pushButton_4.clicked.connect(self.close)
        self.scene.addPixmap(QtGui.QPixmap("section_sketch.png"))
        self.lodgers._getRooms()  # формирование списка self.lodgers.rоом_beds
        self.drowRooms()
        self.graphicsView.setScene(self.scene)

    # Метод для отрисовки
    def drowRooms(self):
        self.Rooms = []
        self.Rooms.append((
            # Рисование прямоугольников для 131 комнаты (обозначения для того чтобы в дальнеёшем присвоить прямоугольникам имя через список)
            self.scene.addRect(195, 40, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1311
            self.scene.addRect(240, 40, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1312
            self.scene.addRect(195, 85, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1313
            self.scene.addRect(240, 85, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green))))  # 1314
        self.Rooms.append((
            # Рисование прямоугольников для 132 комнаты (обозначения для того чтобы в дальнеёшем присвоить прямоугольникам имя)
            self.scene.addRect(330, 40, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1321
            self.scene.addRect(375, 40, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1322
            self.scene.addRect(330, 85, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1323
            self.scene.addRect(375, 85, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green))))  # 1324
        self.Rooms.append((
            # Рисование прямоугольников для 133 комнаты (обозначения для того чтобы в дальнеёшем присвоить прямоугольникам имя)
            self.scene.addRect(465, 40, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1331
            self.scene.addRect(510, 40, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1332
            self.scene.addRect(465, 85, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1333
            self.scene.addRect(510, 85, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green))))  # 1334
        self.Rooms.append((
            # Рисование прямоугольников для 134 комнаты (обозначения для того чтобы в дальнеёшем присвоить прямоугольникам имя)
            self.scene.addRect(595, 40, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1341
            self.scene.addRect(640, 40, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1342
            self.scene.addRect(595, 85, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1343
            self.scene.addRect(640, 85, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green))))  # 1344
        self.Rooms.append((
            # Рисование прямоугольников для 135 комнаты (обозначения для того чтобы в дальнеёшем присвоить прямоугольникам имя)
            self.scene.addRect(595, 320, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1351
            self.scene.addRect(640, 320, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1352
            self.scene.addRect(595, 365, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1353
            self.scene.addRect(640, 365, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green))))  # 1354
        self.Rooms.append((
            # Рисование прямоугольников для 136 комнаты (обозначения для того чтобы в дальнеёшем присвоить прямоугольникам имя)
            self.scene.addRect(465, 320, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1361
            self.scene.addRect(510, 320, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1362
            self.scene.addRect(465, 365, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1363
            self.scene.addRect(510, 365, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green))))  # 1364
        self.Rooms.append((
            # Рисование прямоугольников для 137 комнаты (обозначения для того чтобы в дальнеёшем присвоить прямоугольникам имя)
            self.scene.addRect(330, 320, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1371
            self.scene.addRect(375, 320, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1372
            self.scene.addRect(330, 365, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1373
            self.scene.addRect(375, 365, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green))))  # 1374
        self.Rooms.append((
            # Рисование прямоугольников для 138 комнаты (обозначения для того чтобы в дальнеёшем присвоить прямоугольникам имя)
            self.scene.addRect(195, 320, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1381
            self.scene.addRect(240, 320, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1382
            self.scene.addRect(195, 365, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green)),  # 1383
            self.scene.addRect(240, 365, 35, 35, pen=QtGui.QPen(Qt.black), brush=QtGui.QBrush(Qt.green))))  # 1384

        # список сформированный в новом классе
        for k, v in self.lodgers.rоом_beds:
            self.Rooms[self.rоом_rect[k]][int(v)].setBrush(QtGui.QBrush(Qt.red))

    def openrooms(self):
        self.hide()
        self.rooms.show()

    def openlodgers(self):
        self.hide()
        self.lodgers.show()

    # Функция для возвращения на главное окно (Из окна проживающие) по кнопке Назад
    def returnMainWindow(self):
        self.lodgers._getRooms()
        self.drowRooms()  # отрисовка
        self.lodgers._getRooms()  # формирование списка
        self.lodgers.close()
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())
