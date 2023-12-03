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
        elif char == '*':
            if(not first):
                lineNumbers.append((int(n), start, index - 1))
                first = True
            start = 0
            n = ''
            symbolsLocations.append((lineIndex, index))
        else:
            if(not first):
                lineNumbers.append((int(n), start, index - 1))
                first = True
            start = 0
            n = ''
    if(not first):
        lineNumbers.append((int(n), start, lineLenght - 1))

            
    numbersLocations.append(lineNumbers)

# symbol = (line, index)

for symbol in symbolsLocations:
    numberOfConnections = 0
    numbers = []
    # check for the row above
    if symbol[0] > 0:
        for i, element in enumerate(numbersLocations[symbol[0] - 1]):
            lowerBound = max(element[1] - 1, 0)
            upperBound = min(element[2] + 1, lineLenght)
            if symbol[1] >= lowerBound and symbol[1] <= upperBound:
                numberOfConnections += 1
                numbers.append(element[0])
    #check on the same row
    for i, element in enumerate(numbersLocations[symbol[0]]):
        if element[2] == symbol[1] - 1 or element[1] - 1 == symbol[1]:
            numberOfConnections += 1
            numbers.append(element[0])
    #check for the bottom row
    if symbol[0] == len(numbersLocations) -1: continue
    for i, element in enumerate(numbersLocations[symbol[0] + 1]):
        lowerBound = max(element[1] - 1, 0)
        upperBound = min(element[2] + 1, lineLenght)
        if symbol[1] >= lowerBound and symbol[1] <= upperBound:
            numberOfConnections += 1
            numbers.append(element[0])
    if numberOfConnections == 2:
        output += numbers[0] * numbers[1]

print(output)