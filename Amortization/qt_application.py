import sys
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
QTextEdit, QLineEdit, QLabel, QPushButton, QGroupBox, QComboBox, QMessageBox, QRadioButton, 
QScrollArea)

from Amortization import amortize, compounder

class Amortization(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Amortization")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout(central_widget)
        self.variables_layout = QVBoxLayout()
        self.container = QVBoxLayout()
        self.upper_layout = QHBoxLayout()

        # Input Zone
        # -----------------------------------------------------
        self.group_box = QGroupBox("Input Zone")
        self.group_box.setFixedWidth(250)

        # Radio Box
        self.radio_box = QGroupBox("Annuity")
        self.radio_box.setFixedWidth(200)
        self.radio_layout = QHBoxLayout()
        self.ordinary = QRadioButton("Ordinary")
        self.due = QRadioButton("Due")
        self.radio_layout.addWidget(self.ordinary)
        self.radio_layout.addWidget(self.due)
        self.radio_box.setLayout(self.radio_layout)
        self.ordinary.setChecked(True)
        self.variables_layout.addWidget(self.radio_box)
        
        # Compounding
        self.compounding_label = QLabel("Compounding")
        self.compounding = QComboBox()
        self.compounding.addItems(['Daily', 'Weekly', 'Monthly', 'Semi-Annual', 'Annual'])
        self.compounding.setCurrentIndex(2)
        self.compounding.currentIndexChanged.connect(self.recompute)

        self.variables_layout.addWidget(self.compounding_label)
        self.variables_layout.addWidget(self.compounding)

        # Start Date
        self.start_date_layout = QHBoxLayout()
        self.start_date_label = QLabel("Start Date")
        self.start_date_value = QLineEdit()
        self.start_date_value.setPlaceholderText('MM/DD/YYYY')
        self.start_date_value.setInputMask('99/99/9999;_')
        self.start_date_layout.addWidget(self.start_date_label)
        self.start_date_layout.addWidget(self.start_date_value)

        # End Date
        self.end_date_layout = QHBoxLayout()
        self.end_date_label = QLabel("End Date  ")
        self.end_date_value = QLineEdit()
        self.end_date_value.setPlaceholderText('MM/DD/YYY')
        self.end_date_value.setInputMask('99/99/9999;_')
        self.end_date_value.editingFinished.connect(self.get_periods)
        self.end_date_layout.addWidget(self.end_date_label)
        self.end_date_layout.addWidget(self.end_date_value)
        
        # Periods
        self.periods_layout = QHBoxLayout()
        self.periods_label = QLabel("Periods     ")
        self.periods_value = QLineEdit()
        self.periods_layout.addWidget(self.periods_label)
        self.periods_layout.addWidget(self.periods_value)

        # Principal
        self.principal_layout = QHBoxLayout()
        self.principal_label = QLabel('Principal   ')
        self.principal_value = QLineEdit()
        self.principal_layout.addWidget(self.principal_label)
        self.principal_layout.addWidget(self.principal_value)
        
        # Payment
        self.payment_layout = QHBoxLayout()
        self.payment_label = QLabel("Payment  ")
        self.payment_value = QLineEdit()
        self.payment_layout.addWidget(self.payment_label)
        self.payment_layout.addWidget(self.payment_value)

        # Rate
        self.rate_layout = QHBoxLayout()
        self.rate_label = QLabel("Rate           ")
        self.rate_value = QLineEdit()
        self.rate_layout.addWidget(self.rate_label)
        self.rate_layout.addWidget(self.rate_value)
        self.rate_value.editingFinished.connect(self.get_payment)

        # Buttons
        self.buttons_group_box = QGroupBox("Actions")
        self.button_layout = QVBoxLayout()
        self.amortization_btn = QPushButton('Amortize')
        self.amortization_btn.clicked.connect(self.set_table)
        self.clear_btn = QPushButton('Clear')
        self.clear_btn.clicked.connect(self.clear)
        self.button_layout.addWidget(self.amortization_btn)
        self.button_layout.addWidget(self.clear_btn)
        self.buttons_group_box.setLayout(self.button_layout)
        self.variables_layout.addLayout(self.button_layout)
        self.group_box.setLayout(self.variables_layout)

        self.display_group_box = QGroupBox('Display')
        self.display_label = QLabel("")
        self.display_layout = QHBoxLayout()
        self.display_layout.addWidget(self.display_label)
        self.display_group_box.setLayout(self.display_layout)

        # Results Section
        # ------------------------------------------------
        self.results_group_box = QGroupBox("Results")
        self.results_group_box.setFixedHeight(400)
        self.results_layout = QHBoxLayout()
        self.results_txt = QTextEdit()
        self.results_txt.setReadOnly(True)
        self.results_txt.setFixedHeight(300)
        #self.results_txt.setFixedWidth()
        self.results_layout.addWidget(self.results_txt)
        self.results_group_box.setLayout(self.results_layout)

        # Layouts
        self.variables_layout.addLayout(self.start_date_layout)
        self.variables_layout.addLayout(self.end_date_layout)
        self.variables_layout.addLayout(self.periods_layout)
        self.variables_layout.addLayout(self.principal_layout)
        self.variables_layout.addLayout(self.rate_layout)
        self.variables_layout.addLayout(self.payment_layout)

        self.container = QVBoxLayout()
        self.container.addWidget(self.group_box)
        self.container.addWidget(self.buttons_group_box)

        self.upper_layout.addLayout(self.container)
        self.upper_layout.addWidget(self.results_group_box)

        self.main_layout.addLayout(self.upper_layout)
        self.main_layout.addWidget(self.display_group_box)
        
        #ENDS QT Application
        # -----------------------------------------------------
    """
            # TEMP - DELETE AFTER TESTING -------------------
            start = '01/01/2024'
            end = '12/31/2028'
            principal = 5000
            rate = 9

            self.start_date_value.setText(start)
            self.end_date_value.setText(end)
            self.principal_value.setText(str(principal))
            self.rate_value.setText(str(rate))
            # -------------------------------------
    """

    def get_payment(self):
        start = self.start_date_value.text()
        periods = int(self.periods_value.text())
        comp = self.compounding.currentText()
        rate = float(self.rate_value.text()) / 100
        principal = float(self.principal_value.text())

        ann = ''
        if self.ordinary.isChecked():
            ann = 'Ordinary'
        else: 
            ann = 'Due'

        pmt = compounder(start, periods, comp, rate, ann, principal)
        self.payment_value.setText(str(f'{pmt[2]:.2f}'))
           
    def get_periods(self):
        end_date = datetime.strptime(self.end_date_value.text(), "%m/%d/%Y")
        start_date = datetime.strptime(self.start_date_value.text(), "%m/%d/%Y")
        days = (end_date - start_date).days
        
        if self.compounding.currentText() == 'Daily': 
            self.periods_value.setText(str(days))
        elif self.compounding.currentText() == 'Weekly':
            weeks = days // 7
            self.periods_value.setText(str(weeks))
        elif self.compounding.currentText() == 'Monthly':
            months = days // 30
            self.periods_value.setText(str(months))
        elif self.compounding.currentText() == 'Semi-Annual':
            semi_annual = days / 182
            self.periods_value.setText(str(f'{semi_annual:.0f}'))
        elif self.compounding.currentText() == 'Annual':
            years = days / 365.25
            self.periods_value.setText(str(f'{years:.0f}'))
    
    def set_table(self):
        
        start = self.start_date_value.text()
        periods = int(self.periods_value.text())
        comp = self.compounding.currentText()
        rate = float(self.rate_value.text()) / 100
        ann = self.ordinary.text()
        pmt = self.payment_value.text()
        principal = float(self.principal_value.text())

        amortization_table = amortize(start, periods, comp, rate, ann, pmt, principal)
        css_styles = """
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
                text-align: left;
            }
            tr:hover {
                background-color: #f5f5f5;
            }
        </style>
        """

        # Combine the CSS styles with the HTML content
        full_html_content = css_styles + amortization_table[1]
        self.results_txt.setHtml(full_html_content)
    
        def set_chart(amt):

            sns.set(style="whitegrid")
            plt.figure(figsize=(9, 4.5))
            sns.barplot(data=amt, x='Date', y='Balance', palette='Blues')
            plt.title('Amortized Balance', fontsize=20, fontweight='bold')
            plt.xlabel('Date', fontsize=14)
            plt.ylabel('Balance', fontsize=14)
            plt.xticks([])
            plt.grid(axis='y')
            plt.tight_layout()
            #plt.show()
            plt.savefig('plot.png', format='png')
            plt.close()

            pixmap = QPixmap('plot.png')
            self.display_label.setPixmap(pixmap)


        set_chart(amortization_table[0])
        print(amortization_table[0])
        

    def clear(self):
        self.results_txt.setText('')

    def recompute(self):
        try:
            self.get_periods()
            self.get_payment()
        except:
            pass

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    window = Amortization()
    window.show()
    sys.exit(app.exec())
