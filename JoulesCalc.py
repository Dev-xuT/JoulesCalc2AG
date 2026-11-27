#!/usr/bin/python3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
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
        self.setFixedSize(420, 320)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(14)

        form = QFormLayout()
        form.setSpacing(12)

        self.peso = QLineEdit()
        self.peso.setPlaceholderText("Ex.: 18,13")
        self.peso.setClearButtonEnabled(True)
        self.peso.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.velocidade = QLineEdit()
        self.velocidade.setPlaceholderText("Ex.: 250")
        self.velocidade.setClearButtonEnabled(True)
        self.velocidade.setAlignment(Qt.AlignmentFlag.AlignRight)

        form.addRow("Peso do projétil (grains):", self.peso)
        form.addRow("Velocidade (m/s):", self.velocidade)
        layout.addLayout(form)

        self.resultado = QLineEdit()
        self.resultado.setReadOnly(True)
        self.resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resultado.setPlaceholderText("Informe peso e velocidade")
        self.resultado.setMinimumHeight(58)
        self.resultado.setStyleSheet(
            "QLineEdit {"
            "font-size: 20px;"
            "font-weight: bold;"
            "color: #e67e22;"
            "padding: 4px 8px;"
            "}"
        )
        layout.addWidget(self.resultado)

        limpar = QPushButton("Limpar")
        limpar.clicked.connect(self.limpar_campos)
        layout.addWidget(limpar)

        self.peso.textChanged.connect(self.calcular_joules)
        self.velocidade.textChanged.connect(self.calcular_joules)

        self.setCentralWidget(container)

    @staticmethod
    def converter_numero(texto):
        # Aceita vírgula ou ponto como separador decimal.
        return float(texto.strip().replace(",", "."))

    def calcular_joules(self):
        peso_texto = self.peso.text().strip()
        velocidade_texto = self.velocidade.text().strip()

        if not peso_texto or not velocidade_texto:
            self.resultado.clear()
            return

        try:
            peso = self.converter_numero(peso_texto)
            velocidade = self.converter_numero(velocidade_texto)
        except ValueError:
            self.resultado.setText("Verifique os valores")
            return

        if peso <= 0 or velocidade <= 0:
            self.resultado.setText("Valores devem ser maiores que zero")
            return

        joules = peso * velocidade * velocidade / 30860
        self.resultado.setText(f"{joules:.2f} J")

    def limpar_campos(self):
        self.peso.clear()
        self.velocidade.clear()
        self.resultado.clear()
        self.peso.setFocus()


def main():
    app = QApplication(sys.argv)
    window = JoulesCalculator()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
