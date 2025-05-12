#putting important commands here for later
#ord(single character) returns unicode value
#chr opposite of above

#EXAMPLE FROM INTERNET
s = "GeeksforGeeks"
freq = {}

for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

print(freq)
