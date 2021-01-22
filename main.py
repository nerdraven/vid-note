import sys

from PyQt5 import QtWidgets


class MyApp(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__()

        self.setWindowTitle("Hello World")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = MyApp()
    window.show()

    sys.exit(app.exec_())
