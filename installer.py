import os
from shutil import copy2 as copy_file

my_path = os.path.dirname(os.path.abspath(__file__))
themes_folder_location = os.getenv('AppData') + "\\BetterDiscord\\themes"

if not os.path.isdir(themes_folder_location):
    print('Automatic setup failed. Please enter the full path to your "themes" folder:')
    themes_folder_location = input()

for x in (
    "demo.theme.css",
    "demo.theme.css.header",
    "demo.theme.scss"
):copy_file(my_path + f"\\demo\\{x}", themes_folder_location + f"\\{x}")

with open(themes_folder_location + "\\run_DBS.bat","w") as f:
    f.write(f"@echo off && python {my_path}\\main.py")
