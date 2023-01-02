key = input("Masukkan key: ")
s = [x for x in range(256)]
j = 0
key = [ord(x) for x in key]

for i in range(len(s)):
    j = (j + s[i] + int(key[i % len(key)])) % 256
    s[i], s[j] = s[j], s[i]
print(s)
