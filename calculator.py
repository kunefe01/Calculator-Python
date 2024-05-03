import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QScrollArea, QPushButton


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(200, 200, 700, 300)  # Pencere boyutunu genişlettik
        self.initUI()
    
    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayı 1 : ")
        self.lbl_sayi1.move(50, 30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150, 30)
        self.txt_sayi1.resize(200, 32)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayı 2 : ")
        self.lbl_sayi2.move(50, 70)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150, 70)
        self.txt_sayi2.resize(200, 32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(50, 110)
        self.btn_topla.clicked.connect(self.topla)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Çıkar")
        self.btn_cikar.move(150, 110)
        self.btn_cikar.clicked.connect(self.cikar)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText("Çarp")
        self.btn_carp.move(250, 110)
        self.btn_carp.clicked.connect(self.carp)

        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText("Böl")
        self.btn_bol.move(350, 110)
        self.btn_bol.clicked.connect(self.bol)

        # Sonuç için etiket (label)
        self.lbl_sonuc = QLabel(self)
        self.lbl_sonuc.setText("")
        self.lbl_sonuc.move(50, 150)
        self.lbl_sonuc.resize(400, 30)

        # Kaydırma alanı oluştur
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(450, 0, 250, 300)  # Pencere boyutunu genişlettik
        self.scroll_area.setWidgetResizable(True)

        # İşlem geçmişi için bir widget oluştur
        self.history_widget = QtWidgets.QWidget()
        self.history_layout = QtWidgets.QVBoxLayout(self.history_widget)
        self.scroll_area.setWidget(self.history_widget)

        # Temizleme butonu
        self.btn_temizle = QPushButton(self)
        self.btn_temizle.setText("Temizle")
        self.btn_temizle.move(10, 250)
        self.btn_temizle.clicked.connect(self.temizle)

    def topla(self):
        sayi1 = int(self.txt_sayi1.text())
        sayi2 = int(self.txt_sayi2.text())
        sonuc = sayi1 + sayi2
        self.lbl_sonuc.setText(f"Toplam: {sonuc}")
        self.add_to_history(f"{sayi1} + {sayi2} = {sonuc}")

    def cikar(self):
        sayi1 = int(self.txt_sayi1.text())
        sayi2 = int(self.txt_sayi2.text())
        sonuc = sayi1 - sayi2
        self.lbl_sonuc.setText(f"Fark: {sonuc}")
        self.add_to_history(f"{sayi1} - {sayi2} = {sonuc}")

    def carp(self):
        sayi1 = int(self.txt_sayi1.text())
        sayi2 = int(self.txt_sayi2.text())
        sonuc = sayi1 * sayi2
        self.lbl_sonuc.setText(f"Çarpım: {sonuc}")
        self.add_to_history(f"{sayi1} * {sayi2} = {sonuc}")

    def bol(self):
        sayi1 = int(self.txt_sayi1.text())
        sayi2 = int(self.txt_sayi2.text())
        if sayi2 == 0:
            self.lbl_sonuc.setText("Bir sayıyı 0'a bölemezsiniz!")
            self.add_to_history(f"{sayi1} / {sayi2} = Hata: Bölen sıfır olamaz")
        else:
            sonuc = sayi1 / sayi2
            self.lbl_sonuc.setText(f"Bölüm: {sonuc}")
            self.add_to_history(f"{sayi1} / {sayi2} = {sonuc}")

    def add_to_history(self, text):
        label = QLabel(text)
        self.history_layout.addWidget(label)

    def temizle(self):
        for i in reversed(range(self.history_layout.count())):
            widget = self.history_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()


def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())


app()
