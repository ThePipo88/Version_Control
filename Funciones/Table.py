

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        # Show widget
        self.show()

    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  


"""import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHeaderView, QAbstractItemView, QPushButton, QTableWidget, \
                            QTableWidgetItem, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__(1, 5)
        self.setHorizontalHeaderLabels(list('ABCDE'))
        self.verticalHeader().setDefaultSectionSize(50)
        self.horizontalHeader().setDefaultSectionSize(250)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount )

    def _removeRow(self):
        if self.rowCount() > 0:
            self.removeRow(self.rowCount()-1)

    def _copyRow(self):
        self.insertRow(self.rowCount())
        rowCount = self.rowCount()
        columnCount = self.columnCount()

        for j in range(columnCount):
            if not self.item(rowCount-2, j) is None:
                self.setItem(rowCount-1, j, QTableWidgetItem(self.item(rowCount-2, j).text()))


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 600)

        mainLayout = QHBoxLayout()
        table = TableWidget()
        mainLayout.addWidget(table)
        buttonLayout = QVBoxLayout()

        button_new = QPushButton('New')
        button_new.clicked.connect(table._addRow)
        buttonLayout.addWidget(button_new)

        button_copy = QPushButton('Copy')
        button_copy.clicked.connect(table._copyRow)
        buttonLayout.addWidget(button_copy)

        button_remove = QPushButton('Remove')
        button_remove.clicked.connect(table._removeRow)
        buttonLayout.addWidget(button_remove, alignment=Qt.AlignTop)

        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)

app = QApplication(sys.argv)
app.setStyleSheet('QPushButton{font-size: 20px; width: 200px; height: 50px}')   
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
"""