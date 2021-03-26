# Enter your code here. Read input from STDIN. Print output to STDOUT
nA,A = int(input()),set(input().split())

for _ in range(int(input())):
    opr,n = input().split()
    setn = set(input().split())
  # eval('A.{0}(setn)'.format(opr))
    getattr(A,opr)(setn)

print(sum(map(int,A)))

