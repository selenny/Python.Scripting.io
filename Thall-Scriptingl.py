#!/user/bin/python
# Python Ver:     2.7
#
# Author:	      Terri Hall
#
# Purpose:	       Create a program that checks a folder for changes in .txt files, then copying those changed files to a second folder.
#
# Tested OS:       This code was written and tested to work with Windows 10.
 

import shutil
import os

def checkFiles(src):
    if lastFileUpdate == true:
        shutil.move(src + '/' + file, desc)
    else:
        print "No files were updated today"

def main():
    src = 'C:\Users\webde\Desktop\FolderA'
    dest = 'C:\Users\webde\Desktop\FolderB'
    print src
    print dest
    lastFileUpdate = os.path.getmtime(src, dest)
    print (lastFileUpdate ('Were moved to Folder B'))
    checkFiles(src)




               
