import sys
import math
cnt = 0
room = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
n, k = map(int,sys.stdin.readline().split())
for _ in range(n):
    s, y = map(int, sys.stdin.readline().split())
    room[s][y-1] += 1
for i in room:
    for j in i:
        cnt += math.ceil(j/k)
print(cnt)