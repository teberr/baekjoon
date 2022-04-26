h,m=input().split()
count=int(input()) # 경과시간
h=int(h)
m=int(m)

time=h*60+m
if time+count>=1440:
    time=time+count-1440
else:
    time=time+count
h=time//60
m=time%60
print(h,m)
