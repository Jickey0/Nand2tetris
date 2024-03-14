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

def compileClass(myTokens):
    token = myTokens.pop(0)
    
    return

def main(file_path, save_path):
    myCode = removeComments(file_path)

    tokened_code = adv2(myCode)

    tokened_code = remove_empty_strings(tokened_code)
    #print(tokened_code)

    f = open(save_path + 'output.xml', "w")
    f.write('<tokens>\r\n')
    
    for token in tokened_code:
        type = tokenType(token)
        
        # remove "" from strings
        if type == "stringConstant":
            token = token[1:(len(token) - 1)]
        
        token = replaceSpecialChars(token)
        
        f.write('<' + type + '> ' + token + ' </' + type + '>' + '\r\n')
    
    f.write('</tokens>')
    f.close()

main("Square/Main.jack", "Square/")