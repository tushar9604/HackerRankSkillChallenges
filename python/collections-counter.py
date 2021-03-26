# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

nShoes = int(input())
ShoeNoList = Counter(map(int,input().split()))
nCustomer = int(input())

money = 0
for _ in range(nCustomer):
    shoeNo,price = map(int,input().split())
    
    if ShoeNoList[shoeNo] > 0:
        ShoeNoList[shoeNo] -= 1
        money += price
  
print(money)