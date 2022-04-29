import sys
prime=[2]

num=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
count=0
for i in nums:
    if prime[len(prime)-1]<i:
        for j in range(prime[len(prime)-1],i+1):
            flag=1
            for k in prime:
                if j%k==0: #소수가아님
                    flag=0 
                    break
            if flag==1:
                prime.append(j)
for i in nums:
    if i in prime:
        count=count+1
print(count)
