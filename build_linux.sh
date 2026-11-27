#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

python3 -m venv .venv-linux
.venv-linux/bin/python -m pip install --upgrade pip
.venv-linux/bin/python -m pip install -r requirements.txt pyinstaller

rm -rf build dist
.venv-linux/bin/pyinstaller \
  --clean \
  --noconfirm \
  --onefile \
  --windowed \
  --name joulescalc \
  JoulesCalc.py

printf '\nBuild complete: %s/dist/joulescalc\n' "$ROOT_DIR"
printf 'To install for your user, run: ./install_linux.sh\n'
