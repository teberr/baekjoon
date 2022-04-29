import sys

x,y,w,h=map(int,sys.stdin.readline().split())
min=0
if h-y<y:
    min=h-y
else:
    min=y

if min>w-x:
    min=w-x
if min>x:
    min=x


print(min)
