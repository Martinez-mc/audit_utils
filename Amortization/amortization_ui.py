import sys
from Amortization import amortize, compounder
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
QTextEdit, QLineEdit, QLabel, QPushButton, QGroupBox, QComboBox, QMessageBox, QRadioButton)

class mainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main App")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)







if __name__ == '__main__': 
    app = QApplication(sys.argv)
    window = mainApp()
    window.show()
    sys.exit(app.exec())   