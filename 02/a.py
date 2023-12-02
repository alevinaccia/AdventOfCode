f = open('input.txt', 'r')
redMax = 12
greenMax = 13
blueMax = 14

output = 0

for game in f:
    isGamePossible = True
    g = game.split(':')
    gameID = g[0][5::]
    hands = g[1].split(';')
    for hand in hands:
        dices = hand.split(',')
        
        for dice in dices:
            i = dices.find('blue')
            if(i != -1):
                numberOfDices = int(dices[0:i])
                if(numberOfDices > blueMax):
                    isGamePossible = False
                    break
                continue
            i = dices.find('red')
            if(i != -1):
                numberOfDices = int(dices[0:i])
                if(numberOfDices > redMax):
                    isGamePossible = False
                    break
                continue
            i = dices.find('green')
            if(i != -1):
                numberOfDices = int(dices[0:i])
                if(numberOfDices > greenMax):
                    isGamePossible = False
                    break
                continue
        if(not isGamePossible):
            break
    if(isGamePossible):
        output += int(gameID)

print(output)
           
            
