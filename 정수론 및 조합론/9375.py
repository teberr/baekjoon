import sys

num=int(sys.stdin.readline())

for i in range(num):
    n=int(sys.stdin.readline())
    result={}
    for j in range(n):
        clothes,kind=sys.stdin.readline().rstrip().split()
        if kind in result:
            result[kind]=result[kind]+1
        else:
            result[kind]=1

    days=1
    for k in result.keys():
        days=days*(result[k]+1)
    days=days-1
    print(days)
