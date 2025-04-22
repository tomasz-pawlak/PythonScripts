import os
import stat
from pathlib import Path

extensions = [".exe", ".js", ".scr", ".vbs", ".bat", ".cmd", ".ps1"]
keywords = ["invoice", "password", "login", "bank", "report"]


def is_hidden(filepath: Path) -> bool:
    if os.name == 'nt':
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


def scan_directory(directory: str):
    directory = Path(directory)
    suspicious_filenames = []

    if not directory.is_dir():
        print(f"{directory} is not a directory")
        return

    for root, _, files in os.walk(directory):
        for file in files:
            full_path = Path(root) / file
            if is_suspicious(full_path):
                suspicious_filenames.append(full_path)

    if suspicious_filenames:
        print("\nSuspicious file:")
        for file in suspicious_filenames:
            print(file)
    else:
        print(f"\n No suspicious file in directory {directory}")


scan_directory("")
