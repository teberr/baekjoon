import sys

a=int(sys.stdin.readline())
for i in range(a):
    string=sys.stdin.readline().rstrip()
    count=1
    sum=0
    for j in range(0,len(string)):
        if string[j]=="O":
            sum=sum+count
            count=count+1
        else:
            count=1
    print(sum)
