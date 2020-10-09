def printPreorder(root): 
    
    hasInt = True
    hasId = True
  
    
  
    if root: 
        if(root.ident == None):
            hasId = False
            
        if(root.integer == None):
            hasInt = False
            
        if(hasInt == True or hasId == True):
            
            if(hasInt == True and hasId == True):
                print(root.label+" "+root.ident+" "+str(root.integer))
            elif(hasInt == True):
                print(root.label+" "+str(root.integer))
            elif(hasId == True):
                print(root.label+" "+str(root.ident))
            else:
                print(root.label)
        
        else:
            
            if root.value:
                print(str(root.label)+" "+str(root.value))
            else:
                print(root.label)
            
  
        if root.left:
            printPreorder(root.left) 
  
        if root.right:
            printPreorder(root.right)
        
        if root.child3:
            printPreorder(root.child3)
            
        if root.child4:
            printPreorder(root.child4)