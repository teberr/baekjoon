import sys

a=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
max=data[0]
sum=0
for i in data:
    if i> max:
          max=i

for i in range(0,len(data)):
    data[i]=data[i]/max*100
    sum=sum+data[i]
print(sum/len(data))
