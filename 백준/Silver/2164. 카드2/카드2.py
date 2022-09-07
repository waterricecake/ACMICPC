import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque()

for i in range(n):
    q.append(i+1)

while len(q)!=1:
    q.popleft()
    q.append(q.popleft())

print(q[0])