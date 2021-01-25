import sys

from PyQt5 import QtWidgets

from main import MyApp


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = MyApp()
    window.show()

    sys.exit(app.exec_())
