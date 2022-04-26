h,m=input().split()
h=int(h)
m=int(m)
time=h*60+m
if time>=45:
    time=time-45
else:
    time=time+1440-45
h=time//60
m=time%60
print(h,m)
