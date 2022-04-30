import sys


num=int(sys.stdin.readline())
gen=[0 for i in range(num+1)]

for i in range(1,num+1):
    k=i
    temp=k
    while k!=0:
        temp=temp+k%10
        k=k//10
    if temp<=num and gen[temp]==0:
        gen[temp]=i


print(gen[num])
