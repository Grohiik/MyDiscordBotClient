import sys
import asyncio
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Ui_MainWindow import Ui_MainWindow
import Bot


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # self.send.clicked.connect(self.on_button)
        self.threadpool = QtCore.QThreadPool()

        worker = Worker()
        self.threadpool.start(worker)


#    def on_button(self):


# def add_to_msgs(self, text):
#   self.msg_window.append(text)


class Worker(QtCore.QRunnable):
    """
    Worker thread
    """

    def __init__(self):
        super(Worker, self).__init__()
        self.loop = asyncio.get_event_loop()

    def run(self):
        self.loop.create_task(Bot.start())
        self.loop.run_forever()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())