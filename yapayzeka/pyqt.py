import sys
from PyQt5 import QtWidgets,QtGui
def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 1")
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("buton")
    buton.move(350,150)
    etiket = QtWidgets.QLabel(pencere)
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setPixmap(QtGui.QPixmap("indir.jpg"))
    etiket.setText("Ahmet Yavuz un sayfasına hoşgeldiniz")
    etiket.move(300,30)
    pencere.setGeometry(800,300,600,600)
    pencere.show()
    sys.exit(app.exec_())
Pencere()