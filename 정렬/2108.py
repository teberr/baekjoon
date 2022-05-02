import sys

num=int(sys.stdin.readline())
nums=[]
counts=[0 for i in range(8001)]

sum=0
for i in range(num):
    temp=int(sys.stdin.readline())
    sum=sum+temp
    nums.append(temp)
    counts[temp+4000]=counts[temp+4000]+1
    
nums.sort()

print(round(sum/num))
print(nums[num//2])
count0=nums[0]
count1=0
for i in range(nums[0]+4000,8001):
    if counts[i]>counts[count0]:
       
        count0=i
        count1=0
    elif counts[i]==counts[count0] and count1==0:
        count1=i
        
        
if count1==0:   
    print(count0-4000)
else:
    print(count1-4000)
print(nums[num-1]-nums[0])
