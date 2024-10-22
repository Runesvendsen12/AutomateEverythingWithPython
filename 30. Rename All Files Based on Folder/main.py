from pathlib import Path

root_dir = Path("30. Rename All Files Based on Folder/files")
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        print(path)