import sys
alphabet=[0 for i in range(26)]
a=sys.stdin.readline().rstrip()
for i in range(0,len(a)):
    if ord(a[i])<97:
        alphabet[ord(a[i])-65]=alphabet[ord(a[i])-65]+1
    else:
        alphabet[ord(a[i])-97]=alphabet[ord(a[i])-97]+1

max=0
count=1
for i in range(0,len(alphabet)):
    if alphabet[max]<alphabet[i]:
        max=i
        count=1
    elif alphabet[max]==alphabet[i] and max!=i:
        count=count+1

if count>1:
    print("?")
if count==1:
    print(chr(max+65))
