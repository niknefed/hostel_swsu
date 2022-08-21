from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlTableModel
from lodgers import Ui_lodgers


class Lodgers(QtWidgets.QMainWindow, Ui_lodgers):
    def __init__(self, parent=None):
        super(Lodgers, self).__init__(parent)
        self.setupUi(self)

        sdb = QSqlDatabase.addDatabase('QSQLITE')
        sdb.setDatabaseName('baza.db')
        sdb.open()
        self.model = QSqlTableModel(db=sdb)
        self.model.setTable("users")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()

        self.tableView_1.setModel(self.model)

        self.rоом_beds = []


        self.pushButton_9.clicked.connect(self.on_add_record)  # Добавить запись
        self.pushButton_10.clicked.connect(self.on_del_record)  # Удалить запись

    def on_add_record(self):
        row = self.tableView_1.selectionModel().currentIndex().row()
        if self.tableView_1.selectionModel().currentIndex().row() == -1:
            row = 0
            self.model.insertRow(row)
        else:
            row = row + 1
            self.model.insertRow(row)

        self.model.setData(self.model.index(row, 0), 'ФИО NEW')
        self.model.setData(self.model.index(row, 1), '0000')
        self.model.setData(self.model.index(row, 2), '0')
        self.model.setData(self.model.index(row, 3), '0')
        self.model.submit()

    def on_del_record(self):
        self.model.removeRow(self.tableView_1.currentIndex().row())
        self.model.select()



    def _getRooms(self):
        self.rоом_beds = []
        for row in range(self.model.rowCount()):
            if self.model.data(self.model.index(row, 2)) == 1:
                rоом_bed = str(self.model.data(
                    self.model.index(row, 1)))[:3], \
                           str(self.model.data(self.model.index(row, 1)))[3]
                self.rоом_beds.append(rоом_bed)

