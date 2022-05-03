import sys

a,b=map(int,sys.stdin.readline().split())

def gcd(a,b):
    if a>=b:
        if a%b==0:
            return b
        else:
            return gcd(b,a%b)
    else:
        return gcd(b,a)


g=gcd(a,b)
print(g)
print(a//g * b)
