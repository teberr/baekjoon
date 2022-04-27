a=int(input())
for i in range(1,a+1):
    for j in range(a-i,0,-1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
