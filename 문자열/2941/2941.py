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

''' 
count랑 공백을 아예 한번에 끝내는게 더 효율적

for i in croatia:
        text=text.replace(i,'*')
이렇게 하면 크로아티아 알파벳이 전부 한글자인 *로 치환되므로 전부 치환된 후 길이를 구하면 한번에 구할 수 있음.




'''
