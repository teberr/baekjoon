import sys

n=int(sys.stdin.readline())

sang=list(map(int,sys.stdin.readline().split()))

j=int(sys.stdin.readline())
sample=list(map(int,sys.stdin.readline().split()))

sang=set(sang)

for i in range(0,j):
    if sample[i] in sang:
        sample[i]=1
    else:
        sample[i]=0

for i in sample:
    print(i,end=" ")
