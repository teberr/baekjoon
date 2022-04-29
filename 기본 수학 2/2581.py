import sys
prime=[2]
result=[]
sum=0
start=int(sys.stdin.readline())
end=int(sys.stdin.readline())

for i in range(2,end+1):
    flag=1
    for j in prime:
       if i%j==0:
           flag=0
           break
    if flag==1:
        prime.append(i)

for i in range(start,end+1):
    if i in prime:
        result.append(i)
        sum=sum+i

if len(result)==0:
    print(-1)
else:
    print(sum)
    print(result[0])
           
