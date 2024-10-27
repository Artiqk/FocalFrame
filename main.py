from app.focal_frame import MainWindow
from PySide6 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()
    
    app.exec()