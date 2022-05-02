import sys

num=int(sys.stdin.readline())
yaksu=list(map(int,sys.stdin.readline().split()))
yaksu.sort()
if len(yaksu)%2==0:
    print(yaksu[(len(yaksu)-1)//2]*yaksu[len(yaksu)//2])
else:
    print(yaksu[len(yaksu)//2]**2)
