# Aplicativo Linux — JoulesCalc2AG

Este repositório contém uma calculadora gráfica em Python/Qt6 para estimar a energia em joules com base na massa do projétil em grains e na velocidade em m/s.

## Compilar e instalar

A compilação deve ser feita no próprio Linux onde o aplicativo será usado (PyInstaller não é um compilador cruzado). Requer Python 3 e `venv`; não é necessário acesso de administrador.

```bash
chmod +x build_linux.sh install_linux.sh
./build_linux.sh
./install_linux.sh
```

O primeiro script cria um ambiente virtual local, instala PyQt6 e PyInstaller e gera `dist/joulescalc`. O segundo instala o executável em `~/.local/bin` e cria uma entrada no menu em `~/.local/share/applications`.

Também é possível iniciar diretamente com `./dist/joulescalc`. Para remover a instalação do usuário:

```bash
rm -f ~/.local/bin/joulescalc ~/.local/share/applications/joulescalc.desktop
```

O executável é construído para a distribuição e arquitetura Linux em uso; para distribuir em outros sistemas, compile separadamente em cada ambiente de destino.
