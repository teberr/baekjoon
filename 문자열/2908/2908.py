import sys

a,b=sys.stdin.readline().rstrip().split()
rev_a=""
rev_b=""
for i in range(len(a),0,-1):
    rev_a=rev_a+a[i-1]
for i in range(len(b),0,-1):
    rev_b=rev_b+b[i-1]

rev_a=int(rev_a)
rev_b=int(rev_b)
if rev_a>rev_b:
    print(rev_a)
else:
    print(rev_b)
