import os
import stat
from pathlib import Path

extensions = [".exe", ".js", ".scr", ".vbs", ".bat", ".cmd", ".ps1"]
keywords = ["invoice", "password", "login", "bank", "report"]

def is_hidden(filepath: Path) -> bool:
    if os.path == 'nt':
        try:
            attrs = os.stat(filepath).st_file_attributes
            return bool(attrs & stat.FILE_ATTRIBUTE_HIDDEN)
        except AttributeError:
            return False
    else:
        return filepath.name.startswith(".")

def has_double_extension(filepath: str) -> bool:
    parts = filepath.split(".")
    if len(parts) < 2:
        print(parts)
        return False
    else:
        print(parts)
        return True

has_double_extension("tomek.exe")
