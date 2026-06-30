# Store frequency in a dictionary
freq_map = dict()
# freq_map = {}
nums = [5, 6, 7, 8, 7, 6, 5, 4, 3, 6, 7 ,8]

# iterate krege
for i in range (0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)
# to find how mant times a specific number came
print(freq_map[5])