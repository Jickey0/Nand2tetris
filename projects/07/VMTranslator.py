# removes whitespace and turns our stuff into a list
def parser(file):
    f = open(file, "r")
    
    textNoComments = []
    currentLine = ''
    
    for line in f:
        for char in line:
            if char != "/":
                currentLine = currentLine + char
            else:
                break
        
        currentLine = currentLine.replace('\r\n', '').replace('\n', '')
        words = currentLine.split(" ")
        words = ' '.join(words).split()
        textNoComments.append(words)
        
        currentLine = ''  
    
    filtered_list = [sublist for sublist in textNoComments if sublist]
    return filtered_list

# loops and calls encodeLine
def encodeText(text):
    global textCounter
    result = []
    for line in text:
        result.append(encodeLine(line))
    textCounter += 1
    return result

# does confusing shit
def encodeLine(line):
    
    if line[0] == 'push':
        if line[1] == 'constant':   
            result = readCommands('TextCommands/pushConst.txt') 
        elif line[1] == 'static' or line[1] == 'temp' or line[1] == 'pointer':
            result = readCommands('TextCommands/pushStatic.txt')
        else:
            result = readCommands('TextCommands/push.txt') 
            
        result = result.replace('i', line[2]).replace('LOCATION', locations[line[1]])
        result = result.replace('static', 'static' + str(textCounter) + 'Var' + str(line[2]))
        
    elif line[0] == 'pop':
        if line[1] == 'static' or line[1] == 'temp': 
            result = readCommands('TextCommands/popStatic.txt')
        elif line[1] == 'pointer':
            result = readCommands('TextCommands/popPointer.txt') 
            if line[2] == '0':
                result = result.replace('i', 'THIS')
            else:
                result = result.replace('i', 'THAT')
        else:
            result = readCommands('TextCommands/pop.txt') 
            
        result = result.replace('i', line[2]).replace('LOCATION', locations[line[1]])
        result = result.replace('static', 'static' + str(textCounter) + 'Var' + str(line[2]))
        
    else:
        result = readCommands('TextCommands/' + line[0] + '.txt')
        
        if len(line) > 1:
            result = result.replace("LABEL", line[1]) # only needed for labels
            
        result = replaceVals(result)
    
    if line[0] == 'function':
        result = replaceFunction(line, result)
    if line[0] == 'call':
        result = replaceCall(line, result)
    
    return result
      
# saves file... duh  
def saveFile(file, text):
    f = open(file, 'w')
    for row in text:
        f.write(row)
    return

# helper function for instruction txt files
def readCommands(file):
    f = open(file, 'r')
    result = ''
    for x in f:
        result = result + x
    return result

def replaceFunction(line, text):
    global replacementCounter
    text = text.replace("i", line[2]).replace('FUNCTION', line[1]).replace('ZEROLOOP', 'ZEROLOOP' + str(replacementCounter)).replace('ENDZEROLOOP', 'ENDZEROLOOP' + str(replacementCounter))
    replacementCounter += 1
    return text

def replaceCall(line, text):
    global replacementCounter
    text = text.replace("retAddrLabel", 'retAddrLabel' + str(replacementCounter)).replace('FUNCTION', line[1]).replace('NARGS', line[2])
    replacementCounter += 1
    return text

# changes/replaces varible names
def replaceVals(text):
    global replacementCounter
    text = text.replace("FOO", "FOO" + str(replacementCounter)).replace("BAR", "BAR" + str(replacementCounter))
    replacementCounter += 1
    return text

# changes varible names so no errors
replacementCounter = 0

textCounter = 0
textVarCounter = 0

locations = {
    'local': 'LCL',
    'argument': 'ARG',
    'this': 'THIS',
    'that': 'THAT',
    'constant': 'SP',
    'temp': '5',
    'static': 'static',
    'pointer': 'THIS',
}


# import required module
import os
# assign directory
directory = 'FunctionCalls/StaticsTest'
filesToTranslate = []
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f) and f[-1] == 'm' and f[-2] == 'v':
        filesToTranslate.append(f)

parsedFiles = []
for file in filesToTranslate:
    parsedFiles.append(parser(file))

encodedText = ''

# set up the SP and call sys.init
encodedText = encodedText + str(readCommands('TextCommands/setSP.txt'))
encodedText = encodedText + str(encodeLine(['call', 'Sys.init', '0']))

for file in parsedFiles:
    encodedFile = encodeText(file)
    for line in encodedFile:
        encodedText = encodedText + str(line)

#print(file)
saveFile(directory + '/StaticsTest.asm', encodedText)