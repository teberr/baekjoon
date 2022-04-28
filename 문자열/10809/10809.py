import sys
alphabet=[-1 for i in range(26)]
string=sys.stdin.readline().rstrip()
for i in range(0,len(string)):
    if alphabet[ord(string[i])-97]==-1:
        alphabet[ord(string[i])-97]=i
for i in alphabet:
    print(i,end=" ")

