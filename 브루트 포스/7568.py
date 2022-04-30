import sys


num=int(sys.stdin.readline())
person=[]
rank=[1 for i in range(num)]

for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    person.append([a,b])



for j in range(0,len(person)):
    count=rank[j]
    for k in range(0,len(person)):
        if person[j][0]<person[k][0] and person[j][1]<person[k][1]:
            count=count+1
    rank[j]=count

for i in rank:
    print(i,end=" ")
