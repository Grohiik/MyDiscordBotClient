import sys
import asyncio
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Ui_MainWindow import Ui_MainWindow
import time
import Bot

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.send.clicked.connect(self.on_button)

        self.myThread = DiscordThread()
        self.myThread.start()


#    def on_button(self):


    #def add_to_msgs(self, text):
     #   self.msg_window.append(text)


class DiscordThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

 
    def run(self):
        #loop = asyncio.get_event_loop()
        #loop.create_task(Bot.client.start(Bot.TOKEN))
        #loop.run_forever()
        asyncio.run(Bot.client.start(Bot.TOKEN))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())