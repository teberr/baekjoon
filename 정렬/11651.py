import sys

num=int(sys.stdin.readline())
coord=[]

for i in range(num):
    x,y=map(int,sys.stdin.readline().split())
    coord.append([x,y])


coord.sort(key=lambda x:(x[1],x[0]))
for x,y in coord:
    print(x,y)
