import sys
n = int(sys.stdin.readline())
result = [None] * n
for _ in range(n):
    a, b = sys.stdin.readline().split()
    a = list(a)
    b = list(b)
    if len(a) != len(b):
        result[_] = "Impossible"
        continue
    for x in a:
        for i in range(len(b)):
            if b[i] == x:
                b.pop(i)
                break
    if b:
        result[_] ="Impossible"
    else:result[_] = "Possible"
for s in result:
    print(s)