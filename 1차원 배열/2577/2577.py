import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
count=[0 for i in range(10)]
num=a*b*c
while num!=0:
    count[num%10]=count[num%10]+1
    num=num//10

for i in range(len(count)):
    print(count[i])
