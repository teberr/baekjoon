import sys

num=int(sys.stdin.readline())

count=0
for i in range(2,num+1):
    while True:
        if i%5==0:
            count=count+1
            i=i//5
        else:
            break
 

print(count)
