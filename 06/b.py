f = open("input.txt", "r")

time = 0
distance = 0

for line in f:
    if line.startswith("Time"):
        time = int(''.join( n.strip() for n in line.split(":")[1]))
    elif line.startswith("Distance"):
        distance = int(''.join( n.strip() for n in line.split(":")[1]))

output = 0
for t in range(int(time)):
    accelleration = t #mm/s
    remainingTime = int(time) - accelleration
    dist = accelleration * remainingTime
    if dist > int(distance):
        output += 1
        

print(f'Output:{output}')
