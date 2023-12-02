f = open('input.txt', 'r')

output = 0

for row in f:
    game = row.split(':')[1]
    hands = game.split(';')
    minRed = 0 
    minBlue = 0
    minGreen = 0
    for hand in hands:
        dices = hand.split(',')
        for dice in dices:
            i = dice.find('blue')
            if(i != -1):
                numberOfDices = int(dice[0:i])
                if(numberOfDices > minBlue):
                    minBlue = numberOfDices
                continue
            i = dice.find('red')
            if(i != -1):
                numberOfDices = int(dice[0:i])
                if(numberOfDices > minRed):
                    minRed = numberOfDices
                continue
            i = dice.find('green')
            if(i != -1):
                numberOfDices = int(dice[0:i])
                if(numberOfDices > minGreen):
                    minGreen = numberOfDices
                continue
    power = minGreen * minRed * minBlue
    output += power

print(output)