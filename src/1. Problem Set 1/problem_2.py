# s = "azcbobobegghakl"

counter = 0

for pos in range(len(s)):
    if s[pos : pos + 3] == "bob":
        counter += 1

print(counter)
