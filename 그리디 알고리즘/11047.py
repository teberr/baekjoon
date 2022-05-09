import sys

n,money = map(int,sys.stdin.readline().split())

number=[]
result=0
for i in range(n):
    number.append(int(sys.stdin.readline()))

for i in range(len(number)-1,-1,-1):
    if money==0:
        break
    if money>=number[i]:
        result=result+money//number[i]
        money=money%number[i]

print(result)
