import sys
a,b =map(int,input().split())
data=list(map(int,sys.stdin.readline().split()))
for i in data:
    if i<b:
        print(i,end=" ")
