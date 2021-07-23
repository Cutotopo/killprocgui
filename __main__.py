import os
import sys
import subprocess
from PyQt5 import Qt
from PyQt5.QtCore import Qt, center
from PyQt5.QtGui import QPalette, QTextBlock, QTextLine
from PyQt5.QtWidgets import *

def getpnm():
    currentText = processLineEdit.text()
    return currentText

def killas():
    # if checkbox is checked run as root.
    checked = sudocb.isChecked()
    checkedl = str(checked).lower()
    return checkedl

def tbReturnPressed():
    killproc(processLineEdit.text())


def killproc(procname):
    # KillProc is available at https://github.com/Cutotopo/killproc
    if procname:
        try:
            if (killas() == 'true'):
                pidlist = str((str(subprocess.check_output(["pidof",procname])).lstrip("b'").rstrip("'n\\"))).split(' ')
                for pid in pidlist:
                    os.system(f'sudo kill {pid}')
                alert3 = QMessageBox()
                alert3.setWindowTitle('Success')
                alert3.setText(f'The process {procname} was successfully killed.')
                alert3.exec()
            else:
                pidlist = str((str(subprocess.check_output(["pidof",procname])).lstrip("b'").rstrip("'n\\"))).split(' ')
                for pid in pidlist:
                    os.system(f'kill {pid}')
                alert4 = QMessageBox()
                alert4.setWindowTitle('Success')
                alert4.setText(f'The process {procname} was successfully killed.')
                alert4.exec()
        except subprocess.CalledProcessError:
            alert1 = QMessageBox()
            alert1.setWindowTitle('Error')
            alert1.setText(f'The process {procname} doesn\'t exist or is not running.')
            alert1.exec()
    else:
        alert2 = QMessageBox()
        alert2.setWindowTitle('Error')
        alert2.setText('Please type the process\' name.')
        alert2.exec()

def buttonClick():
    killproc(getpnm())


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

headerLabel = QLabel()
headerLabel.setText("KillProcGUI")
headerLabel.setAlignment(Qt.AlignCenter)
layout.addWidget(headerLabel)

processLineEdit = QLineEdit()
processLineEdit.setPlaceholderText('Process name')
processLineEdit.returnPressed.connect(tbReturnPressed)
layout.addWidget(processLineEdit)

sudocb = QCheckBox()
sudocb.setText('Kill as root')
layout.addWidget(sudocb)

killBtn = QPushButton()
killBtn.setText('Kill process')
killBtn.clicked.connect(buttonClick)
layout.addWidget(killBtn)

window.setLayout(layout)
window.setWindowTitle('KillProc GUI')
window.show()
app.exec()



