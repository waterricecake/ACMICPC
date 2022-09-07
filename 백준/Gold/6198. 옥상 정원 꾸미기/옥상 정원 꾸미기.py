import sys

n = int(sys.stdin.readline().rstrip())

result = 0
s = []
for i in range(n):
    h = int(sys.stdin.readline().rstrip())
    if s:
        while s[-1] <= h:
            s.pop()
            if not s:
                break
    result += len(s)
    s.append(h)
print(result)