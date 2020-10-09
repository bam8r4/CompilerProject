#Author of this code is Brent Moran

from files import *


opTokens = ['=','<','>','==',':','+','-','*','/','%','.','(',')',',','{','}',';','[',']']

keywordTokens = ['begin', 'end', 'loop', 'void', 'var', 'return', 'in', 'out', 'program', 'iffy', 'then', 'let', 'data']

fsaTable = [
    
    ['equalTk','lessTTk','greaterTTk','dubEqTk','colTk','addTk','subTk','multTk','divTk','percentTk','periodTk','lParTk','rParTk','commaTk','lCurlBracketTk','rCurlBracketTk','semiColonTk','lSqBracketTk','rSqBracketTk'] ,
    ['beginTk', 'endTk', 'loopTk', 'voidTk', 'varTk', 'returnTk', 'inTk', 'outTk', 'programTk', 'iffyTk', 'thenTk', 'letTk', 'dataTk'] , 
    ['idTk'],
    ['intTk'],
    ['commentTk'],
    ["Error 5: Invalid value in idToken: "],
    ["Error 6: Value that is not numeric in intToken: "],
    ["Error 7: Whitespace in a between two @ signs is not allowed. On line number: "],
    ["Error 8: Unkown error on line number: "]
    
    ]

def tkTypeFsa(value):
            
    for x in opTokens:
        if(value == x):
            return 0
    for x in keywordTokens:
        if(value == x):
            return 1
    if(value[0].isalpha()):
        for x in range(0,len(value)):
            if(value[x].isalpha() or value[x].isdigit()):
                continue
            else:
                return 5
        return 2
    
    if(value[0].isdigit()):
        for x in range(0,len(value)):
            if(value[x].isdigit()):
                continue
            else:
                return 6
        return 3    
    
    if(value[0] == '@'):
        for x in range(0, len(value)):
            if(value[x].isspace()):
                return 7
        if(value[int(len(value)-1)] == '@'):
            return 4
    else:
        return 8
        
def tkInstanceFsa(tkInstance , value):
    
   
        if(tkInstance == 0):
            
            count = 0
            for x in opTokens: 
                if(value == x):
                    return count
                count = count + 1  
             
            
        elif(tkInstance == 1):
            count = 0
            for x in keywordTokens:
                if(value == x):
                    return count
                count = count + 1
            
                    
        else:
            return 0
        
        
            
        
def fsaTableDriver(x , y):
    return fsaTable[x][y]
    
    
def scanDriver(value, lineNum):
    
    x = tkTypeFsa(value)
    y = tkInstanceFsa(x, value)
    
    if x is None:
        x = 7
    
    if(x > 4):
        
        if(x == 5 or x == 6):
            
            if(x == 5):
                message = fsaTableDriver(x,y)
                print(message + value + " on line number: "+ str(lineNum))
                return -1
            
            if(x == 6):
                message = fsaTableDriver(x,y)
                print(message  + value + " on line number: "+ str(lineNum))
                return -1
                
        if(x == 7 or x == 8):
            
            if(x == 7):
                message = fsaTableDriver(x,y)
                print(message + str(lineNum))
                return -1
            
            if(x == 8):
                message = fsaTableDriver(x,y)
                print(message + str(lineNum))
                return -1
    
    
    retValue = fsaTableDriver(x,y)
    
    return retValue
            
