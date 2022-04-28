import sys

num=int(sys.stdin.readline())
count=0

for i in range(num):
    alpha=[0 for i in range(26)]
    text=sys.stdin.readline().rstrip()
    flag=1
    for i in range(0,len(text)):
        if alpha[ord(text[i])-97]==0:
            alpha[ord(text[i])-97]=1
        elif alpha[ord(text[i])-97]==1:
            if text[i]!=text[i-1]:
                flag=0
                break
    if flag==1:
        count=count+1
    
print(count)
    
