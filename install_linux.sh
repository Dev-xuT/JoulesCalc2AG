#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
APP="$ROOT_DIR/dist/joulescalc"
BIN_DIR="$HOME/.local/bin"
DESKTOP_DIR="$HOME/.local/share/applications"

if [[ ! -x "$APP" ]]; then
  echo "Linux app not found at: $APP" >&2
  echo "Build it first by running: ./build_linux.sh" >&2
  exit 1
fi

install -Dm755 "$APP" "$BIN_DIR/joulescalc"
mkdir -p "$DESKTOP_DIR"
cat > "$DESKTOP_DIR/joulescalc.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=Calculadora de Joules
Comment=Calcula a energia cinética em joules
Exec="$BIN_DIR/joulescalc"
TryExec=$BIN_DIR/joulescalc
Icon=accessories-calculator
Terminal=false
Categories=Utility;Education;
EOF
chmod 644 "$DESKTOP_DIR/joulescalc.desktop"

printf 'Instalado! Procure por “Calculadora de Joules” no menu de aplicativos.\n'
printf 'Executável: %s/joulescalc\n' "$BIN_DIR"
printf 'Para iniciar pelo terminal: %s/joulescalc\n' "$BIN_DIR"
