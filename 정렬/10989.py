import sys

num=int(sys.stdin.readline())
nums=[0 for i in range(10001)]

for i in range(num):
    temp=(int(sys.stdin.readline()))
    nums[temp-1]=nums[temp-1]+1

for j in range(0,len(nums)):
    if num!=0:
        if nums[j]!=0:
            for k in range(nums[j]):
                print(j+1)
                num=num-1
    if num==0:
        break
