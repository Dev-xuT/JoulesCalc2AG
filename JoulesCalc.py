#!/usr/bin/python3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class JoulesCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora de Joules")
        self.setFixedSize(420, 300)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        form = QFormLayout()
        form.setSpacing(15)

        self.peso = QDoubleSpinBox()
        self.peso.setRange(0, 100000)
        self.peso.setDecimals(2)
        self.peso.setSuffix(" grains")

        self.velocidade = QDoubleSpinBox()
        self.velocidade.setRange(0, 10000)
        self.velocidade.setDecimals(2)
        self.velocidade.setSuffix(" m/s")

        form.addRow("Peso do projétil:", self.peso)
        form.addRow("Velocidade:", self.velocidade)
        layout.addLayout(form)

        self.resultado = QLineEdit()
        self.resultado.setReadOnly(True)
        self.resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resultado.setText("0.00 J")
        self.resultado.setStyleSheet(
            "font-size: 28px;"
            "font-weight: bold;"
            "color: #e67e22;"
            "padding: 15px;"
        )
        layout.addWidget(self.resultado)

        calcular = QPushButton("Calcular")
        calcular.setDefault(True)
        calcular.setStyleSheet("font-size: 16px; padding: 10px;")
        calcular.clicked.connect(self.calcular_joules)

        limpar = QPushButton("Limpar")
        limpar.clicked.connect(self.limpar_campos)

        layout.addWidget(calcular)
        layout.addWidget(limpar)

        self.peso.valueChanged.connect(self.calcular_joules)
        self.velocidade.valueChanged.connect(self.calcular_joules)

        self.setCentralWidget(container)

    def calcular_joules(self):
        peso = self.peso.value()
        velocidade = self.velocidade.value()

        if peso <= 0 or velocidade <= 0:
            self.resultado.setText("0.00 J")
            return

        joules = peso * velocidade * velocidade / 30860
        self.resultado.setText(f"{joules:.2f} J")

    def limpar_campos(self):
        self.peso.setValue(0)
        self.velocidade.setValue(0)
        self.resultado.setText("0.00 J")
        self.peso.setFocus()


def main():
    app = QApplication(sys.argv)
    window = JoulesCalculator()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
