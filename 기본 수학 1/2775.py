import sys

T=int(sys.stdin.readline())

for i in range(T):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    home=[[j for j in range(n+1)] for x in range(k+1)]
    for j in range(1,k+1):
        for l in range(1,n+1):
            home[j][l]=home[j][l-1]+home[j-1][l]
    print(home[k][n])
