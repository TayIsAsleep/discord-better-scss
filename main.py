import os
import traceback
from time import sleep

# Code from https://stackoverflow.com/a/5917395/13921835
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

# Gets all of the .header files
header_files = [x for x in os.listdir() if x.endswith(".header")]

if len(header_files) == 0:
    input("No .header files found!\nPress Enter to exit.")
    exit()

# Prepare all the information we will need
work = []
for x in header_files:
    this_work = {}

    this_work['filename'] = x.split(".header")[0]
    this_work['header_filename'] = x
    
    with open(x, "r") as f:
        this_work['header'] = f.read()
    
    work.append(this_work)

# Run the main script
print("headers are being added...")
try:
    while 1:
        for x in work:
            try:
                with open(this_work['filename'], "r") as f:
                    first_line = f.readline().strip("\n")
                
                if first_line != this_work['header']:
                    line_prepender(this_work['filename'], this_work['header'])
            except Exception:
                traceback.print_exc()
                pass

        sleep(0.2)
except KeyboardInterrupt:
    print("Stopping...")
    exit()
except Exception:
    traceback.print_exc()
    pass

# Uh oh...
input("If you are reading this, then that means that something went really wrong...")
