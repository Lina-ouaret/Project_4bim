

#### Premier test unitaire !!!!
import pathlib
from pathlib import Path
home = Path.home()
print(home)
cwd = Path.cwd()
cwd
target_dir = cwd / "test"
initial_count=0
for file in target_dir.iterdir():
    if file.suffix == ".png" :
        initial_count+=1
    #print(file)
print(initial_count)

wave = Path("test")
initial_count = 0
for nb in Path("test").glob("*.PNG"):
    initial_count += 1
print(initial_count)

for txt_path in Path("test").glob("*.jpg"):
    print(txt_path)


initial_count = 0
for path in pathlib.Path("test").iterdir():
    if path.is_file():
        initial_count += 1

print(initial_count)
