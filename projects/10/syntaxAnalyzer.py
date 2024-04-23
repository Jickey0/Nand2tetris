# this was so painful
def removeComments(file):
    f = open(file, "r")
    result = ''
    
    ignore_lines = False
    e = []
    
    for line in f:
        currentLine = ' '.join(line.split())
        currentLine = currentLine.replace('\r\n', '').replace('\n', '')
        
        i = 0
        while i < len(currentLine):
            if i + 1 < len(currentLine) and currentLine[i] == '/' and currentLine[i + 1] == '/': # double //
                break
                
            if i + 1 < len(currentLine) and currentLine[i] == '/' and currentLine[i + 1] == '*': # starting a /* comment
                ignore_lines = True
                i += 1
                
            if not ignore_lines:
                result = result + currentLine[i]
            
            if i + 1 < len(currentLine) and currentLine[i] == '*' and currentLine[i + 1] == '/': # ending a */ comment
                ignore_lines = False
                i += 1
            
            i += 1
        
        for char in result:
            e.append(char)
        
        result = ''
        
    return(''.join(e))


keywords = ["class", "constructor", 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']

symbol = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
        
specialChars = {'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}


def adv2(text):
    token = ''
    strings = False
    token_dict = []
    
    for char in text:
        # string flip flop thing
        if char == '"' and strings == False:
            strings = True
        elif char == '"' and strings == True:
            strings = False
        
        # must be whitespace
        if char == ' ' and strings == False:
            token_dict.append(token)
            token = ''
            continue
        
        # write spaces
        elif char == ' ' and strings == True:
            token = token + char
            continue
        
        # write char
        elif char not in symbol:
            token = token + char
            continue

        # must be a symbol
        elif char in symbol and strings == False:
            if token != '':
                token_dict.append(token)
                token = ''
            token_dict.append(char)
            
    return token_dict


def remove_empty_strings(lst):
    return [item for item in lst if item != '']

# returns token type 
def tokenType(token):
    if token[0] == '"' and token[len(token) - 1] == '"':
        return 'stringConstant'
    if any(i.isdigit() for i in token):
        return 'integerConstant'
    if token in keywords:
        return 'keyword'
    if token in symbol:
        return 'symbol'
    else:
        return 'identifier'

# returns the current keyword which is the current token as a const
# only called if tokentype is KEYWORD
def keyWord(token):
    return token.upper()

# replaces normals chars with weird ones, because why not?
def replaceSpecialChars(str):
    result = ''
    
    for char in str:
        if char in specialChars:
            char = specialChars[char]
        
        result = result + char
    
    return result
    
# IMPORTANT --> How most tokens are saved
def writeToken(token, type, result):
    if type == 'stringConstant':
        token = token[1:(len(token) - 1)]
    
    token = replaceSpecialChars(token)
    result.append(('<' + type + '> ' + token + ' </' + type + '>'))
    return result

# TODO: add protective measures
def compileClass(myTokens, result):
    result.append('<class>')
    
    # class
    result = writeToken(myTokens.pop(0), 'keyword', result)
    
    # the immediate next token must be the classes name
    result = writeToken(myTokens.pop(0), 'identifier', result)
    
    # add the { symbol
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    # optional classVarDec
    result = compileClassVarDec(myTokens, result)
    
    # optional subroutineDec
    result = compileSubroutine(myTokens, result)
    
    # add the } symbol
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    result.append('</class>')
    
    return result

def compileClassVarDec(myTokens, result):
    while myTokens[0] == 'static' or myTokens[0] == 'field':
        result.append('<classVarDec>')
        
        result = writeToken(myTokens.pop(0), 'keyword', result)
        
        # could be keyword or identifer
        type = tokenType(myTokens[0])
        result = writeToken(myTokens.pop(0), type, result)
        
        # identifier
        result = writeToken(myTokens.pop(0), 'identifier', result)
        
        # while we don't encounter a ; must be a identifier
        while myTokens[0] != ';':
            if myTokens[0] == ',':
                result = writeToken(myTokens.pop(0), 'symbol', result)
            else:
                result = writeToken(myTokens.pop(0), 'identifier', result)
            
        # end ;
        result = writeToken(myTokens.pop(0), 'symbol', result)
        
        result.append('</classVarDec>')
        
    return result
            
def compileSubroutine(myTokens, result):
    while myTokens[0] == 'constructor' or myTokens[0] == 'function' or myTokens[0] == 'method':
        result.append('<subroutineDec>')
        
        result = writeToken(myTokens.pop(0), 'keyword', result)
        
        # could be keyword or identifer
        type = tokenType(myTokens[0])
        result = writeToken(myTokens.pop(0), type, result)
        
        # subroutineName
        result = writeToken(myTokens.pop(0), 'identifier', result)
        
        # (
        result = writeToken(myTokens.pop(0), 'symbol', result)
        
        result = parameterList(myTokens, result)
        
        # )
        result = writeToken(myTokens.pop(0), 'symbol', result)
        
        result = subroutineBody(myTokens, result)
        
        result.append('</subroutineDec>')

    return result
    
def subroutineBody(myTokens, result):
    result.append('<subroutineBody>')
    
    # {
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    while myTokens[0] == 'var':
        result = varDec(myTokens, result)
        
    result = statements(myTokens, result)
    
    # }
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    
    result.append('</subroutineBody>')
    return result
    
def statements(myTokens, result):
    result.append('<statements>')
    
    while myTokens[0] == 'let' or myTokens[0] == 'if' or myTokens[0] == 'while' or myTokens[0] == 'do' or myTokens[0] == 'return':
        token = myTokens[0]
        
        if token == 'let':
            result = letStatement(myTokens, result)
        if token == 'if':
            result = ifStatement(myTokens, result)
        if token == 'while':
            result = whileStatement(myTokens, result)
        if token == 'do':
            result = doStatement(myTokens, result)
        if token == 'return':
            result = returnStatement(myTokens, result)
    
    
    result.append('</statements>')
    
    return result

# --- <STATEMENTS> --- #       
def letStatement(myTokens, result):
    result.append('<letStatement>')
    
    # let
    result = writeToken(myTokens.pop(0), 'keyword', result)
    
    # varName
    result = writeToken(myTokens.pop(0), 'identifier', result)
    
    # optional index
    if myTokens[0] == '[':
        # [
        result = writeToken(myTokens.pop(0), 'symbol', result)
        
        result = expression(myTokens, result)
        
        # ]
        result = writeToken(myTokens.pop(0), 'symbol', result)
    
    # =
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    result = expression(myTokens, result)
    
    # ;
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    result.append('</letStatement>')
    
    return result

op = ['+', '-', '*', '/', '&', '|', '<', '>', '=']

# very cool
def expression(myTokens, result):
    result.append('<expression>')
    
    result = term(myTokens, result)
    
    while myTokens[0] in op:
        # op
        result = writeToken(myTokens.pop(0), 'symbol', result)
        
        # term
        result = term(myTokens, result)
    
    result.append('</expression>')
    return result

def term(myTokens, result):
    result.append('<term>')
    
    # find type
    type = tokenType(myTokens[0])
    
    if type == 'integerConstant':
        result = writeToken(myTokens.pop(0), 'integerConstant', result)
        
    if type == 'stringConstant':
        result = writeToken(myTokens.pop(0), 'stringConstant', result)
        
    # keywordConstant
    if myTokens[0] == 'true' or myTokens[0] == 'false' or myTokens[0] == 'null' or myTokens[0] == 'this':
        result = writeToken(myTokens.pop(0), 'keyword', result)
        
    # varName or subroutineCall
    if type == 'identifier':
        
        # TODO: check this: subroutineCall
        if myTokens[1] == '(' or myTokens[1] == '.':
            result = subroutineCall(myTokens, result)
        
        # varname
        else:
            # varName
            result = writeToken(myTokens.pop(0), 'identifier', result)
            
            # optional index
            if myTokens[0] == '[':
                # [
                result = writeToken(myTokens.pop(0), 'symbol', result)
                
                result = expression(myTokens, result)
                
                # ]
                result = writeToken(myTokens.pop(0), 'symbol', result)
    
    # TODO: fix this (NAH WE GOOD)
    if type == 'symbol':
        # '(' expression ')'
        if myTokens[0] == '(':
            # (
            result = writeToken(myTokens.pop(0), 'symbol', result)
            
            result = expression(myTokens, result)
            
            # )
            result = writeToken(myTokens.pop(0), 'symbol', result)
            
        # unaryOp term
        else:
            # unaryOp
            result = writeToken(myTokens.pop(0), 'symbol', result)
            
            result = term(myTokens, result)
            
    result.append('</term>')
    
    return result
    
# TODO: make this
def subroutineCall(myTokens, result):
    # subroutineName | (className | varName)
    result = writeToken(myTokens.pop(0), 'identifier', result)
    
    if myTokens[0] == '(':
        # (
        result = writeToken(myTokens.pop(0), 'symbol', result)
        
        result = expressionList(myTokens, result)
        
        # )
        result = writeToken(myTokens.pop(0), 'symbol', result)
    else:
        # .
        result = writeToken(myTokens.pop(0), 'symbol', result)
        
        # subroutineName
        result = writeToken(myTokens.pop(0), 'identifier', result)
        
        # (
        result = writeToken(myTokens.pop(0), 'symbol', result)
        
        result = expressionList(myTokens, result)
        
        # )
        result = writeToken(myTokens.pop(0), 'symbol', result)
    
    return result
    
# TODO: fix the <symbol> being wrapped in <term>
def expressionList(myTokens, result):
    result.append('<expressionList>')
    
    if myTokens[0] != ')':
        result = expression(myTokens, result)
    
        # optional loop until we find the ')'
        while myTokens[0] == ',':
            # ,
            result = writeToken(myTokens.pop(0), 'symbol', result)
            
            # expression aka term
            result = expression(myTokens, result)
    
    result.append('</expressionList>')
    
    return result


# fuck this shit
def ifStatement(myTokens, result):
    result.append('<ifStatement>')
    
    # if
    result = writeToken(myTokens.pop(0), 'keyword', result)
    
    # (
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    result = expression(myTokens, result)
    
    # )
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    # {
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    result = statements(myTokens, result)
    
    # }
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    # optional 'else'
    if myTokens[0] == 'else':
        # else
        result = writeToken(myTokens.pop(0), 'keyword', result)
        
        # {
        result = writeToken(myTokens.pop(0), 'symbol', result)

        result = statements(myTokens, result)

        # }
        result = writeToken(myTokens.pop(0), 'symbol', result)
    
    result.append('</ifStatement>')
    
    return result    

    
def whileStatement(myTokens, result):
    result.append('<whileStatement>')
    
    # while
    result = writeToken(myTokens.pop(0), 'keyword', result)
    
    # (
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    result = expression(myTokens, result)
    
    # )
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    # {
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    result = statements(myTokens, result)
    
    # }
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    result.append('</whileStatement>')
    
    return result

    
def doStatement(myTokens, result):
    result.append('<doStatement>')
    
    # do
    result = writeToken(myTokens.pop(0), 'keyword', result)
    
    result = subroutineCall(myTokens, result)
    
    # ;
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    result.append('</doStatement>')
    
    return result

# TODO: make expression optional (DONE)
def returnStatement(myTokens, result):
    result.append('<returnStatement>')
    
    # return
    result = writeToken(myTokens.pop(0), 'keyword', result)
    
    if myTokens[0] != ';':
        result = expression(myTokens, result)
    
    # ;
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    result.append('</returnStatement>')
    
    return result
# --- </STATEMENTS> --- #   


def varDec(myTokens, result):
    result.append('<varDec>')
    
    # 'var'
    result = writeToken(myTokens.pop(0), 'keyword', result)
    
    # could be keyword or identifer
    type = tokenType(myTokens[0])
    result = writeToken(myTokens.pop(0), type, result)
    
    # identifier
    result = writeToken(myTokens.pop(0), 'identifier', result)
        
    # while we don't encounter a ; must be a comma and a identifier
    while myTokens[0] != ';':
        result = writeToken(myTokens.pop(0), 'symbol', result)
        result = writeToken(myTokens.pop(0), 'identifier', result)
            
    # end ;
    result = writeToken(myTokens.pop(0), 'symbol', result)
    
    
    result.append('</varDec>')
    return result


def parameterList(myTokens, result):
    result.append('<parameterList>')
    
    # loop optional parameters
    comma = False
    while myTokens[0] != ')':
        # comma seperate after first loop
        if comma == True:
            result = writeToken(myTokens.pop(0), 'symbol', result)
        
        # could be keyword or identifer
        type = tokenType(myTokens[0])
        result = writeToken(myTokens.pop(0), type, result)
        
        # varName
        result = writeToken(myTokens.pop(0), 'identifier', result)
            
        comma = True
        
    result.append('</parameterList>')
    
    return result

def containsHowMany(chr, str):
    counter = 0
    for c in str:
        if c == chr:
            counter += 1
            
    return counter

# CASES: <...> and </...>, <...>, </...>
# SO VERY BADLY MADE FUNCTION
def prettyPrint(input):
    doNothing = 0
    output = []
    current_line = ''
    indentCounter = 0
    for i in range(len(input)):
        if i != (len(input) - 1):
            for j in range(indentCounter):
                current_line = current_line + '  '
        
        current_line = current_line + input[i]
        
        if containsHowMany('<', input[i]) == 2:
            # TOP 10 Worst coding practices
            doNothing = 0
        elif '</' in input[i]:
            indentCounter -= 1
        else:
            indentCounter += 1
        
        output.append(current_line)
        current_line = ''
    
    return output

                
def main1(file_path, save_path):
    myCode = removeComments(file_path)

    tokened_code = adv2(myCode)

    tokened_code = remove_empty_strings(tokened_code)
    #print(tokened_code)

    f = open(save_path + 'output1.xml', "w")
    f.write('<tokens>\r\n')
    
    
    
    # print and write easy version of code (COMPLETE)
    for token in tokened_code:
        type = tokenType(token)
        
        # remove "" from strings
        if type == "stringConstant":
            token = token[1:(len(token) - 1)]
        
        token = replaceSpecialChars(token)
        
        f.write('<' + type + '> ' + token + ' </' + type + '>' + '\r\n')
    
    f.write('</tokens>')
    f.close()


def main2(folder, file):
    file_path = folder + '/' + file
    save_path = folder + '/'
    
    myCode = removeComments(file_path)

    tokened_code = adv2(myCode)

    tokened_code = remove_empty_strings(tokened_code)
    #print(tokened_code)
    
    result = []
    result = compileClass(tokened_code, result)
    
    #print(result)
    result = prettyPrint(result)
    
    f = open(file_path + '.xml', "w")
    
    for line in result:
        f.write(line + '\r\n')
    
    f.close()

#main1("ExpressionLessSquare", "square.jack")
main2("ExpressionLessSquare", "Square.jack")