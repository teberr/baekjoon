import sys

a,b,c=map(int,sys.stdin.readline().split())

if (c-a)%(b-a)==0:
    date=(c-a)//(a-b)+1
else:
    date=(c-a)//(a-b)+2

        
print(date)
