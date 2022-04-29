import sys
start,end=map(int,sys.stdin.readline().split())
prime=[0 for i in range(end+1)] 

prime[1]=1


for i in range(2,end+1):
    if prime[i]==0: # 소수임
        for j in range(2,end//i+1):
            prime[i*j]=1


for j in range(start,end+1):
    if prime[j]==0:
        print(j)
        
