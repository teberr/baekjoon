import sys

def solve(n):
    result=[1,1,1,2,2,3]
    if n>5:
        i=5
        while i<n:
            result.append(result[i-4]+result[i])
            i+=1
        return result[n-1]
            
    else:
        return result[n-1]

n=int(sys.stdin.readline())

for i in range(n):
    k=int(sys.stdin.readline())
    print(solve(k))
