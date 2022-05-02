import sys

num=int(sys.stdin.readline())
nums=[]
for i in range(num):
    nums.append(int(sys.stdin.readline()))


def sort(start,end,nums):
    result=[]
    if end-start<=1:
        return nums[start:end]
    else:
        i=0
        j=0
        a=sort(start,(start+end)//2,nums)
        b=sort((start+end)//2,end,nums)
        while True:
            if i==len(a) or j==len(b):
                break
            if a[i]<b[j]:
                result.append(a[i])
                i=i+1
            else:
                result.append(b[j])
                j=j+1

        if i !=len(a):
            for k in range(i,len(a)):
                result.append(a[k])
                
        if j!=len(b):
            for k in range(j,len(b)):
                result.append(b[k])

        return result

    
result=sort(0,len(nums),nums)
for i in result:
    print(i)
