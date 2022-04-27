import sys
a=int(sys.stdin.readline())
data= list(map(int,sys.stdin.readline().split()))
min=data[0]
max=data[0]
for i in range(0,a):
    if min>data[i]:
        min=data[i]
    if max<data[i]:
        max=data[i]

print(min,max)
