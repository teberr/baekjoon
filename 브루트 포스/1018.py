import sys


a,b=map(int,sys.stdin.readline().split())
chess=[]
for i in range(a):
    temp=sys.stdin.readline().rstrip()
    chess.append(temp)


count=65

for x in range(0,a-7):  
    for y in range(0,b-7):
        count1=0 #B로 시작할 때
        count2=0 #W로 시작할 때
        for i in range(0,8):
            for j in range(0,8):
                if (i+j)%2==0:
                    if chess[i+x][j+y]=='B':
                        count2=count2+1
                    else:
                        count1=count1+1
                else:
                    if chess[i+x][j+y]=='W':
                        count2=count2+1
                    else:
                        count1=count1+1
        count=min(count1,count2,count)
print(count)
