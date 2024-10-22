from pathlib import Path

root_dir = Path("C:/Users/rbs/OneDrive - Azend A S/Skrivebord/Tutorials/AutomateEverythingWithPython/29. Add Prefix to All Filenames in Folder/files")

file_paths = root_dir.iterdir()

for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    print(new_filepath)
    path.rename(new_filepath)