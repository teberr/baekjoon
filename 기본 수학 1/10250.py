import sys

T=int(sys.stdin.readline())

for i in range(T):
    h,w,n=map(int,sys.stdin.readline().split())  # h(층)w(방)n(몇번째손님)
    if n%h==0:
        floor=str(h)
        if n//h<10:
            room="0"+str(n//h)
        else:
            room=str(n//h)
            
    else:
        floor=str(n%h) # 층수임.    
        if n//h+1<10:
            room="0"+str(n//h+1)
        else:
            room=str(n//h+1) # 호실임

    print(floor+room)
