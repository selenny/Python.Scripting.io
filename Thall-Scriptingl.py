

#!/user/bin/python
# Python Ver:     2.7
#
# Author:	      Terri Hall
#
# Purpose:	       Create a program that checks a folder for changes in .txt files, then copying those changed files to a second folder.
#
# Tested OS:       This code was written and tested to work with Windows 10.
 

import shutil, os, time

def checkFileMove(src, dest):
    currentTime = time.time()
    
listFile = os.listdir(src)
for files in listFile:
    
    if files.endswith(".txt"):
        sourceFile = os.path.join(src + files)
        lastFileUpdate = os.path.getmtime(sourceFile)
        print (lastFileUpdate)
        modTime = currentTime - lastFileUpdate
        if modTime < 86400:
            shutil.move(sourceFile, dest)
            print (sourceFile + 'Was moved to FolderB')
        else:
            print ("No files were updated today")
    
def main():
    src = 'C:\Users\webde\Desktop\FolderA\\'
    dest = 'C:\Users\webde\Desktop\FolderB\\'
    checkFileMove(src, dest)
    
                
if __name__=='__main__':
    main()
               
