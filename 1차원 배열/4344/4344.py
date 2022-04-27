import sys

a=int(sys.stdin.readline())
for i in range(a):
    data=list(map(int,sys.stdin.readline().split()))
    num=data[0]
    data=data[1:]
    sum=0
    count=0
    for j in data:
        sum=sum+j
    for j in data:
        if j>(sum/num):
            count=count+1
    print("%2.3f%%"%(count/num*100))
