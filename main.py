from PyQt5 import QtWidgets


class MyApp(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__()

        self.setWindowTitle("Hello World")
