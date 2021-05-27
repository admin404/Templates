import sys

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())