import sys
from parser import *
ST = []
truthTable = ["True"]

class STV:
    
    def __init__(self, ident, lineNum):
        self.ident = ident
        self.lineNum = lineNum
        
def verify(ident, lineNum):
    global ST
    
    verified = False
    
    for x in range(0,len(ST)):
        
        if(ident == ST[x].ident):
            verified = True
        
    if(verified == False):
        print("Static Semantic Error: Variable "+ident+" has been accessed before it was defined. Line Number: "+str(lineNum)+"\n")
        truthTable[0]="False"
    
    
def statSem(root):
    
    global ST
    global truthTable
    
    hasId = True
    
    if(root.ident == None):
        hasId = False
  
    if(hasId == True and root.label == "<vars>"):
        
        ident = root.ident
        lineNum = root.lineNumber
        
        for x in range(0,len(ST)):
            #Checking to see if the value we are defining has already been defined. 
            if(ident == ST[x].ident):
                print("Static Semantic Error: Data "+ST[x].ident+" has already been defined on line number "+str(ST[x].lineNum)+
                "\nProgram is attempting to redefine it on line: "+str(lineNum)+" which is not allowed.\n")
                truthTable[0]="False"
                
        else:
            
            #Creating another value to add to the ST list. 
            possSTV = STV(ident,lineNum)
            ST.append(possSTV)
            
    elif(hasId == True):
        ident = root.ident
        lineNum = root.lineNumber
        
        verify(ident, lineNum)
        
        
        
          
  
    if root.left:
        statSem(root.left) 
  
    if root.right:
        statSem(root.right)
        
    if root.child3:
        statSem(root.child3)
            
    if root.child4:
        statSem(root.child4)
        
        
def statSemDriver(root):
    global truthTable
    
    #print("Checking static semantics...\n")
    
    statSem(root)
    
    if(truthTable[0] == "False"):
        print("Above issues found with the static semantics. Need to be corrected. Exiting...")
        sys.exit()
    
    #print("Static Semantics are good.")
    
    
