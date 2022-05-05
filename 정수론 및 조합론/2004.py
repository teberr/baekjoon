import sys

a,b=map(int,sys.stdin.readline().split())
count2=0
count5=0
def count(n,k):
    count=0
    while n!=0: # 5->1 10->2 15->3 20->4 25-> 5 30->6
        n=n//k
        count=count+n
    
    return count

count2= count(a,2)-count(b,2)-count(a-b,2)
count5= count(a,5)-count(b,5)-count(a-b,5)


print(min(count2,count5))
