import os
import stat
from pathlib import Path

extensions = ["exe", "js", "scr", "vbs", "bat", "cmd", "ps1"]
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

    if len(parts) > 2 and parts[-1] in extensions:
        return True
    else:
        return False

def is_suspicious(file: Path) -> bool:
    name = file.name.lower()
    ext = file.suffix.lower()
    return (
        ext in extensions or
        name in keywords or
        is_hidden(file) or
        has_double_extension(name)
    )

if is_suspicious(Path("")):
    print("Suspicious filename detected")
else:
    print("Suspicious filename undetected")
