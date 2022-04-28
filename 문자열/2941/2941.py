import sys
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
text= sys.stdin.readline().strip()
count=0

for i in croatia:

    while text.find(i)!=-1:
        
        count=count+1
        text=text.replace(i,' '*len(i),1)
        

text=text.replace(" ","")
print(len(text)+count)
