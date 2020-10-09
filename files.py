import os
import sys

kbInput = False
fileInput = False
inFileName = None

#Taknig an argument list and wrinting it to a file.
def writeToFile(file, list):
    with open(file, 'w') as f:
        for item in list:
            f.write("%s\n" % item)

#Checking to see if the input file is empty
def isFileEmpty(file):
    if os.path.getsize(file) == 0:
        return True
    else:
        return False

#Copy one file to another location.
def copyFile(fileIn, fileOut):
    with open(fileIn) as f:
        with open(fileOut, "w") as f1:
            for line in f:
                f1.write(line)
                
def printf(fileOut, phrase):
    with open(fileOut, "w") as f1:
        f1.write(phrase)
    
                
#Selection structure to see what situation were given.
if(len(sys.argv) == 1):
    kbInput = True
    inputString = raw_input("Please input a string by hand. Press enter when complete.\n")
    f = open('temp.txt', 'w')
    f.write(inputString)
    f.close()

elif(len(sys.argv) ==  2):
    janFile = str(sys.argv[1])
    janFile = janFile + ".sp2020"
    fileInput = True
    FileName = janFile
    FileName = FileName.rsplit( ".", 1 )
    inFileName = FileName[0]+".asm"
    copyFile(janFile,'temp.txt')

else:
    print("There was an unknown error. Please run the program again.")
    sys.exit()
'''
copyFile('test.txt','temp.txt')

#Exit if we are given a blank file or the user inputs no information.
if(isFileEmpty('temp.txt')):
    print("The file provided has no information.")
    sys.exit()'''
