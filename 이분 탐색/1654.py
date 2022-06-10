import sys

K,N=map(int,sys.stdin.readline().split())

length=[]
for i in range(K):
    temp=int(sys.stdin.readline())
    length.append(temp)


length=sorted(length)
start=1
end=length[-1]
while start<=end:

    mid=(start+end)//2

    l=0
    for x in length:
        l=l+(x//mid)
    if l<N: # 구하고자 하는것 보다 적게 나오므로 더 작게 잘라야함
        end=mid-1
    else : # 구하고자 하는것보다 크거나 같게 나오므로 더 크게 잘라야함(최대구해야하므로)
        start=mid+1

temp=max(start,end)
l=0
for x in length:
    l=l+(x//temp)
if l>=N:
    print(max(start,end))
else:
    print(min(start,end))
