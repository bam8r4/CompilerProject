from scanner import *

#fix assign function and chekc loop func
scannerError = False

#This is so all functions can access the counter at the same level.
counter = [0]
tokenList = []


class token:
    
    def __init__(self, tkClass, lineNum, tkInstance):
        self.tkClass = tkClass
        self.tkInstance = tkInstance
        self.lineNum = lineNum
        
    def output(self):
        print("Value: "+ self.value + " Token Class: "+ self.tkClass + " Line Number: " + str(self.lineNum))
        
class Node: 
    def __init__(self,label,token,lineNumber): 
        self.left = None
        self.right = None
        self.child3 = None
        self.child4 = None
        self.value = None
        self.label = label 
        self.token = token
        self.lineNumber = lineNumber
        self.ident = None
        self.integer = None

def parser():
    global counter
    #print("Scanner was successful... starting parser.")
    root = program()
    count = counter[0]
    counter[0] = count + 1
    
    
    currentToken = tokenList[counter[0]].tkClass
    
    if(currentToken == "EOFtk"):
	   #print("Parse was successful \n")
           pass
    else:
	    print("Parse Error: Unexpected end of file.")
	    sys.exit()
	
    return root

def program():
    global counter
    count = counter[0]
    root = Node("<program>","voidTk", 1)
    
    if(root.token == "voidTk"):

	    #Set children
        root.left = var()
        root.right = block()
        
	
    else:
        print("Parse Error: Tree could not be established.")
        sys.exit()
    
    
    return root
   
def block():
    
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<block>", token , lineNumber)
    
    

    counter[0] = count + 1
    
    
    if(token == "beginTk"):
		
        node.left = var();
        node.right = stats();
        
        token = tokenList[counter[0]].tkClass
       
        if(token == "endTk"):
            
            return node;
        else:
           
            print("Parse Error: Unexpected end of file.")
            sys.exit()
    else:
        print("Parse Error: Expected beginTk but found: " + str(node.token) + " on line number: " + str(node.lineNumber))
        sys.exit()
    
    return node;



def var():
    
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<vars>", token , lineNumber)
    
    
    if(token == "beginTk" or token == "outTk" or token == "inTk" or token == "loopTk" or token == "iffyTk" or token == "idTk"):
        node.token = "voidTk"
        return node
        
    #counter[0] = count + 1
    count = counter[0]
    token = tokenList[count].tkClass
    
    if(token == "dataTk"):
        
        token = tokenList[count+1].tkClass
        
        if(token == "idTk"):
            node.ident = tokenList[count + 1].tkInstance
            token = tokenList[count + 2].tkClass
            
            if(token == "equalTk"):
                token = tokenList[count + 3].tkClass
                
                if(token == "intTk"):
                    
                    node.integer = tokenList[count + 3].tkInstance
                    token = tokenList[count + 4].tkClass
                    
                    if(token == "periodTk"):
                        counter[0] = count + 5
                        
                        node.left = var()
                        
                        return node
                        
                    else:
                        print("Parse Error: Expected period after "+str(tokenList[count+3].tkInstance) + "on line number: "+ str(lineNumber))
                        sys.exit()
                        
                else:
                    print("Parse Error: Expected integer after = sign on line number: "+ str(lineNumber))
                    sys.exit()
                
            else:
                print("Parse Error: Expected equal sign after identifier "+node.ident+" on line number: "+ str(lineNumber))
                sys.exit()
            
        else:
            print("Parse Error: Excpected identifier after Data on line number: "+ str(lineNumber))
            sys.exit()
        
    else:
        print("Parse Error: Expected dataTk on line: "+ str(lineNumber))
        sys.exit()
 

def expr():
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<expr>", token , lineNumber)
    
    node.left = N()
    
    token = tokenList[counter[0]].tkClass
    
    if(token == "subTk"):
        
        node.value = "-"
        
        counter[0] = count + 2
        
        node.right = expr()
    
    return node
    
def N():
    
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<N>", token , lineNumber)
    
    node.left = A()
    
    token = tokenList[counter[0]].tkClass
    
    if(token == "divTk" or token == "multTk"):
        node.value = tokenList[counter[0]].tkInstance
        
        counter[0] = count + 1
        
        node.right = N()
        
        return node
    
    else:
        
        return node
    
def A():
    
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<A>", token , lineNumber)
        
    node.left = M()
    
    token = tokenList[counter[0]].tkClass
    
    if(token == "addTk"):
        count = counter[0]
        counter[0] = count + 1
        if(tokenList[counter[0]].tkClass == "intTk" or tokenList[counter[0]].tkClass == "idTk" or tokenList[counter[0]].tkClass == "multTk" ):
            node.right = A()
        else:
            #recentchange
            print("Parse Error: Expected idTk or intTk after "+token+" on line: "+str(lineNumber))
            sys.exit()
        
    
    return node
        
def M():
    
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<M>", token , lineNumber)
    
    
    if(token == "multTk"):
        
        node.value = "*"
        
        counter[0] = count + 1
        
        node.left = M()
    else:

        node.left = R()
        
    return node
    
def R():
    
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<R>", token , lineNumber)
    
        
    if(token == "lParTk"):
        
        counter[0] = count + 1
        
        node.left = expr()
        
        if(tokenList[counter[0]].tkClass == "rParTk"):
            
            count = counter[0]
            counter[0] = count + 1
            
            return node
        else:
            
            print("Parse Error: Expected right parenthesis on line " + str(lineNumber))
            sys.exit()
    
    if(token == "idTk" or token == "intTk"):
        
        if(token == "idTk"):
            node.token = tokenList[counter[0]].tkClass
            node.ident = tokenList[counter[0]].tkInstance
            
            counter[0] = count + 1
            
            return node
        
        if(token == "intTk"):
            node.token = tokenList[count].tkClass
            node.integer = tokenList[count].tkInstance
            
            
            counter[0] = count + 1
            
            return node
            
    else:
        #print("This token caused the fail "+tokenList[counter[0]].tkClass)
        #print("Parse Error: Identifier or Integer expected on line: " + str(lineNumber))
        #sys.exit()
        pass
        

def stats():
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<stats>", "voidTk" , 1)
    
    node.left = stat()
    node.right = mStat()
    
    return node
    
def mStat():
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<mStat>", "voidTk" , 1)
    
    if(token == "endTk"):
        
        node.token = "empty"
        return node
    else:
        node.left = stat()
        node.right = mStat()
        return node

def stat():
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<stat>", token , lineNumber)
    
    
    if(token == "inTk"):
        
        node.left = inFunc()
        
        if(tokenList[counter[0]].tkClass == 'periodTk'):
            pass
        else:
            print("Parse Error: Expected period after end of line on line number: " + str(lineNumber))
            sys.exit()
        
    elif(token == "outTk"):
        
        node.left = out()
        
        if(tokenList[counter[0]].tkClass == 'periodTk'):
            pass
        else:
            print("Parse Error: Expected period after end of line on line number: " + str(lineNumber))
            sys.exit()
        
    elif(token == "beginTk"):
        
        node.left = block()
        
    elif(token == "iffyTk"):
        
        node.left = ifst()
        
        if(tokenList[counter[0]].tkClass == 'periodTk'):
            pass
        else:
            print("Parse Error: Expected period after end of line on line number: " + str(lineNumber))
            sys.exit()
        
    elif(token == "loopTk"):
        
        node.left = loop()
        
        if(tokenList[counter[0]].tkClass == 'periodTk'):
            pass
        else:
            print("Parse Error: Expected period after end of line on line number: " + str(lineNumber))
            sys.exit()
        
    elif(token == "idTk"):
        
        node.left = assign()
        
        if(tokenList[counter[0]].tkClass == 'periodTk'):
            pass
        else:
            print("Parse Error: Expected period after end of line on line number: " + str(lineNumber))
            sys.exit()
        
    else:
        
        print("Parse Error: Innopropriate or misplaced value: " + str(tokenList[count].tkInstance) +" on line number: " + str(lineNumber))
        sys.exit()
     
     
    count = counter[0]
    counter[0] = count + 1
    return node
        
def inFunc():
    
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<in>", token , lineNumber)
    
    counter[0] = count + 1
    
    if(token == "inTk"):
        
        if(tokenList[counter[0]].tkClass == "idTk"):
            
            node.ident = tokenList[counter[0]].tkInstance
            count = counter[0]
            counter[0]=count + 1
        else:
            print("Parse Error: Expected Identifier after -in- on line: " + str(lineNumber))
            sys.exit()
        
        
    else:
        print("Parse Error: Expected -in- expression on line: "+ str(lineNumber))
        sys.exit()
        
    return node

def out():
    
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<out>", token , lineNumber)
    
    
    counter[0] = count + 1
    
    if(token == "outTk"):
        node.left = expr()
        
    else:
        print("Parse Error: Expected -out- on line number: "+str(lineNumber))
        sys.exit()
    
    return node

def ifst():
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<if>", token , lineNumber)
    
    counter[0] = count + 1
    count = counter[0]
    
    if(tokenList[counter[0]].tkClass == "lSqBracketTk"):
        counter[0] = count + 1
        
        node.left = expr()
        node.right = RO()
        node.child3 = expr()
        
        
        if(tokenList[counter[0]].tkClass == "rSqBracketTk"):
            count = counter[0]
            counter[0] = count + 1
            token = tokenList[counter[0]].tkClass
            
            if(token == "thenTk"):
                count = counter[0]
                counter[0] = count + 1
                node.child4 = stat()
            else:
                print("Parse Error: Expected then after ] on line "+str(lineNumber))
                sys.exit()
        else:
            print("Parse Error: Expected ] on line: "+str(lineNumber))
            sys.exit()
            
    else:
        print("Parse Error: Expected [ on line: "+str(lineNumber))
        sys.exit()

    return node   
    

def loop():
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<loop>", token , lineNumber)
    
    counter[0] = count + 1
    count = counter[0]
    
    
    if(tokenList[counter[0]].tkClass == "lSqBracketTk"):
        count = counter[0]
        counter[0] = count + 1
        
        node.left = expr()
        node.right = RO()
        node.child3 = expr()
        
        if(tokenList[counter[0]].tkClass == "rSqBracketTk"):
            count = counter[0]
            counter[0] = count + 1
            
            node.child4 = stat()
        else:
            print("Parse Error: Expected ] on line: "+str(lineNumber))
            sys.exit()
    else:
        print("Parse Error: Expected [ on line: "+str(lineNumber))
        sys.exit()
        
    return node
            

def assign():
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<assign>", token , lineNumber)
    
    node.ident = tokenList[count].tkInstance
    node.value  = tokenList[count].tkInstance
    
    counter[0] = count + 1
    count = counter[0]
    
    if(tokenList[count].tkClass == "equalTk"):
        count = counter[0]
        counter[0] = count + 1
        node.left = expr()
    else:
        print("Parse Error: Expected equal sign after: "+str(node.value)+" on line number: "+ str(lineNumber))
        sys.exit()
        
    return node

#RO() should be error free    
def RO():
    global counter
    count = counter[0]
    
    token = tokenList[count].tkClass
    lineNumber = tokenList[count].lineNum
    node = Node("<RO>", token , lineNumber)
    
   
    
    if(token == "lessTTk"):
        
        count = counter[0]
        counter[0] = count + 1
        
        if(tokenList[counter[0]].tkClass == "lessTTk"):
            
            counter[0] = count + 2
            node.value = "< <"
            
        elif(tokenList[counter[0]].tkClass == "greaterTTk"):
            
            counter[0] = count + 2
            
            node.value = "< >"
            
        else:
            counter[0] = count + 1
            node.value = "<"
            
    elif(token == "greaterTTk"):
        
        count = counter[0]
        counter[0] = count + 1
        
        if(tokenList[counter[0]].tkClass == "greaterTTk"):
            counter[0] = count + 2
            node.value = "> >"
            
        else:
            counter[0] = count + 1
            node.value = ">"
            
    elif(token == "dubEqTk"):
        counter[0] = count + 1
        node.value = "=="
            
    else:
        print("Parse Error: Expected operator token on line number: " + str(lineNumber))
        sys.exit()
        
    return node
            
    

count = 0
tokenCount = 0      
with open('temp.txt','r') as f:
    
    #print("Starting Scanner...")
    for line in f:
        
        count = count + 1
        
        for word in line.split():
            
            tkType = scanDriver(word, count)
            
            #Removing comments before parser.
            if(tkType == 'commentTk'):
                continue
            if(tkType == -1):
                scannerError = True
                
            addToken = token(tkType, count, word)
            tokenList.append(addToken)
            tokenCount = tokenCount + 1
            
addToken = token('EOFtk', count, None)            
tokenList.append(addToken)
tokenCount = tokenCount + 1

if(scannerError == True):
    print("There are scanner errors present that must be resolved before running the Parser.")
    sys.exit()
'''            
for x in range(0,tokenCount):
    print(tokenList[x].tkClass + str(tokenList[x].lineNum))
'''
    
'''
print(counter[0])
count = counter[0]
count = count + 1
counter[0] = 5
print(counter[0])
'''
        
