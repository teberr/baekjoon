import sys

def gcd(a,b):
    if a>=b:
        if a%b==0:
            return b
        else:
            return gcd(b,a%b)
    else:
        return gcd(b,a)

num=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

for i in range(1,len(nums)):
    a=nums[0]
    b=nums[i]
    g=gcd(a,b)
                

    print("%d/%d"%(nums[0]//g,nums[i]//g))
 

