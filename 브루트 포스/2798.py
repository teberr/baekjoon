import sys
import math

num,target=map(int,sys.stdin.readline().split())
card=list(map(int,sys.stdin.readline().split()))
result=0
flag=0
for i in range(0,len(card)):
    for j in range(i+1,len(card)):
        for k in range(j+1,len(card)):
            temp=card[i]+card[j]+card[k]
            if target-result>target-temp and target-temp>=0:
                result=card[i]+card[j]+card[k]
            if result==target:
                flag=1
                print(result)
                break
        if flag==1:
            break
    if flag==1:
        break
if flag==0:
    print(result)
