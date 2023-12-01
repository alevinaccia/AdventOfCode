f = open("input.txt", "r")

output = 0

for line in f:
    nums = []
    for char in line:
        if char.isnumeric():
            nums.append(char)

    output += int(nums[0] + nums[-1]); 

print(output)