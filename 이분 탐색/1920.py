import sys

i=int(sys.stdin.readline().strip())
A=list(map(int,sys.stdin.readline().split()))

b=int(sys.stdin.readline().strip())
B=list(map(int,sys.stdin.readline().split()))

A=sorted(A)

answer=[]

for i in range(0,len(B)):
    start=0
    end=len(A)-1
    flag=0
    while start<=end:
        mid=(start+end)//2
        if B[i]>A[mid]:
            start=mid+1
        elif B[i]<A[mid]:
            end=mid-1
        else:
            answer.append(1)
            flag=1
            break
    if flag==0:
        answer.append(0)
    
for i in answer:
    print(i)
