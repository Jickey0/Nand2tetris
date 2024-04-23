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

GlobalVariables = []
LocalVariables = []

symbols = ['var', 'field', 'static', 'arg']
globalSymbols = ['static', 'field']

# ---- 2: loop through the string to create symbol table ---- #
def GlobalSymbolTable(tokens):
    index = 0
    
    # NOTE: I think this is only for method and constructor calls (need to check)
    # adds the local varaibles this and that first
    #define('this', 'point', 'argument')
    #define('other', 'point', 'argument')
    
    while tokens[index] != '<subroutineDec>' and tokens[index] != '</class>':
        if tokens[index] in symbols:
            kind = tokens[index]

            # moves two tokens right to find the type
            type = tokens[index + 3]
            
            # moves four tokens right to find the names
            index, names = findNames(tokens, index + 6)
            
            for name in names:
                define(name, type, kind)  
            
        index += 1
    return
    
# TODO: FIX THIS: adds a new variable to the current table
def define(name, type, kind):
    global GlobalVariables
    global LocalVariables
    
    if kind == 'field':
        kind = 'this'
    
    # gets the number of a specific kind in order to add to the table
    index = varCount(kind)
    
    row = [name, type, kind, index]
    if kind == 'this' or kind == 'static':
        GlobalVariables.append(row)
    else:
        LocalVariables.append(row)
        
    return 
    
# returns the number of a given kind
def varCount(kind):
    global GlobalVariables
    global LocalVariables
    
    count = 0
    for row in GlobalVariables:
        if row[2] == kind:
            count += 1
    for row in LocalVariables:
        if row[2] == kind:
            count += 1
    return count
  
# returns the type of a varible 
def varType(var):
    global GlobalVariables
    global LocalVariables
    
    for row in GlobalVariables:
        if row[0] == var:
            return row[0], row[1], row[2], row[3]
        
    for row in LocalVariables:
        if row[0] == var:
            return row[0], row[1], row[2], row[3]
    
    return 'UNKNOWN', '', "ERROR", 'VAR NOT FOUND'
    
# loops to find the number of variables to add and their respective names
def findNames(tokens, index):
    names = []
    
    while True:
        currentToken = tokens[index]
        
        if currentToken == ';':
            return index, names
        if currentToken != ',':
            names.append(currentToken)
        
        index += 3       
       
VMcode = ''

# --- 3: create VM command writing helper functions --- #
# push or pop commands
def writeCommand(type, segment, index):
    global VMcode
    line = type + ' ' + segment + ' ' + index + '\r\n'
    VMcode = VMcode + line
    return

symbolToCommand = [['+', 'add'], ['-', 'sub'], ['<', 'lt'], ['>', 'gt'], ['&', 'and'], ['|', 'and'], ['=', 'eq']]

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

def PushKeywordConst(token):
    if token == 'this':
        writeCommand('push', 'pointer', '0')
    else:
        writeCommand('push', 'constant', '0')
        if token == 'true':
            writeArithmetic('not')

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
        
        while tokens[index] != '</class>':
            if tokens[index] == '<subroutineDec>':
                index = compileSubroutine(tokens, index)
            index += 1
    
    return
    
# TODO
def compileSubroutine(tokens, index):
    global LocalVariables
    
    # move to the keyword the keyword method, construct, function
    index += 2
    
    # TODO: fix this
    if tokens[index] == 'method':
        # clear the local vars for the next table!
        LocalVariables = []
        define('this', 'point', 'argument')
        compileParamList(tokens, index)
        compileSubroutineVariables(tokens, index)
        
        # name of function
        index += 6
        name = currentClass + '.' + tokens[index]
        
        index = moveIndexTo(tokens, index, '<parameterList>')
        
        # WRONG: find the number of vars via param number
        # nVars = howManyParams(tokens, index)
        
        # find the number of vars
        nVars = varCount('local')
        
        writeFunction(name, nVars)
        
        # grab the this segment
        writeCommand('push', 'argument', '0')
        writeCommand('pop', 'pointer', '0')
        
    if tokens[index] == 'function':
        LocalVariables = []
        compileParamList(tokens, index)
        compileSubroutineVariables(tokens, index)
        
        # name of function
        index += 6
        name = currentClass + '.' + tokens[index]
        
        index = moveIndexTo(tokens, index, '<parameterList>')
        
        # find the number of vars
        nVars = varCount('local')
        
        writeFunction(name, nVars)
        
    if tokens[index] == 'constructor':
        LocalVariables = []
        compileParamList(tokens, index)
        compileSubroutineVariables(tokens, index)
        
        # name of function
        index += 6
        name = currentClass + '.' + tokens[index]
        
        # find the number of vars
        nVars = varCount('local')
        
        # find the number of vars (why?)
        nArgs = varCount('this')
        
        writeFunction(name, nVars)
        
        # allocate nVars amount of memory 
        writeCommand('push', 'constant', str(nArgs))
        writeCall('Memory.alloc', '1')
        
        # move the memory pointer into the this memory segment
        writeCommand('pop', 'pointer', '0')
        
     
    print(LocalVariables)
     
    index = moveIndexTo(tokens, index, '<subroutineBody>')
    
    index = compileSubroutineBody(tokens, index)
    
    index = moveIndexTo(tokens, index, '</subroutineDec>')
    
    return index

# adds params to local symbol table
def compileParamList(tokens, index):
    global LocalVariables
    
    index = moveIndexTo(tokens, index, '<parameterList>')
    
    while tokens[index] != '</parameterList>':
        if tokens[index] == '<keyword>':
            define(tokens[index + 4], tokens[index + 1], 'argument')
            index += 5
        index += 1
    return index
    
def compileSubroutineVariables(tokens, index):
    while tokens[index] != '</subroutineBody>':
        if tokens[index] == 'var':
            kind = 'local'

            # moves two tokens right to find the type
            type = tokens[index + 3]
            
            # moves four tokens right to find the names
            index, names = findNames(tokens, index + 6)
            
            for name in names:
                define(name, type, kind) 
        
        index += 1
    return
    

# helper: debugging function
def printer(tokens, index, num):
    for i in range(num):
        print(tokens[index + i])

# helper: returns the number of parameters provided to the function
def howManyParams(tokens, index):
    final_index = moveIndexTo(tokens, index, '</parameterList>')
    
    return ((final_index - index) / 3)

# helper: finds if there is an else in the if statement
def containsElse(tokens, index):
    ifcounter = 0
    index += 1
    while tokens[index] != '</ifStatement>' or ifcounter != 0:
        if tokens[index] == '<ifStatement>':
            ifcounter += 1
        elif tokens[index] == '</ifStatement>':
            ifcounter -= 1
        elif tokens[index] == 'else' and ifcounter == 0:
            return True
        index += 1
        token = tokens[index]
    return False

# TODO: complete?
def compileSubroutineBody(tokens, index):
    # NOTE: could cause an if this isnt always generated
    index = moveIndexTo(tokens, index, '<statements>')
    
    index = compileStatements(tokens, index)
    
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
    
    # special logic for arrays!
    if name == 'Array' and tokens[index + 3] == '[':
        index = moveIndexTo(tokens, index, '<expression>')
        
        writeCommand('push', segment, str(num))
        index = compileExpression(tokens, index)
        
        # add arr pointer and expression
        writeArithmetic('add')
        
        # compile seconds expression
        index = moveIndexTo(tokens, index, '<expression>')
        
        index = compileExpression(tokens, index)
        
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
    index = compileExpression(tokens, index)
    
    # pop the val from expression into the var
    writeCommand('pop', segment, str(num))
    
    index = moveIndexTo(tokens, index, '</letStatement>')
    
    return index

ifCounter = 0


def compileIf(tokens, index):
    global ifCounter
    
    ifelse = containsElse(tokens, index)
    
    index = moveIndexTo(tokens, index, '<expression>')
    
    index = compileExpression(tokens, index)
    
    trueLabel = 'IF_TRUE' + str(ifCounter)
    trueEnd = 'IF_END' + str(ifCounter)
    falseLabel = 'IF_FALSE' + str(ifCounter)
    ifCounter += 1
    
    writeStatement('if-goto', trueLabel)
    writeStatement('goto', falseLabel)
    writeStatement('label', trueLabel)
    
    index = moveIndexTo(tokens, index, '<statements>')
    index = compileStatements(tokens, index)
    
    # doesn't matter if we keep this but its a small
    # optimization
    if ifelse:
        writeStatement('goto', trueEnd)
        
    writeStatement('label', falseLabel)
    
    if ifelse:
        index = moveIndexTo(tokens, index, '<statements>')
        index = compileStatements(tokens, index)
    
        writeStatement('label', trueEnd)
    
    index = moveIndexTo(tokens, index, '</ifStatement>')
        
    return index

Label_counter = 0

def compileWhile(tokens, index):
    global Label_counter
    whileLabel = 'WHILE_EXP' + str(Label_counter)
    whileEndLabel = 'WHILE_END' + str(Label_counter)
    Label_counter += 1
    
    # write the loop label
    writeStatement('label', whileLabel)
    
    index = moveIndexTo(tokens, index, '<expression>')
    
    index = compileExpression(tokens, index)
    
    # invert the expression
    writeArithmetic('not')
    
    # 1. goto the escape loop label if expression is true
    writeStatement('if-goto', whileEndLabel)
    
    index = moveIndexTo(tokens, index, '<statements>')
    
    index = compileStatements(tokens, index)
    
    # 2. LOOP !!!
    writeStatement('goto', whileLabel)
    
    # write escape loop label
    writeStatement('label', whileEndLabel)
    
    index = moveIndexTo(tokens, index, '</whileStatement>')
    
    return index


def compileDo(tokens, index):
    # move index to subroutine Name (thank me latter)
    index += 5
    
    index = compileSubroutineCall(tokens, index)
    
    # pop temp 0
    writeCommand('pop', 'temp', '0')
    
    return index


def compileReturn(tokens, index):
    # move to expression or symbol
    index += 4
    
    if tokens[index] == '<expression>':
        index = compileExpression(tokens, index)
        
        # probably move to symbol
        index += 1
    else:
        writeCommand('push', 'constant', '0')
    
    writeReturn()
    
    # move to </returnStatement>
    index = moveIndexTo(tokens, index, '</returnStatement>')
    
    return index

# I may have to change the compileSubroutines to include
# pushing the object to the stack for draw()
def compileSubroutineCall(tokens, index):
    # push the object (at least find the info about it)
    type, name2, segment, num = varType(tokens[index])
    
    index, name, pushObject = compileSubroutineName(tokens, index)

    Nargs = 0
    if pushObject:
        writeCommand('push', 'pointer', '0')
        Nargs += 1
    else:
        # is were calling a game.run instead of on the orig class
        # for example not SquareGame.run
        if name2 != '':
            writeCommand('push', segment, str(num))
            Nargs += 1
    
    # first we eval some expression
    Nargs = Nargs + compileExpressionList(tokens, index)
    
    # call function
    writeCall(name, str(Nargs))
    
    index = moveIndexTo(tokens, index, '</expressionList>')
    
    return index

# helper subroutine function that seperates a draw() from a object.draw() call
def compileSubroutineName(tokens, index):
    # just tells us if its a object call
    pushObject = False
    
    # draw()
    if tokens[index + 3] == '(':
        name = currentClass + '.' + tokens[index]
        pushObject = True
    # something.something()
    else:
        name = varType(tokens[index])[1]
        
        if name == '':
            name = tokens[index]
            
        name = name + '.' + tokens[index + 6]
    
    index = moveIndexTo(tokens, index, '<expressionList>')
     
    return index, name, pushObject


def compileExpression(tokens, index):
    # move to first part of the expression
    index += 1
    termCounter = 0
    opsCounter = 0
    
    while tokens[index] != '</expression>':
        if tokens[index] == '<term>':
            index = compileTerm(tokens, index)
            termCounter += 1
                
        if tokens[index] == '<symbol>' and tokens[index + 1] != ')' and tokens[index + 1] != '(':
            # save the + - * or whatever
            LastOp = tokens[index + 1]
            opsCounter += 1
        
        if termCounter > 1 and opsCounter > 0:
            writeArithmetic(LastOp)
            termCounter -= 1
            opsCounter -= 1

        index += 1
    
    return index

# TODO: fix / add priority to lists
def compileTerm(tokens, index):
    # move to term type
    index += 1
    
    if tokens[index] == '<integerConstant>':
        writeCommand('push', 'constant', tokens[index + 1])
        index += 2
        
    if tokens[index] == '<stringConstant>':
        compileString(tokens[index + 1])
        index += 2

    if tokens[index] == '<keyword>':
        PushKeywordConst(tokens[index + 1])
        index += 2
        
    if tokens[index] == '<symbol>':
        opToken = tokens[index + 1]
        
        # if term is UrnaryOp + Term --> compileTerm then push op
        if opToken == '-' or opToken == '~':
            index = moveIndexTo(tokens, index, '<term>')
            index = compileTerm(tokens, index)
            
            if opToken == '-':
                writeArithmetic('neg')
            elif opToken == '~':
                writeArithmetic('not')
                
        # if term is (expr) --> call compileExpression
        elif opToken == '(':
            index = moveIndexTo(tokens, index, '<expression>')
            index = compileExpression(tokens, index)

    # NOTE: There is likely a issue here
    if tokens[index] == '<identifier>':
        index += 1
        
        type, name, segment, num = varType(tokens[index])
        
        # if type == subroutineCall
        # NOTE: idk whats going on here tbh
        if tokens[index + 3] == '(' or tokens[index + 3] == '.':
            index = compileSubroutineCall(tokens, index)
        else:
            # push the symbol
            writeCommand('push', segment, str(num))
            
            # logic for arrays: '(' added for logic
            if tokens[index + 3] == '[':
                index = compileExpression(tokens, index + 5)
                
                # add to get the arr + expression address
                writeArithmetic('add')
                #pop pointer 1 // THAT = address of b[j]
                writeCommand('pop', 'pointer', '1')
                #push that 0 // stack top = b[j]
                writeCommand('push', 'that', '0')
                
            index = moveIndexTo(tokens, index, '</term>')

    return index


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
    # number of aguments going into a function || tracked by commas
    Nargs = 0
    
    # move to end of expression list
    while tokens[index] != '</expressionList>':
        # compile first expression
        if tokens[index] == '<expression>':
            index = compileExpression(tokens, index)
            Nargs += 1
            
        index += 1
        
    return Nargs


def main(file, save_file_name):
    tokens = readXML(file)
    
    GlobalSymbolTable(tokens)
    print(GlobalVariables)
    
    compileClass(tokens, 0)
    
    f = open(save_file_name + '.vm', "w")
    
    f.writelines(VMcode)
    
    f.close()
    
    return

# normal
#xml_file_path = "Square/noIndents.xml"   
#save_file_name = 'Square/Square'

# for debugging
xml_file_path = "/Users/lindageer/Projects/nand2tetris/Nand2tetris/projects/11/Pong/noIndents.xml"   
save_file_name = '/Users/lindageer/Projects/nand2tetris/Nand2tetris/projects/11/Pong/Ball'

main(xml_file_path, save_file_name)

#NOTE: we need to throw away the subroutine level 
# symbol table each time we start compiling a new subroutine