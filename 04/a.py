f = open('input.txt', 'r')

output = 0

for line in f:
    lineScore = 0
    input = line.split(":")[1]
    numbers = input.strip().split("|")
    winningNumbers = numbers[0].split(" ")[:-1:]
    playedNumbers = numbers[1].split(" ")[1::]

    for element in playedNumbers:
        if element == '':
            playedNumbers.remove(element)
    
    playedNumbers = [int(element) for element in playedNumbers]
    
    for element in winningNumbers:
        if element != '':
            if int(element) in playedNumbers:
                lineScore += 1

    if(lineScore > 0): 
        output += pow(2, lineScore - 1)

print(output)