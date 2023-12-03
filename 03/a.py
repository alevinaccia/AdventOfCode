f = open('input.txt' , 'r')

numbersLocations = []
symbolsLocations = []
lineLenght = 0
output = 0

for lineIndex, line in enumerate(f):
    n = ''
    first = True
    start = 0
    line = line.strip()
    lineLenght = len(line)
    lineNumbers = []
    for index, char in enumerate(line):
        if char.isnumeric():
            if first: 
                start = index
                first = False
            n += char
        elif char == '.':
            if(not first):
                lineNumbers.append((int(n), start, index - 1))
                first = True
            start = 0
            n = ''
        else:
            if(not first):
                lineNumbers.append((int(n), start, index - 1))
                first = True
            start = 0
            n = ''
            symbolsLocations.append((lineIndex, index))
    if(not first):
        lineNumbers.append((int(n), start, lineLenght - 1))

            
    numbersLocations.append(lineNumbers)

# symbol = (line, index)

for symbol in symbolsLocations:
    # check for the row above
    if symbol[0] > 0:
        for i, element in enumerate(numbersLocations[symbol[0] - 1]):
            if element == []: continue
            lowerBound = max(element[1] - 1, 0)
            upperBound = min(element[2] + 1, lineLenght)
            if symbol[1] >= lowerBound and symbol[1] <= upperBound:
                output += element[0]
                numbersLocations[symbol[0] - 1][i] = []
    #check on the same row
    for i, element in enumerate(numbersLocations[symbol[0]]):
        if element == []: continue
        if element[2] == symbol[1] - 1 or element[1] - 1 == symbol[1]:
            output += element[0]
            numbersLocations[symbol[0]][i] = []
    #check for the bottom row
    if symbol[0] == len(numbersLocations) -1: continue
    for i, element in enumerate(numbersLocations[symbol[0] + 1]):
        if element == []: continue
        lowerBound = max(element[1] - 1, 0)
        upperBound = min(element[2] + 1, lineLenght)
        if symbol[1] >= lowerBound and symbol[1] <= upperBound:
            output += element[0]
            numbersLocations[symbol[0] + 1][i] = []

print(output)