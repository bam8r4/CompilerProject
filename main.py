from treeFunctions import *
from parser import *
from staticSemantics import *
from comp import *

root = parser()

statSemDriver(root)

with open("temp.txt", "w") as f1:
        
    codeGenerator(root, f1)
    
if(kbInput == True):
    
    copyFile("temp.txt","kb.asm")
    
else:
    copyFile("temp.txt",inFileName)
    
    

