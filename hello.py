import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle('Hello world')
    w.show()
    sys.exit(app.exec_())
    pass
if __name__ == "__main__":
    main()