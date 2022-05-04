import sys

num=int(sys.stdin.readline())
for i in range(num):
    a,b = map(int,sys.stdin.readline().split())
    result=1
    for j in range(0,a):
        result=result*(b-j)//(j+1)

    print(result)
