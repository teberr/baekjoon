import sys

num=int(sys.stdin.readline())
global count
count=0
track=[]

def hanoi(start,end,n):
    global count
    point=6-start-end
    if n==1:
        track.append([start,end])
        count=count+1
    else:
        hanoi(start,point,n-1)
        track.append([start,end])
        count=count+1
        hanoi(point,end,n-1)
        

hanoi(1,3,num)
print(count)
for i in track:
    print(i[0],i[1])
