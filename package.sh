#!/usr/bin/env bash
rm -rf src/__pycache__/
rm -rf src/sketcher/__pycache__/
rm -rf src/sketcher/commands/__pycache__/
rm -rf src/sketcher/entities/__pycache__/
python -m zipapp -c src -o sketcher -p "/usr/bin/env python3"
