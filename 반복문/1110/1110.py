import sys
count=0
num= int(sys.stdin.readline())
result=num
while True:
    
    if num<10:
        a=0
        b=num
        num=b*10+b
    else:
        a=num//10
        b=num%10
        if a+b>=10:
            num=b*10+((a+b)%10)
        else:
            num=b*10+a+b

    count=count+1
    if result==num:
        break
print(count)
