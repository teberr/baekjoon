import sys

num=int(sys.stdin.readline())
person=[]

for i in range(num):
    x,y=sys.stdin.readline().rstrip().split()
    x=int(x)
    person.append([x,y])

person.sort(key=lambda x:x[0])

for x,y in person:
    print(x,y)
