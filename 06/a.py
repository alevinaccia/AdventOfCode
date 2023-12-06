f = open("input.txt", "r")

times = []
distances = []

output = 1

for line in f:
    if line.startswith("Time"):
        times = line.split(":")[1].split()
    elif line.startswith("Distance"):
        distances = line.split(":")[1].split()
        
for i, time in enumerate(times):
    n = 0
    for t in range(int(time)):
        accelleration = t #mm/s
        remainingTime = int(time) - accelleration
        dist = accelleration * remainingTime
        if dist > int(distances[i]):
            n += 1
    output *= n

print(output)
