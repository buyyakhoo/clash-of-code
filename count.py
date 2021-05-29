s = input()
c = {}
for i in s:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
m = max(c, key=lambda key: c[key])
print(m, c[m])


