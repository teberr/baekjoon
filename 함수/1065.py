import sys
def han(n):

    count=0
    for i in range(1,n+1):
        temp=[]
        j=0
        while i!=0:
            temp.append(i%10)
            i=i//10
        if len(temp)<=2:
            count=count+1
        else:
            for i in range(1,len(temp)-1):
                if temp[i+1]-temp[i]!=temp[i]-temp[i-1]:
                    j=1
                    break
            if j==0:
                count=count+1
    print(count)
                

n=int(sys.stdin.readline())
han(n)
