import sys

while True:
    num=int(sys.stdin.readline())
    if num==0:
        break
    
    end=num*2
    prime=[0 for i in range(end+1)] 

    prime[1]=1


    for i in range(2,end+1):
        if prime[i]==0: # 소수임
            for j in range(i*2,end+1,i):

                prime[j]=1

    count=0
    for j in range(num+1,end+1):
        if prime[j]==0:
            count=count+1
    print(count)      
