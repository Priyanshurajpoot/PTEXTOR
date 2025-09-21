# src/util.py
import sys
import os

def resource_path(relative_path):
    """Return the correct path for PyInstaller bundled files."""
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
