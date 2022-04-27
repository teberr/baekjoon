import sys

data=[]
count=[]

for i in range(10):
    a=int(sys.stdin.readline())
    data.append(a%42)

for i in data:
    if i not in count:
        count.append(i)

print(len(count))
