# using get - get is a dictionary method in python
nums = [8, 3, 5, 8, 2, 3, 8, 9, 5, 2, 2, 1]
hash_map = dict()
n = len(nums)
for i in range (0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

print(hash_map)