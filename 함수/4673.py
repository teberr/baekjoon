self_number=[0 for i in range(10001)]
def d(n):
    sum=n
    while n!=0:
        sum=sum+n%10
        n=n//10
    if sum<=10000:
        self_number[sum]=1

for i in range(1,10001):
    d(i)
for i in range(1,10001):
    if self_number[i]==0:
        print(i)
