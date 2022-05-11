import sys

num1,num2=map(int,sys.stdin.readline().split())
pokemon1={}
pokemon2={}
for i in range(0,num1):
    temp=sys.stdin.readline().rstrip()
    pokemon1[temp]=i+1
    pokemon2[i+1]=temp
    
for j in range(num2):
    
    k=sys.stdin.readline().rstrip()
    try:
        k=int(k)
    except:
        pass
    if type(k)==str:
        print(pokemon1[k])
    else:
        print(pokemon2[k])
