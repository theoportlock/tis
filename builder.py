import PyQt5.QtWidgets as Q
app = Q.QApplication([])
window = Q.QWidget()
layout = QVBoxLayout()
topbutton = Q.QPushButton('Top')
bottombutton = Q.QPushButton('Bottom')

def topclicked():
    alert = Q.QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

topbutton.clicked.connect(topclicked)
topbutton.show()
window.setLayout(layout)
window.show()
app.exec_()
