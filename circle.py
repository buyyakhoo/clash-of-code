import math

# n = int(input())
# r = int(input())

# for y in range(n):
#     for x in range(n):
#       print('x', end=' ')

#other people code
l=[]
n = int(input()) # n x n square
for i in range(n):
    l.append(["."]*n)
r = int(input()) #radius of circle

c = n//2
for y in range(n):
    for x in range(n):
        d = math.sqrt((x-c)**2 + (y-c)**2)
        if d <= r:
            l[y][x] = "#"

for x in l:
    print(*x)
