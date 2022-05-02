import sys

num=int(sys.stdin.readline())
word=[]

for i in range(num):
    temp=sys.stdin.readline().rstrip()
    if temp not in word:
        word.append(temp)

word.sort(key=lambda x:(len(x),x))

for i in word:
    print(i)
