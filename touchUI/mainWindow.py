import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from touchUI import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()
    sys.exit()


if __name__ == '__main__':
    main()
