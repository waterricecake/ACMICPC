import math
a=[0]*10
for i in input():a[int(i)]+=1
a[6]=math.ceil((a[6]+a[-1])/2)
print(max(a[:-1]))