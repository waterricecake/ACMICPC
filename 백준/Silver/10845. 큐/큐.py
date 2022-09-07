import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
q = deque()
result = []
for _ in range(n):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        if q:
            result.append(q.popleft())
        else:
            result.append(-1)
    elif cmd[0] == "size":
        result.append(len(q))
    elif cmd[0] =="front":
        if q:
            result.append(q[0])
        else:
            result.append(-1)
    elif cmd[0] == "back":
        if q:
            result.append(q[-1])
        else:
            result.append(-1)
    elif cmd[0] =="empty":
        if q:
            result.append(0)
        else:
            result.append(1)
for i in result:
    print(i)