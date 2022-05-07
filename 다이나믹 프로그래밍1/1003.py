import sys

n = int(sys.stdin.readline())
def solve(n):
    fibo=[[1,0],[0,1]]
    while n>=len(fibo):
        fibo.append([fibo[len(fibo)-1][0]+fibo[len(fibo)-2][0],fibo[len(fibo)-1][1]+fibo[len(fibo)-2][1]])
    return fibo[n][0],fibo[n][1]

for i in range(n):
    N= int(sys.stdin.readline())
    result_0,result_1=solve(N)
    print(result_0,result_1)

    
