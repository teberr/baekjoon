import sys
import itertools
import collections
N=int(sys.stdin.readline())
number=list(map(int,sys.stdin.readline().split()))
number=collections.deque(number)
operand=list(map(int,sys.stdin.readline().split()))
op=[]
for i in range(operand[0]):
    op.append("+")
for i in range(operand[1]):
    op.append("-")
for i in range(operand[2]):
    op.append("*")
for i in range(operand[3]):
    op.append("/")

max_result=-1000000000
min_result=1000000000
op=list(map(list,itertools.permutations(op,N-1)))
for operand in op:
    operand=collections.deque(operand)
    n=number.copy()
    while len(n)!=1:
        a=n.popleft()
        b=n.popleft()
        o=operand.popleft()
        if o=="+":
            n.appendleft(a+b)
        elif o=="*":
            n.appendleft(a*b)
        elif o=="-":
            n.appendleft(a-b)
        else:
            if a>0:
                n.appendleft(a//b)
            elif a==0:
                n.appendleft(0)
            else:
                a=abs(a)
                temp=a//b
                n.appendleft(-temp)
    max_result=max(n[0],max_result)
    min_result=min(n[0],min_result)
        
    
print(max_result)
print(min_result)
