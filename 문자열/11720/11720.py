import sys

sum=0
n=int(sys.stdin.readline())
string=sys.stdin.readline().rstrip()
for i in string:
    sum=sum+int(i)
print(sum)
