import sys

num=int(sys.stdin.readline())
nums=[]
while True:
    if num==0:
        break
    nums.append(num%10)
    num=num//10

nums.sort(reverse=True)
for i in range(0,len(nums)):
    print(nums[i],end="")
