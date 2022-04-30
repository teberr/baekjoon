import sys
import math

num=int(sys.stdin.readline())
for i in range(num):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    
    d1=math.sqrt((x2-x1)**2+(y2-y1)**2)
    if max(d1,r1,r2) == d1:
        if d1>r1+r2:
            print(0)
        elif d1==r1+r2:
            print(1)
        elif d1<r1+r2:
            print(2)
    else:
        if d1==abs(r2-r1):
            if r1==r2:
                print(-1)
            else:
                print(1)
        elif d1<abs(r2-r1):
            print(0)
        elif d1>abs(r2-r1):
            print(2)
        
