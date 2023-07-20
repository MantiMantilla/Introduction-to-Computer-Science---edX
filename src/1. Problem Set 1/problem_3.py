# s = "azcbobobegghakl"

longest_len = 0
longest_str = ""


for pos_1 in range(len(s)):
    curr_len = 1
    curr_str = s[pos_1]
    for pos_2 in range(pos_1 + 1, len(s)):
        if s[pos_2] >= s[pos_2 - 1]:
            curr_len += 1
            curr_str += s[pos_2]
        else:
            break
    if curr_len > longest_len:
        longest_len = curr_len
        longest_str = curr_str

print("Longest substring in alphabetical order is:", longest_str)
