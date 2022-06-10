import sys
import itertools

N=int(sys.stdin.readline())
member=[x for x in range(N)]
total=list(map(list,itertools.combinations(member,N//2)))
start=[]
link=[]
power=[]
for i in range(0,len(total)//2):
    start.append(total[i])
    link.append(total[len(total)-i-1])

for i in range(N):
    power.append(list(map(int,sys.stdin.readline().split())))
diff=-1
for x in range(0,len(start)):
    start_power=0
    link_power=0
    start_temp=list(map(list,itertools.permutations(start[x],2)))
    link_temp=list(map(list,itertools.permutations(link[x],2)))
    for temp in start_temp:
        start_power+=power[temp[0]][temp[1]]
    for temp in link_temp:
        link_power+=power[temp[0]][temp[1]]
    if diff==-1:
        diff=abs(start_power-link_power)
    else:
        diff=min(diff,abs(start_power-link_power))
print(diff)
