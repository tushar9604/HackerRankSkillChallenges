'''from itertools import combinations
from math import factorial
n,l,k = int(input()),input().split(),int(input())
c = n - l.count('a')
total = int(factorial(n)/(factorial(k) * factorial(n - k)))
without_a = int(factorial(c)/(factorial(k) * factorial(c - k)))

print(round((total - without_a)/total,3))
'''
from itertools import combinations
input()
combos = list(combinations(input().split(), int(input())))
count = 0
for i in combos:
    if "a" in i:
        count+=1
print(round(count/len(combos),3))