f = open('input.txt', 'r')

numStrings = { 
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine': '9'
}

output = 0

for line in f:
    nums = []
    for test in numStrings:
        a = line.rfind(test)
        b = line.find(test)
        if a != -1 and b != -1:
            nums.append((numStrings[test], a))
            nums.append((numStrings[test], b))
    for index, char in enumerate(line):
        if char.isnumeric():
            nums.append((char, index))
    nums.sort(key=lambda x:x[1])
    output += int(nums[0][0] + nums[-1][0])
    
print(output)