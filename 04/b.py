f = open('input.txt', 'r')

output = 0
cardCountArray = []

for line in f:
    try:
        multiplier = 1 + cardCountArray.pop(0)
    except:
        multiplier = 1

    output += multiplier
    matches = 0
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
                matches += 1

    for i in range(matches):
        if i < len(cardCountArray):
            cardCountArray[i] = cardCountArray[i] + multiplier
        else:
            cardCountArray.append(multiplier)

print(output)