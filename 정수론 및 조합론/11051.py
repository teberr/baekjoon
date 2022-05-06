import sys

n,k=map(int,sys.stdin.readline().split())


def solve(n,k):
    result=[[0 for i in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or i==j:
                result[i][j]=1
            else:
                result[i][j]=result[i-1][j-1]+result[i-1][j]

    return result[n][k]

print(solve(n,k)%10007)
