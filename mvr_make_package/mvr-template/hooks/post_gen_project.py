import os
import shutil

for root, dirs, _ in os.walk(".", topdown=False):
    for name in dirs:
        if name != "__pycache__":
            continue
        shutil.rmtree(os.path.join(root, name))
