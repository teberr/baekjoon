import sys


num=int(sys.stdin.readline())
title=[]
i=0
while True:
    if len(title)==num:
        break
    i=i+1
    if "666"in str(i):
        title.append(i)
print(title[len(title)-1])
