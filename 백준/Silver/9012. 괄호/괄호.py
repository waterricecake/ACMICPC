import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    vps = str(sys.stdin.readline().rstrip())
    s = []
    for w in vps:
        if w == "(":
            s.append(w)
        else:
            if not s:
                s.append(w)
                break
            s.pop()
    if s:
        print('NO')
    else:
        print('YES')