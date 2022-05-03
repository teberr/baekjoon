import sys

def bi_coef(n,k):
    if n==k or k==0:
        return 1
    else:
        return bi_coef(n-1,k)+bi_coef(n-1,k-1)

n,k=map(int,sys.stdin.readline().split())
print(bi_coef(n,k))
