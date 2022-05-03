import sys

def gcd(a,b):
    if a>=b:
        if a%b==0:
            return b
        else:
            return gcd(b,a%b)
    else:
        return gcd(b,a)
num=int(sys.stdin.readline())
for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    g=gcd(a,b)
    print(a//g * b)
