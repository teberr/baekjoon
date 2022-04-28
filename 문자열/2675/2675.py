import sys
a=int(sys.stdin.readline())
for i in range(a):
    b,c=sys.stdin.readline().split()
    b=int(b)
    c=c.rstrip()
    for j in range(0,len(c)):
        print(c[j]*b,end="")
    print()
