n = bin(int(raw_input()))[2:][::-1]
val = 0
for i in range(len(n)):
    val += int(n[i]) * (4**i)
print(val)
