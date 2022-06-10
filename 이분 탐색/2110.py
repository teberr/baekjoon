import sys

N,C=map(int,sys.stdin.readline().split())

point=[]
for i in range(N):
    point.append(int(sys.stdin.readline()))
point=sorted(point)
start=1
end=point[-1]-point[0]
while start<=end:
    mid=(start+end)//2
    count=1 
    current_x=point[0] #첫 위치에 공유기 설치
    for i in range(0,len(point)): # 첫위치 + 간격 만큼 지났을 때 공유기 설치
        if point[i]>=current_x+mid:
            count+=1
            current_x=point[i]
            
    if count>=C: # 공유기를 더 많이 설치했다 => 간격이좁았다 간격을 늘리려면 start가 커져야함  
        start=mid+1
    else : # 공유기를 더 적게 설치했다 => 간격이 너무 넓었다, 간격을 좁히려면 end가 작아져야함 
        end=mid-1

print(end)
