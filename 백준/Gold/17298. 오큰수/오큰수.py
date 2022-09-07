import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int,sys.stdin.readline().rstrip().split()))

result = [-1]*n
s = []
for i in range(n):
    if s:
        while s[-1][0]< arr[i]:
            pos = s.pop()[1]
            result[pos] = arr[i]
            if not s:
                break
    s.append([arr[i],i])
print(*result)