import sys

def solve(a):
    start=a//5
    end=a//3

    for i in range(start,-1,-1):
        for j in range(0,end+1):
            if i*5+j*3==a:
                return i+j
            elif i*5+j*3>a:
                break
    return -1


a=int(sys.stdin.readline())
print(solve(a))
