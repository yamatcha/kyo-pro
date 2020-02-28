import glob
import os
import shutil
files = glob.glob("./0*")
s=set()
for file in files:
    dir = "../"+file[:5].split("/")[1]+"abc"
    shutil.move(file,dir)