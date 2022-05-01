import sys

nums=[]

num=int(sys.stdin.readline())
for i in range(num):
    nums.append(int(sys.stdin.readline()))    

for i in range(0,num):
    temp=nums[i]
    for j in range(i,num):
        if nums[i]>nums[j]:
            nums[i]=nums[j]
            nums[j]=temp
            temp=nums[i]
    

for i in nums:
    print(i)
