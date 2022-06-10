import sys
N,M=map(int,sys.stdin.readline().split())
number=[]

    
def dfs():
    if len(number)==M:
        for x in number:
            print(x,end=" ")
        print()
    else:
        for i in range(1,N+1):
            if len(number)==0:
                number.append(i)
                dfs()
                number.pop()
            else:
                if number[-1]<=i:
                    number.append(i)
                    dfs()
                    number.pop()
dfs()
