import math

def removeComments(file):
    f = open(file, "r")
    
    textNoComments = []
    currentLine = ''
    previous_char = ''
    ignore_lines = False # meant for /* comments */
    quotes = False # meant for preserving spacing in quotes
    
    final_result = ''
    last_char = ''
    
    for line in f:
        for i in range(len(line)):
            if line[i] == '"' and quotes == False:
                #print('yippe ' + str(i))
                quotes = True
            elif line[i] == '"' and quotes == True:
                quotes = False
                #print('NO! ' + str(i))
            
            if len(line) != i - 1: # must check so we don't go over
                if line[i] == '/' and line[i + 1] == '/': # double //
                    break
                
                # meant for ending a */ comment
                if line[i] == '/':
                    if ignore_lines:
                        ignore_lines = False
                        continue
                
                if line[i] == '/' and line[i + 1] == '*': # if /*
                    ignore_lines = True
                
                if not ignore_lines:
                    if line[i] == ' ' and last_char == ' ':
                        continue
                    elif line[i] == ' ' and i == 0:
                        continue 
                    else:
                        currentLine = currentLine + line[i]
    
            else:
                if line[i] == '/':
                    ignore_lines = False
                
                if not ignore_lines and line[i] != ' ':
                    currentLine = currentLine + line[i]
            
            last_char = line[i]

        if quotes == False:
            currentLine = currentLine.replace('\r\n', '').replace('\n', '')
            print(currentLine)
            #words = currentLine.split(" ")
            #words = ' '.join(words).split()
            #textNoComments.append(words)
        
        currentLine = ''  
    
    filtered_list = [sublist for sublist in textNoComments if sublist]
    return filtered_list

# turns the 2d array into a 1d array
def flatten_array(arr):
    result = []
    for line in arr:
        for part in line:
            result.append(part)
            
    return result

keywords = ["class", "constructor", 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']

symbol = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']

# advance returns the current word and what is left from looping
def advance(str):
    token = ''
    for i in range(len(str)):
        if str[i] not in symbol:
            token = token + str[i]
        else:
            if len(token) == 0: # we immediately have a symbol
                return (str[i], str[i + 1:])
            else: # encounter a symbol but already have a token
                return (token, str[i:])
    
    return (token, '') # reach the end of the str

# does nothing
def parse(str):
    while len(str) != 0:
        return
    return
        


myCode = removeComments("ArrayTest/Main.jack")
print(myCode)

# TODO: fix "HOW', 'MANY', 'NUMBERS?', '" error
#for str in myCode:
#    while len(str) != 0:
#        result = advance(str)
#        token = result[0]
#       str = result[1]
#        print(token)