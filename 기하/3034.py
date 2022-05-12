import sys

n,w,h=map(int,sys.stdin.readline().split())


for i in range(n):
    sample=int(sys.stdin.readline())
    if w**2+h**2>=sample**2:
        print("DA")
    else:
        print("NE")
