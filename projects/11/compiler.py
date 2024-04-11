import re

specialChars = [['&lt;', '<'], ['&gt;', '>'], ['&quot;', '"'], ['&amp;', '&']]

# 1: convert XML to a long ass string
def readXML(file):
    f = open(file, 'r')
    
    # after each open or close <> we append the word
    result = []
    
    for i in f:
        tokens = re.findall(r'<[^>]+>|[^<]+', i)
    
    # NOTE: we don't need this: removes weird spacing thing
    for i in range(len(tokens)):
        if tokens[i][0] == ' ' and tokens[i][len(tokens[i]) - 1] == ' ':
            tokens[i] = tokens[i][1:len(tokens[i]) - 1]
            
            # replace special chars
            for j in range(len(specialChars)):
                
                tokens[i] = tokens[i].replace(specialChars[j][0], specialChars[j][1])
    
    return tokens

variables = []

symbols = ['var', 'field', 'static', 'arg']
globalSymbols = ['static', 'field']

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
            return row[0], row[1], row[2], row[3]
    #print(var)
    
    return 'UNKNOWN', '', "ERROR", 'VAR NOT FOUND'

    
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
       
VMcode = ''

# --- 3: create VM command writing helper functions --- #
# push or pop commands
def writeCommand(type, segment, index):
    global VMcode
    line = type + ' ' + segment + ' ' + index + '\r\n'
    VMcode = VMcode + line
    return

symbolToCommand = [['+', 'add'], ['-', 'sub'], ['<', 'lt'], ['>', 'gt'], ['&', 'and'], ['|', 'and'], ['~', 'not'], ['-', 'neg']]

# TODO: add & and |
def writeArithmetic(type):
    global VMcode
    
    written = False
    
    for i in range(len(symbolToCommand)):
        if type == symbolToCommand[i][0]:
            VMcode = VMcode + symbolToCommand[i][1] + '\r\n'
            written = True
    
    if type == '*':
        writeCall('Math.multiply', '2')
        written = True
        
    if type == '/':
        writeCall('Math.divide', '2')
        written = True
    
    if written == False:
        VMcode = VMcode + type + '\r\n'
        
    return

# Label, Goto, if
def writeStatement(type, label):
    global VMcode
    VMcode = VMcode + type + ' ' + label + '\r\n'
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

# class name at the top of file
currentClass = ''

# ---- 4: compiles a full class ---- #
# TODO: add a protective measure
def moveIndexTo(tokens, index, str):
    while tokens[index] != str:
        index += 1
    
    return index

# TODO:
def compileClass(tokens, index):
    global currentClass
    if tokens[index] == '<class>':
        index = index + 5
        
        # records the class name from the top of the file
        currentClass = tokens[index]
        
        # move our index to <subroutineDec>
        while tokens[index] != '<subroutineDec>':
            index += 1
        
        index = compileSubroutine(tokens, index)
    
    return
    
# TODO: maybe not
def compileClassVarDec():
    return
    
# TODO
def compileSubroutine(tokens, index):
    # move to the keyword the keyword method, construct, function
    index += 2
    
    # TODO: fix this
    if tokens[index] == 'method':
        # name of function
        index += 6
        name = currentClass + '.' + tokens[index]
        
        index = moveIndexTo(tokens, index, '<parameterList>')
        
        # find the number of vars via param number
        nVars = howManyParams(tokens, index)
        
        writeFunction(name, nVars)
        
        # grab the this segment
        writeCommand('push', 'argument', 'zero')
        writeCommand('pop', 'pointer', '0')
        
        
    if tokens[index] == 'function':
        # name of function
        index += 6
        name = currentClass + '.' + tokens[index]
        
        index = moveIndexTo(tokens, index, '<parameterList>')
        
        # find the number of vars
        nVars = varCount('local')
        
        writeFunction(name, nVars)
        
        compileParameterList()
        
    if tokens[index] == 'constructor':
        # name of function
        index += 6
        name = currentClass + '.' + tokens[index]
        
        # IM NOT SURE IF WE CARE ABOUT THE PARAMS RIGHT NOW
        
        nVars = varCount('field')
        
        # allocate nVars amount of memory 
        writeCommand('push', 'constant', str(nVars))
        writeCall('Memory.alloc', '1')
        
        # move the memory pointer into the this memory segment
        writeCommand('pop', 'pointer', '0')
        
     
    index = moveIndexTo(tokens, index, '<subroutineBody>')
    
    index = compileSubroutineBody(tokens, index)
    
    return index

# debugging function
def printer(tokens, index, num):
    for i in range(num):
        print(tokens[index + i])

# returns the number of parameters provided to the function
def howManyParams(tokens, index):
    final_index = moveIndexTo(tokens, index, '</parameterList>')
    
    return ((final_index - index) / 3)

# TODO: pushes them to the stack?
def compileParameterList():
    return

# TODO: incomplete
def compileSubroutineBody(tokens, index):
    # NOTE: could cause an if this isnt always generated
    index = moveIndexTo(tokens, index, '<statements>')
    
    index = compileStatements(tokens, index)
        
    return index

# DONE: litteraly does nothing
def compileVarDec(tokens, index):
    return index

# TODO:
def compileStatements(tokens, index):
    while tokens[index] != '</statements>':
        index += 1
        if tokens[index] == '<doStatement>':
            index = compileDo(tokens, index)
            
        if tokens[index] == '<returnStatement>':
            index = compileReturn(tokens, index)
            
        if tokens[index] == '<letStatement>':
            index = compileLet(tokens, index)
            
        if tokens[index] == '<ifStatement>':
            index = compileIf(tokens, index)
            
        if tokens[index] == '<whileStatement>':
            index = compileWhile(tokens, index)
        
    return index

# TODO: array logic
def compileLet(tokens, index):
    # move to var name
    index += 5
    
    # loop up in table (given 'x' aka the name variables[])
    type, name, segment, num = varType(tokens[index])
    #printer(tokens, index, 5)
    #print('Name: ' + name)
    
    # special logic for arrays!
    if name == 'Array' and tokens[index] == '[':
        index = moveIndexTo(tokens, index, '<term>')
        index = compileExpression(tokens, index, [], [])[0]
        
        # add arr pointer and expression
        writeArithmetic('add')
        
        # compile seconds expression
        index = moveIndexTo(tokens, index, '<expression>')
        
        index = compileExpression(tokens, index, [], [])[0]
        
        # store the returned val into temp memory
        writeCommand('pop', 'temp', '0')
        
        #pop pointer 1 // THAT = address of a[i]
        writeCommand('pop', 'pointer', '1')
        #push temp 0 // stack top = b[j]
        writeCommand('push', 'temp', '0')
        #pop that 0 // a[i] = b[j]
        writeCommand('pop', 'that', '0')
        
        index = moveIndexTo(tokens, index, '</letStatement>')
    
        return index
    
    index = moveIndexTo(tokens, index, '<expression>')
    
    # compile expression
    index = compileExpression(tokens, index, [], [])[0]
    
    # pop the val from expression into the var
    writeCommand('pop', segment, str(num))
    
    index = moveIndexTo(tokens, index, '</letStatement>')
    
    return index

Label_counter = 0

def compileIf(tokens, index):
    global Label_counter
    
    index = moveIndexTo(tokens, index, '<expression>')
    
    index = compileExpression(tokens, index, [], [])[0]
    
    # invert the expression
    writeArithmetic('~')
    
    # 1. write a unique label to go to if true
    writeStatement('if-goto', 'L' + str(Label_counter))
    Label_counter += 1
    
    index = moveIndexTo(tokens, index, '<letStatement>')
    
    index = compileStatements(tokens, index)
    
    # 2. go to end of statement (aka skip the next part)
    writeStatement('goto', 'L' + str(Label_counter))
    Label_counter += 1
    
    # jumped from point 1. 
    writeStatement('label', 'L' + str(Label_counter - 2))
    
    index = compileStatements(tokens, index)
    
    # jumped from point 2. (end of ifStatement)
    writeStatement('label', 'L' + str(Label_counter - 2))
    
    return index


def compileWhile(tokens, index):
    global Label_counter
    
    # write the loop label
    writeStatement('label', 'L' + str(Label_counter))
    Label_counter += 1
    
    index = moveIndexTo(tokens, index, '<expression>')
    
    index = compileExpression(tokens, index, [], [])[0]
    
    # invert the expression
    writeArithmetic('not')
    
    # 1. goto the escape loop label if expression is true
    writeStatement('if-goto', 'L' + str(Label_counter))
    
    index = moveIndexTo(tokens, index, '<statements>')
    
    index = compileStatements(tokens, index)
    
    # 2. LOOP !!!
    writeStatement('goto', 'L' + str(Label_counter - 1))
    
    # write escape loop label
    writeStatement('label', 'L' + str(Label_counter))
    
    index = moveIndexTo(tokens, index, '</whileStatement>')
    
    return index


def compileDo(tokens, index):
    index = compileSubroutineCall(tokens, index)
    
    # pop temp 0
    writeCommand('pop', 'temp', '0')
    
    return index


def compileReturn(tokens, index):
    # move to expression or symbol
    index += 4
    
    if tokens[index] == '<expression>':
        index = compileExpression(tokens, index, [], [])[0]
        
        # probably move to symbol
        index += 1
    else:
        writeCommand('push', 'constant', '0')
    
    writeReturn()
    
    # move to </returnStatement>
    index = moveIndexTo(tokens, index, '</returnStatement>')
    
    return index

def compileSubroutineCall(tokens, index):
    # change the use cases for function calls
    if tokens[index + 11] == '<expressionList>':
        offset = 0
    else:
        offset = 5
    
    expression_index = moveIndexTo(tokens, index, '<expressionList>')
    
    # first we eval some expression
    Nargs = compileExpressionList(tokens, expression_index)
    
    # push the object
    type, name, segment, num = varType(tokens[index + offset])
    if type != 'UNKNOWN':
        writeCommand('push', segment, str(num))
        extraParam = 1
    else:
        extraParam = 0
        # changed from var[0] to var[1] ... I know
        name = tokens[index + offset]
    
    # call function
    writeCall(name + tokens[index + offset + 3] + tokens[index + offset + 6], str(Nargs + extraParam))
    
    index = moveIndexTo(tokens, index, '</expressionList>')
    
    return index

# TODO: add array compatability
def compileExpression(tokens, index, nums, ops):   
    # move to first part of the expression
    index += 1
    
    # create stacks for nums and ops
    while tokens[index] != '</expression>':
        if tokens[index] == '<term>':
            index, nums = compileTerm(tokens, index, nums, ops)
            
            nums, ops = doStackOps(nums, ops)

        if tokens[index] == '<symbol>':
            index += 1
            
            if tokens[index] == ')':
                removeParentheses(nums)
                removeParentheses(ops)
            else:
                if tokens[index] == '(':
                    nums.append(tokens[index])
                    
                # add the + - * or whatever
                ops.append(tokens[index])
            
            nums, ops = doStackOps(nums, ops)
        
        if tokens[index] == '<expression>':
            index, nums, ops = compileExpression(tokens, index, nums, ops)
        
        index += 1
    
    return index, nums, ops

# moves backwards to remove '('
def removeParentheses(str):
    for i in range(len(str)):
        #print(str[len(str) - i - 1])
        if str[len(str) - i - 1] == '(':
            str.pop(len(str) - i - 1)

    return str

# expression helper function
def doStackOps(nums, ops):
    # NOTE: this may break everything
    # do single unaryOp operations
    if len(nums) > 0 and len(ops) > 0:
        if nums[-1] != '(':
            if ops[-1] == '~' or ops[-1] == '-':
                writeArithmetic(ops.pop(-1))
    
    while True:
        if len(nums) > 1 and len(ops) > 0:
            if ops[-1] != '(' and nums[-1] != '(' and nums[-2] != '(':
                #print(nums)
                #print(ops)
                # pop the command to write it
                writeArithmetic(ops.pop(-1))
                
                # remove a val from the nums stack
                nums.pop(-1)
            else:
                break
        else:
            break
    
    return nums, ops

            
# TODO: fix / add priority to lists
def compileTerm(tokens, index, nums, ops):
    
    # move to term type
    index += 1
    
    if tokens[index] == '<integerConstant>':
        index += 1
        nums.append(tokens[index])
        writeCommand('push', 'constant', tokens[index])
        index += 1
        
    if tokens[index] == '<stringConstant>':
        compileString(tokens[index + 1])
        index += 1

    # NOTE: not sure if it can handle class function calls
    if tokens[index] == '<identifier>':  
        index += 1
        nums.append(tokens[index])
        
        type, name, segment, num = varType(tokens[index])
        
        # if type == subroutineCall
        if type == 'UNKNOWN' and name != 'Array':
            print("SUBROUTINE: " + tokens[index])
            index = compileSubroutineCall(tokens, index)
        else:
            # push the symbol
            writeCommand('push', segment, str(num))
            print('IDENT: ' + tokens[index])
            #printer(tokens, index, 3)
            
            # logic for arrays: '(' added for logic
            if tokens[index + 3] == '[':
                print("array: " + tokens[index])
                nums.append('(')
                ops.append('(')
                
                index = compileExpression(tokens, index + 5, nums, ops)[0]
                
                removeParentheses(nums)
                removeParentheses(ops)
                
                # add to get the arr + expression address
                writeArithmetic('add')
                print('ADDING: ' + tokens[index])
                
                #pop pointer 1 // THAT = address of b[j]
                writeCommand('pop', 'pointer', '1')
                #push that 0 // stack top = b[j]
                writeCommand('push', 'that', '0')
                
                # remove the val because we just added it
                nums.pop(-1)
                
            index = moveIndexTo(tokens, index, '</term>')

    return index, nums

# only used for compiling strings inside of terms
def compileString(token):
    # first call string.new for the len(token)
    writeCommand('push', 'constant', str(len(token)))
    writeCall('String.new', '1')
    
    # add chars to the string
    for char in token:
        writeCommand('push', 'constant', str(ord(char)))
        writeCall('String.appendChar', '2')
    return

# TODO: calls compileExpression for each comma seperated thingy
def compileExpressionList(tokens, index):
    nums = []
    ops = []
    
    # number of aguments going into a function || tracked by commas
    Nargs = 0
    
    # move to end of expression list
    while tokens[index] != '</expressionList>':
        # compile first expression
        if tokens[index] == '<expression>':
            index, nums, ops = compileExpression(tokens, index, nums, ops)
            Nargs += 1
            
        index += 1
        
    return Nargs


def main(file, save_file_name):
    tokens = readXML(file)
    
    SymbolTable(tokens)
    print(variables)
    
    compileClass(tokens, 0)
    
    f = open(save_file_name + '.vm', "w")
    
    f.writelines(VMcode)
    
    f.close()
    
    return

xml_file_path = "Average/noIndents.xml"   
save_file_name = 'Average/Main'
main(xml_file_path, save_file_name)

#NOTE: we need to update terms to handle: strings, *expressions, *unaryOp (symbol) term
#NOTE: object function calls must push the object beforehand