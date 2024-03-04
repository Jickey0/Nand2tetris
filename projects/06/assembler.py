# this could have been done much better
def RemoveSpaces(text):
    result = []
    line = ''
    for i in range(len(text)):
        for char in text[i]:
            if char == '/':
                break
            if char != ' ' and char != '\r\n':
                line = line + char
        
        if len(line) > 0:
            result.append(line)
        line = ''
        
    return result

def FindSymbols(text):
    symbol_counter = 0
    new_list = []
    for i in range(len(text)):
        if text[i][0] == '(':
            symbol = text[i][1:len(text[i]) - 1]
            Symbols[symbol] = i - symbol_counter
            symbol_counter += 1
        else:
            new_list.append(text[i])

    return new_list

def ReplaceSymbols(text):
    counter = 16
    result = []
    for line in text:
        if line[0] == '@' and line[1:len(line)].isdigit() == False:
            if line[1:len(line)] in Symbols:
                result.append('@' + str(Symbols[line[1:len(line)]]))
            else:
                while counter in list(Symbols.values()):
                    counter += 1
                Symbols[line[1:len(line)]] = counter
                result.append('@' + str(Symbols[line[1:len(line)]]))             
        else:
            result.append(line)
            
    return result
            
def Encode(text):
    result = []
    for line in text:
        if line[0] == '@':
            result.append(Ainstruction(line))
        else:
            result.append(Cinstruction(line))
 
    return result

def Ainstruction(line):
    line = line[1:len(line)]
    binary = '0' + str(bin(int(line)).replace("0b", "").zfill(15))
    return binary

def Cinstruction(line):
    part = ''
    dest_exist = False
    comp_exist = False
    jval = '000'
    destval = '000'
    
    for i in range(len(line)):
        if line[i] == '=':
            dest_exist = True
            destval = dest[part]
            part = ''
            continue
        if line[i] == ';':
            comp_exist = True
            cval = comp[part]
            if 'M' in part:
                aval = 1
            else:
                aval = 0
            part = ''
            continue
        if i == len(line) - 1 and comp_exist == False:
            part = part + line[i]
            comp_exist = True
            cval = comp[part]
            if 'M' in part:
                aval = 1
            else:
                aval = 0
            part = ''
            continue
        if i == len(line) - 1:
            part = part + line[i]
            jval = jump[part]
            continue
            
        part = part + line[i]
    
    return '111' + str(aval) + str(cval) + str(destval) + str(jval)
            
comp = {
    "0" : "101010",
    "1" : "111111",
    "-1" : "111010",
    "D" : "001100",
    "A" : "110000",
    "M" : "110000",
    "!D" : "001101",
    "!A" : "110001",
    "!M" : "110001",
    "-D" : "001111",
    "-A" : "110011",
    "-M" : "110011",
    "D+1" : "011111",
    "A+1" : "110111",
    "M+1" : "110111",
    "D-1" : "001110",
    "A-1" : "110010",
    "M-1" : "110010",
    "D+A" : "000010",
    "D+M" : "000010",
    "D-A" : "010011",
    "D-M" : "010011",
    "A-D" : "000111",
    "M-D" : "000111",
    "D&A" : "000000",
    "D&M" : "000000",
    "D|A" : "010101",
    "D|M" : "010101"
}

dest = {
    'M' : '001',
    'D' : '010',
    'DM' : '011',
    'MD' : '011',
    'A' : '100',
    'AM' : '101',
    'AD' : '110',
    'ADM' : '111'
}

jump = {
    'JGT' : '001',
    'JEQ' : '010',
    'JGE' : '011',
    'JLT' : '100',
    'JNE' : '101',
    'JLE' : '110',
    'JMP' : '111'
}

Symbols = {
'R0' : '0',
'R1' : '1',
'R2' : '2',
'R3' : '3',
'R4' : '4',
'R5' : '5',
'R6' : '6',
'R7' : '7',
'R8' : '8',
'R9' : '9',
'R10' : '10',
'R11' : '11',
'R12' : '12',
'R13' : '13',
'R14' : '14',
'R15' : '15',
'SCREEN' : '16384',
'KBD' : '24576',
'SP' : '0',
'LCL' : '1',
'ARG' : '2',
'THIS' : '3',
'THAT' : '4'
}

text = []    
f = open("pong/Pong.asm", "r")
for x in f:
    new_line = x.replace('\r\n', '')
    text.append(new_line)
f.close()

text_no_spaces = RemoveSpaces(text)
text_no_symbols = FindSymbols(text_no_spaces)
text_symbols_replaced = ReplaceSymbols(text_no_symbols)
result = Encode(text_symbols_replaced)

file = open("pong/MyPong.hack", "w")
for line in result:
    file.write(line + "\n")
file.close()
