import re
import os
from datetime import datetime
import shutil


def find(key, in_directory=None, out_directory=None):
    if in_directory is not None and in_directory[-1] != '/':
        in_directory += "/"
    if out_directory is not None and out_directory[-1] != '/':
        out_directory += "/"
    if in_directory is None:
        in_directory = "./"
    if out_directory is None:
        current_time = datetime.now().strftime("%d%m%Y_%H%M%S")
        out_directory = f'./result{current_time}/'
    if not os.path.exists(out_directory):
        os.mkdir(out_directory)
    n_files = 0
    for file in os.listdir(in_directory):
        if os.path.isfile(f"{in_directory}{file}"):
            with open(f"{in_directory}{file}", "r", encoding="utf-8") as f:
                text = f.read()
                pattern = f"\s+{key}\s+"
                match = re.findall(pattern, text, flags=re.IGNORECASE)
                if len(match) != 0:
                    n_files += 1
                    shutil.copy(f"{in_directory}{file}",
                                f"{out_directory}{file}")
    if n_files == 0:
        print("No files found!")
    else:
        print(f"Results : {out_directory}")
