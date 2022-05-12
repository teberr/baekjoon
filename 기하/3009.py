import sys
x={}
y={}
for i in range(3):
    a,b=map(int,sys.stdin.readline().split())
    if a not in x:
        x[a]=1
    else:
        x[a]=x[a]+1
    if b not in y:
        y[b]=1
    else:
        y[b]=y[b]+1

result=[]
for k in x.keys():
    if x[k]==1:
        result.append(k)
        break

for k in y.keys():
    if y[k]==1:
        result.append(k)
        break

print(result[0],result[1])
