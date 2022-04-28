import sys

a=int(sys.stdin.readline())
factorial=[0]
count=0
point=0

while factorial[point]<a:
    factorial.append(factorial[point]+(point+1))
    point=point+1



start=factorial[point-1] 
i=a-start
if point%2==0:
    print("%d/%d"%(i,point+1-i))
else:
    print("%d/%d"%(point+1-i,i))
