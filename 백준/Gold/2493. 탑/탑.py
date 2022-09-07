import sys


n = int(sys.stdin.readline().rstrip())

tower = list(map(int,sys.stdin.readline().rstrip().split()))
s = [[100000000,0]]
result = [0] *n
for i in range(n):
    h = tower[i]
    while s:
        if s[-1][0] < h:
            s.pop()
        else:
            break
    result[i] = s[-1][1]
    s.append([tower[i],i+1])

print(*result)