import collections
import sys

N=int(sys.stdin.readline())
queue=collections.deque()
for i in range(N):
    string=sys.stdin.readline().strip()
    if " " in string:
        cmd,number=string.split()
        queue.append(int(number))
        continue
    else:
        if string=="front":
            if len(queue)==0:
                print(-1)
            else:
                temp=queue.popleft()
                print(temp)
                queue.appendleft(temp)
        elif string=="back":
            if len(queue)==0:
                print(-1)
            else:            
                temp=queue.pop()
                print(temp)
                queue.append(temp)
        elif string=="empty":
            if len(queue)==0:
                print(1)
            else:
                print(0)
        elif string=="size":
            print(len(queue))
        elif string=="pop":
            if len(queue)==0:
                print(-1)
            else:
                temp=queue.popleft()
                print(temp)
