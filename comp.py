from staticSemantics import *

TempVarCntr=[0]
TempLabCntr=[0]
#static VarCntr=0;
def incrementTempLabCntr():
    #global TempLabCntr
    
    TempLabCntr[0]=TempLabCntr[0]+1

def incrementTempVarCntr():
    #global TempVarCntr
    
    TempVarCntr[0]=TempVarCntr[0]+1 
    
#Counters and functions to ensure we allocate storage correctly and change tags/labels.    
VarCNTR = 0
LabCNTR = 0
def retTempVar():
    VarCNTR = TempVarCntr[0]
    incrementTempVarCntr()
    value = "T"+str(VarCNTR)
    return value
    
def retTempLab():
    LabCNTR = TempLabCntr[0]
    incrementTempLabCntr()
    label = "L"+str(LabCNTR)
    return label

def codeGenerator(root, f1):
    global ST
    
    if(root.label == "<program>"):
        
        #codeGenerator(root.left, f1)
        codeGenerator(root.right, f1)
        
        f1.write("STOP\n")
        
        for x in range(0,len(ST)):
            f1.write(str(ST[x].ident)+" 0\n")
        
        for x in range(0,TempVarCntr[0]):
            f1.write("T"+str(x)+" 0\n")
        
    elif(root.label == "<block>"):
        
        codeGenerator(root.left,f1)
        codeGenerator(root.right,f1)
        
        return
    
    elif(root.label == "<vars>"):
        if root.ident:
            if root.integer:
                
                f1.write("LOAD "+str(root.integer)+"\n")
                f1.write("STORE "+str(root.ident)+"\n")
        else:
            return
        
        if root.left:
            codeGenerator(root.left, f1)
        
        return
    
    elif(root.label == "<stats>"):
        
        codeGenerator(root.left, f1)
        codeGenerator(root.right, f1)
        
        return
        
    
    elif(root.label == "<mStat>"):
        
        if root.left:
            if root.right:
                codeGenerator(root.left,f1)
                codeGenerator(root.right,f1)
            
        else:
            
            return
                
    
    elif(root.label == "<stat>"):
        
        codeGenerator(root.left, f1)
        
    elif(root.label == "<in>"):
        
        #value = retTempVar()
        f1.write("READ "+str(root.ident)+"\n")
        f1.write("LOAD "+str(root.ident)+"\n")
        f1.write("STORE "+str(root.ident)+"\n")
        
        
        if root.left:
            codeGenerator(root.left, f1)
            
        if root.right:
            (codeGenerator,f1)
        
        return
    
    elif(root.label == "<out>"):
        
        codeGenerator(root.left, f1)
        value = retTempVar()
        f1.write("STORE "+str(value)+"\n")
        f1.write("WRITE "+str(value)+"\n")
        
        
    elif(root.label == "<if>"):
        codeGenerator(root.child3,f1)
        value = retTempVar()
        f1.write("STORE "+str(value)+"\n")
        codeGenerator(root.left,f1)
        f1.write("SUB "+str(value)+"\n")
        tempLabel = retTempLab()
        
        if(root.right.value == "=="):
            f1.write("BRNEG "+str(tempLabel)+"\n")
            f1.write("BRPOS "+str(tempLabel)+"\n")
        elif(root.right.value == "<"):
            f1.write("BRZERO "+str(tempLabel)+"\n")
            f1.write("BRPOS "+str(tempLabel)+"\n")
        elif(root.right.value == ">"):
            f1.write("BRZERO "+str(tempLabel)+"\n")
            f1.write("BRNEG "+str(tempLabel)+"\n")
        elif(root.right.value == "< <"):
            f1.write("BRPOS "+str(tempLabel)+"\n")
        elif(root.right.value == "> >"):
            f1.write("BRNEG "+str(tempLabel)+"\n")
        elif(root.right.value == "< >"):
            f1.write("BRZERO "+str(tempLabel)+"\n")
            
        codeGenerator(root.child4,f1)
            
        f1.write(str(tempLabel)+": NOOP\n")
        return
        
    elif(root.label == "<loop>"):
        
        tempLabel1 = retTempLab()
        f1.write(str(tempLabel1)+": NOOP\n")
        
        codeGenerator(root.child3,f1)
        value = retTempVar()
        f1.write("STORE "+str(value)+"\n")
        codeGenerator(root.left,f1)
        f1.write("SUB "+str(value)+"\n")
        tempLabel2 = retTempLab()
        
        if(root.right.value == "=="):
            f1.write("BRNEG "+str(tempLabel2)+"\n")
            f1.write("BRPOS "+str(tempLabel2)+"\n")
        elif(root.right.value == "<"):
            f1.write("BRZERO "+str(tempLabel2)+"\n")
            f1.write("BRPOS "+str(tempLabel2)+"\n")
        elif(root.right.value == ">"):
            f1.write("BRZERO "+str(tempLabel2)+"\n")
            f1.write("BRNEG "+str(tempLabel2)+"\n")
        elif(root.right.value == "< <"):
            f1.write("BRPOS "+str(tempLabel2)+"\n")
        elif(root.right.value == "> >"):
            f1.write("BRNEG "+str(tempLabel2)+"\n")
        elif(root.right.value == "< >"):
            f1.write("BRZERO "+str(tempLabel2)+"\n")
            
        codeGenerator(root.child4, f1)
        f1.write("BR "+str(tempLabel1)+"\n")
        f1.write(str(tempLabel2)+": NOOP\n")
        return
        
    elif(root.label == "<assign>"):
        codeGenerator(root.left, f1)
        
        f1.write("STORE "+str(root.ident)+"\n")
        return
    
    elif(root.label == "<expr>"):
        
        if root.left:
            if root.right:
                
                codeGenerator(root.right, f1)
                value = retTempVar()
                
                f1.write("STORE "+str(value)+"\n")
                codeGenerator(root.left, f1)
                f1.write("SUB "+str(value)+"\n")
                
                return
            
            else:
                
                codeGenerator(root.left, f1)
                
                return
        return
        
        
    elif(root.label == "<N>"):
        #Need to check this
        if root.left.left.left:
        
            if root.right:
                codeGenerator(root.right, f1)
                value = retTempVar()
                
                #Error begins here
                f1.write("STORE "+str(value)+"\n")
                codeGenerator(root.left, f1)
                    
                if(root.value == "/"):
                    f1.write("DIV "+str(value)+"\n")
                else:
                    f1.write("MULT "+str(value)+"\n")
                        
                return
            codeGenerator(root.left, f1)
            
        return
        
        
    
    elif(root.label == "<A>"):
        
        if root.left:
            if root.right:
                
                codeGenerator(root.right, f1)
                value = retTempVar()
                
                f1.write("STORE "+str(value)+"\n")
                codeGenerator(root.left, f1)
                f1.write("ADD "+str(value)+"\n")
                
                return
            
            else:
                codeGenerator(root.left, f1)
                
                return
        return
    
    
    elif(root.label == "<M>"):
        
        if root.left:
        
            if(root.value == "*"):
                codeGenerator(root.left, f1)
                
                f1.write("MULT -1\n")
                
                return
            else:
                codeGenerator(root.left, f1)
                return
        
        return
        
     
    elif(root.label == "<R>"):
        
        if root.left:
            codeGenerator(root.left, f1)
            return
        
        if root.integer:
            f1.write("LOAD "+str(root.integer)+"\n")
            return
            
        if root.ident:
            f1.write("LOAD "+str(root.ident)+"\n")
            return
        return
    
    else:
        print("Welp")
        return
            
