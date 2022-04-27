import sys
max=0
counter=0
for i in range(1,10):
    temp=int(sys.stdin.readline())
    if temp > max:
        max=temp
        counter=i
        
print(max)
print(counter)
