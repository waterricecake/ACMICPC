import sys
from collections import deque
while True:
    s = sys.stdin.readline().rstrip()
    if s =='.':
        break
    result = "no"
    q = deque()
    for word in s:
        if word =="(" or word =="[":
            q.append(word)
        elif word ==")":
            if not q or q[-1] == "[":
                q.append(0)
                break
            else:
                q.pop()
        elif word =="]":
            if not q or q[-1] =="(":
                q.append(0)
                break
            else:
                q.pop()
    if not q:
        result = "yes"
    print(result)