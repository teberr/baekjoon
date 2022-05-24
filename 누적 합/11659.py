import sys

n,m=map(int,sys.stdin.readline().split())

number=list(map(int,sys.stdin.readline().split()))
for i in range(1,len(number)):
    number[i]=number[i]+number[i-1]
for x in range(m):
    i,j=map(int,sys.stdin.readline().split())
    if i==1:
        print(number[j-1])
    else:
        print(number[j-1]-number[i-2])
