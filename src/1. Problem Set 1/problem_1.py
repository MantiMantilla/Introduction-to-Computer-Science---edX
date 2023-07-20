# s = "azcbobobegghakl"

vowels = "aeiou"

counter = 0

for ch in s:
    if ch in vowels:
        counter += 1

print("Number of vowels:", counter)
