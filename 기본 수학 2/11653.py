import sys

num=int(sys.stdin.readline())

while num!=1:
    for i in range(2,num+1):
        if num%i==0:
            print(i)
            break
    num=num//i
