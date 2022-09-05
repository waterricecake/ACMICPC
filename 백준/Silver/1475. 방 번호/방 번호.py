import sys
import math
arr = [0] * 9
num = str(sys.stdin.readline().rstrip())
for i in num:
    if i =="9":
        arr[6] +=1
    else:
        arr[int(i)] +=1
arr[6] = math.ceil(arr[6]/2)
print(max(arr))