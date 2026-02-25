from PyQt5 import QtWidgets
import sys 
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazı_alanı = QtWidgets.QLineEdit()
        self.yazi_alani = QtWidgets.QLabel("bana henüz tıklanmadı")
        self.buton = QtWidgets.QPushButton("bana tıklayınız")
        self.say = 0

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.yazı_alanı)
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.buton.clicked.connect(self.click)
        self.show()

    def click(self):
        self.say += 1
        
        if self.say > 10:
            self.yazi_alani.setText("yeter daa ne ki... " + str(self.say) +  " kere tıklama yetmedi mi")
        else:
            self.yazi_alani.setText("bana " + str(self.say) + " defa tıklandı.")


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())