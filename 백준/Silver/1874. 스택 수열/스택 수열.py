import sys

n = int(sys.stdin.readline().rstrip())
s = []
result = []
now = 1
check = False
for _ in range(n):
    cmd = int(sys.stdin.readline().rstrip())
    
    while now <= cmd:
        s.append(now)
        result.append("+")
        now +=1
    if cmd == s.pop():
        result.append("-")
    else:
        check = True
if check:
    print("NO")
else:
    for i in result:
        print(i)