import unittest

from PyQt5 import QtWidgets

from main import MyApp


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        app = QtWidgets.QApplication([])
        window = MyApp()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
