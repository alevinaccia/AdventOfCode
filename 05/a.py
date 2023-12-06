f = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".splitlines()

#f = open("input.txt", 'r')

seedInput = []
changeMap = []

for line in f:
    if seedInput == []:
        seedInput = [int(e) for e in line.split(":")[1].split()]
        changeMap = [False for i in seedInput]

    elif any(char.isdigit() for char in line):
        nums = line.split()
        source = int(nums[1])
        destination = int(nums[0])
        range = int(nums[2])
        #print(f's{source}:{source+range -1}, d{destination}:{destination+range -1}')
        for i, seed in enumerate(seedInput):
            if seed >= source and seed <= source + range - 1 and not changeMap[i]:
                seedInput[i] = destination + (seed - source)
                changeMap[i] = True
    elif line == "\n":
        changeMap = [False for e in changeMap]
    
print(min(seedInput))

