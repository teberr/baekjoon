import sys

a= sys.stdin.readline().strip()
time=0
for i in range(0,len(a)):
    j=ord(a[i])-65
    if j<15:
        time=time+(j//3)+3
    elif j<19:
        time=time+8
    elif j<22:
        time=time+9
    else:
        time=time+10

print(time)
    
