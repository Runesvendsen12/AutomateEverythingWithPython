from pathlib import Path

p1 = Path("C:/Users/rbs/OneDrive - Azend A S/Skrivebord/Tutorials/AutomateEverythingWithPython/28. Intro to Python Pathlib Library/Section 4 Working with Computer files and folders/files/ghi.txt")

if not p1.exists():
    with open(p1, 'w') as file:
        file.write('Content 3')

p2 = Path("C:/Users/rbs/OneDrive - Azend A S/Skrivebord/Tutorials/AutomateEverythingWithPython/28. Intro to Python Pathlib Library/Section 4 Working with Computer files and folders/files")
for item in p2.iterdir():
    print(item.name)