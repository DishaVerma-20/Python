s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

hash_list = [0] * 27

# ye possible hua hai kyuki jo s tha vo hmara srf small alhabets contain krta haii
for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(f"frequency of {ch}:-", hash_list[index], end = '\n')