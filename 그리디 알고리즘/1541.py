import sys

n=list(sys.stdin.readline().rstrip().split("-"))


for i in range(0,len(n)):
    rep=0
    if '+' in n[i]:
        temp=list(map(int,n[i].split("+")))
        for j in temp:
             rep=rep+j
        n[i]=rep
    else:
        n[i]=int(n[i])

result=n[0]
for i in range(1,len(n)):
    result=result-n[i]

print(result)
