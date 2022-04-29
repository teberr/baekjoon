import sys

T=int(sys.stdin.readline())
prime=[0 for i in range(10001)]
 
for i in range(T):
    num=int(sys.stdin.readline())
    

    for i in range(2,num+1):
        if prime[i]==0:
            for j in range(2*i,num+1,i):
                prime[j]=1


  
    for i in range(num//2,1,-1):
        if prime[i]==0 and prime[num-i]==0:
                print(i,num-i)
                break
