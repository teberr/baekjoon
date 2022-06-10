import sys

K,N=map(int,sys.stdin.readline().split())

length=list(map(int,sys.stdin.readline().split()))

start=1
end=max(length)
while start<=end:

    mid=(start+end)//2
    l=0
    for x in length:
        if x>mid:
            l=l+(x-mid)
    if l>=N: # 구하고자 하는것 보다 너무 많이 잘랐으므로 덜잘라야함 
        start=mid+1
    else : # 구하고자 하는것보다 너무 적게 잘랐으므로 더 잘라야함.
        end=mid-1

print(end)
