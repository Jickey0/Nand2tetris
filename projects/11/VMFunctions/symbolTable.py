
# ---- 2: loop through the string to create symbol table ---- #
def SymbolTable(tokens):
    
    # adds the local varaibles this and that first
    define('this', 'point', 'argument')
    define('other', 'point', 'argument')
    
    for i in range(len(tokens)):
        token = tokens[i]
        
        if token in symbols:
            # moves two tokens right to find the type
            type = tokens[i + 3]
            
            # moves four tokens right to find the names
            names = findNames(tokens, i + 6)
            
            # we replace field with this
            if token == 'field':
                token = 'this'
            if token == 'var':
                token = 'local'
            
            for name in names:
                define(name, type, token)
            
    return
    
# adds a new variable to the current table
def define(name, type, kind):
    # gets the number of a specific kind in order to add to the table
    index = varCount(kind)
    
    row = [name, type, kind, index]
    variables.append(row)
    return 
    
# returns the number of a given kind
def varCount(kind):
    count = 0
    for row in variables:
        if row[2] == kind:
            count += 1
    return count
  
# returns the type of a varible 
def varType(var):
    global variables
    
    for row in variables:
        if row[0] == var:
            return row[2], row[3]
        
    return "ERROR", 'VAR NOT FOUND'
    
# loops to find the number of variables to add and their respective names
def findNames(tokens, index):
    count = 0
    names = []
    
    while True:
        currentToken = tokens[index + count]
        
        if currentToken == ';':
            return names
        if currentToken != ',':
            names.append(currentToken)
        
        count += 3       
