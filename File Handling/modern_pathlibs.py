# object oriented pathlib, modern and cleaner way to work with paths
from pathlib import Path

file_path = Path("hello.txt")

print(file_path.exists())
print(file_path.is_file()) # ky given path ek file haii?
print(file_path.is_dir()) # ky given path ek folder haii
print(file_path.stat().st_size) # stat file ke baare mai metadata aur information deta haiii