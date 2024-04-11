import re

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
    
    return tokens
