from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MessageBoxs():
    def information(self, titulo, mensagem):
        self.msg = QMessageBox()
        self.msg.setWindowIcon(QIcon("images/moed.png"))
        self.msg.setWindowTitle(titulo)
        self.msg.setText(mensagem)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()

    @staticmethod
    def about(titulo, mensagem):
        msg = QMessageBox()
        msg.setWindowIcon(QIcon("images/moed.png"))
        msg.setWindowTitle(titulo)
        msg.setText(mensagem)
        msg.setIconPixmap(QPixmap("images/moed.png"))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def warning(self, titulo, mensagem):
        self.msg = QMessageBox()
        self.msg.setWindowIcon(QIcon("images/moed.png"))
        self.msg.setWindowTitle(titulo)
        self.msg.setText(mensagem)
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()

    @staticmethod
    def progress_dialog(titulo, lista):
        msg = QProgressDialog()
        msg.setWindowIcon(QIcon("images/moed.png"))
        msg.setWindowTitle(titulo)
        msg.setCancelButtonText("Cancelar")
        value = 0
        for a in lista:
            msg.setMaximum(len(lista))
            value = value + 1
            msg.setValue(value)
        #msg.autoClose()
        msg.show()


class TimerMessageBox(QMessageBox):
    def func(self, titulo, texto, timeout=3):
        self.setWindowTitle(titulo)
        self.setWindowIcon(QIcon("images/moed.png"))
        self.setIconPixmap(QPixmap("images/moed.png"))
        self.time_to_wait = timeout
        self.setText(texto)
        self.setStandardButtons(QMessageBox.Ok)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changeContent)
        self.timer.start()
        self.exec_()

    def changeContent(self):
        #self.setText("wait (closing automatically in {0} secondes.)".format(self.time_to_wait))
        self.time_to_wait -= 1
        if self.time_to_wait <= 0:
            self.close()

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()


