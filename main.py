import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.on_button_click)
        self.circles = []

    def on_button_click(self):
        x = random.randint(50, self.width() - 50)
        y = random.randint(50, self.height() - 50)
        diameter = random.randint(20, 100)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(255, 255, 0))
        for (x, y, diameter) in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())