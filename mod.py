m = int(input())
n = int(input())
r = 0
for i in input().split():
    r += int(i)%m
print(r)
