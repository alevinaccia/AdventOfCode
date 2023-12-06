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

f = """seeds: 79 14 45 13

seed-to-soil map:
50 98 2
52 50 48

""".splitlines()



#f = open("input.txt", 'r')

seedInput = []
seeds = []
ranges = []
changeMap = []

for line in f:
    if seedInput == []:
        seedInput = [int(e) for e in line.split(":")[1].split()]
        seeds = seedInput[0::2] #even for the seeds
        ranges = seedInput[1::2] #odd for the ranges
        changeMap = [False for i in seeds] #one entry per seed

    elif any(char.isdigit() for char in line):
        nums = line.split()
        source = int(nums[1])
        destination = int(nums[0])
        range = int(nums[2])
        for i, seed in enumerate(seeds):
            if seed >= source and seed + ranges[i] <= source + range - 1 and not changeMap[i]:
                seeds[i] = destination + (seed - source)
                changeMap[i] = True

    elif line == '':
        print(changeMap)
        changeMap = [False for e in changeMap]
        print(seeds)
        print("---")
    
#print(min(seedInput))
""" s   r  s  r
79 14 45 13

seed-to-soil map:
50 98 2
52 50 3 """