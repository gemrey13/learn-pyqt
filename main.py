import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My PyQt5 Application")
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello, PyQt5!", self)

        sampleImg = QLabel(self)
        sampleImg.setGeometry(0, 0, 250, 300)
        pixmap = QPixmap("test.png")
        sampleImg.setPixmap(pixmap)
        sampleImg.setScaledContents(True)

        sampleImg.setGeometry((self.width() - sampleImg.width()) // 2,
                              (self.height() - sampleImg.height()) // 2,
                             sampleImg.width(),
                             sampleImg.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()