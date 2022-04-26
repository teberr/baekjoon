a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
money=0
if a==b==c:#셋다 같은 경우
    money=10000+a*1000
elif a!=b and b!=c and a!=c:# 셋다 다른경우
    if a>b and a>c:
        money=a*100
    elif b>a and b>c :
        money=b*100
    else:
        money=c*100
else:
    if a==b or a==c:
        money=1000+a*100
    else:
        money=1000+b*100
print(money)
