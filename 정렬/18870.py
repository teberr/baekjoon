import sys
nums=[]
num=int(sys.stdin.readline())
temp=list(map(int,sys.stdin.readline().split()))

for i in range(0,num):   
    nums.append([temp[i],i])


nums.sort(key=lambda x:x[0])
#print("정렬후",nums)

before=nums[0][0]-1
count=0
for i in range(0,num):
    
    #print("nums[%d][0] : %d before : %d count : %d"%(i,nums[i][0],before,count))
    if nums[i][0]!=before:
        before=nums[i][0]
        nums[i][0]=count
        count=count+1
    else:
        nums[i][0]=nums[i-1][0]
        
#print("압축후",nums)

nums.sort(key=lambda x:x[1])
#print("재정렬후",nums)
for i in range(0,num):
    print(nums[i][0],end=" ")
