import sys

a=int(sys.stdin.readline())
point=0
count=0
while a>point:
    if point==0:
        point=1
    else:
        point=point+count*6 
    count=count+1
    

print(count)
#1~1 =   1 0  1+6*0
#2~7 =   2 6  1+6*1
#8~19 =  3 12 7+6*2
#20~37 = 4 18 19+6*3
#38~61 = 5 24 37+6*4
