
# --- 3: create VM command writing helper functions --- #
# push or pop commands
def writeCommand(type, segment, index):
    global VMcode
    line = type + ' ' + segment + ' ' + index + '\r\n'
    VMcode = VMcode + line
    return

# ADD, SUB, NEG, exc
def writeArithmetic(type):
    global VMcode
    
    if type == '+':
        VMcode = VMcode + 'add' + '\r\n'
        
    if type == '-':
        VMcode = VMcode + 'sub' + '\r\n'
    
    if type == '*':
        writeCall('Math.multiply', '2')
        
    if type == '/':
        writeCall('Math.divide', '2')
        
    return

# Label, Goto, if
def writeStatement(label):
    global VMcode
    VMcode = VMcode + label + '\r\n'
    return

def writeCall(name, Nargs):
    global VMcode
    VMcode = VMcode + 'call ' + name + ' ' + Nargs + '\r\n'
    return
    
def writeFunction(name, nVars):
    global VMcode
    VMcode = VMcode + 'function ' + name + ' ' + str(nVars) + '\r\n'
    return
    
# its that simple 
def writeReturn():
    global VMcode
    VMcode = VMcode + 'return\r\n'
    return
