import sys

n,k = map(int,sys.stdin.readline().split())
result = [0 for i in range(n)]
number=[]

def solve(k,depth):

    
    if depth==k:
        for i in range(0,len(number)):
            print(number[i],end=" ")
                
        print()   
        return
    else:
        for i in range(0,len(result)):
            if result[i]==0:
                result[i]=1
                number.append(i+1)
                d=depth
                d=d+1
                solve(k,d)
                number.pop()
                d=d-1
                result[i]=0
            

solve(k,0)
    
