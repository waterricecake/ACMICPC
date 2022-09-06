import sys

k = int(sys.stdin.readline().rstrip())

result = []

for _ in range(k):
    cmd = int(sys.stdin.readline().rstrip())
    
    if cmd ==0:
        if result:
            result.pop()
    else:
        result.append(cmd)

print(sum(result))