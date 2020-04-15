import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def dialog():
    mbox = QMessageBox()

    mbox.setText("Your allegiance has been noted")
    ok = QMessageBox.Ok
    batal = QMessageBox.Cancel
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(ok | batal)
            
    mbox.exec_()

# def window():
#     # app = QApplication(sys.argv)
#     # widget = QWidget()
    

#     # textLabel = QLabel(widget)
#     # textLabel.setText("Hello")
#     # textLabel.move(110,110)

#     # widget.setGeometry(50,50,320,200)
#     # widget.setWindowTitle("PyQt5 Example")
#     # widget.show()
#     # sys.exit(app.exec_())
#     app = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(300,300)
#     w.setWindowTitle('Guru99')
    
#     label = QLabel(w)
#     label.setText("Behold the Guru, Guru99")
#     label.move(100,130)
#     label.show()

#     btn = QPushButton(w)
#     btn.setText('Beheld')
#     btn.move(110,150)
#     btn.show()
#     btn.clicked.connect(dialog)

if __name__ == '__main__':
#    window()
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle('Guru99')
    
    label = QLabel(w)
    label.setText("Behold the Guru, Guru99")
    label.move(100,130)
    label.show()

    btn = QPushButton(w)
    btn.setText('Beheld')
    btn.move(110,150)
    
    btn.show()
    btn.clicked.connect(dialog)
    w.show()
    sys.exit(app.exec_())
