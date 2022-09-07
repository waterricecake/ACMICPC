import sys
from collections import deque


n,m = map(int,sys.stdin.readline().rstrip().split())
array = list(map(int,sys.stdin.readline().rstrip().split()))

q = deque(list(range(1,n+1)))
cnt = 0
for cmd in array:
    if q[0] != cmd:
        c_l =-1
        c_r = 0
        while cmd != q[c_l]:
            c_l -=1
        while cmd != q[c_r]:
            c_r +=1
        if abs(c_r) > abs(c_l):
            turn = c_l
        else:
            turn = c_r
        q.rotate(-turn)
        cnt += abs(turn)
    q.popleft()
print(cnt)