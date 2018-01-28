

#!/user/bin/python
# Python Ver:     2.7
#
# Author:	      Terri Hall
#
# Purpose:	       Create a program that checks a folder for changes in .txt files, then copying those changed files to a second folder.
#
# Tested OS:       This code was written and tested to work with Windows 10.
 

import shutil, os, sys, time

def main():
    src = 'C:\Users\webde\Desktop\FolderA'
    dest = 'C:\Users\webde\Desktop\FolderB'
    lastFileUpdate = os.path.getmtime(sourceFile)

listFile = os.listdir(src)
for files in listFile:
    if files.endswith(".txt"):
        sourceFile = os.path.join(src + files)  #This checks for mod time
    lastFileUpdate = os.path.getmtime(sourceFile)
    print (lastFileUpdate)

currentTime = time.time()
modTime = currentTime - lastFileUpdate  #time difference between current time and mod time

if modTime < 86400:
    shutil.move(sourceFile, dest)
    print (sourceFile + 'Was moved to FolderB')
else:
    print ("No files were updated today")
                
if __name__=='__main__':
    main()
               
