import sys
N,M=map(int,sys.stdin.readline().split())
number=[]

    
def dfs(index):
    if len(number)==M:
        for x in number:
            print(x,end=" ")
        print()
    else:
        for i in range(index,N+1):
            number.append(i)
            dfs(i+1)
            number.pop()
dfs(1)
