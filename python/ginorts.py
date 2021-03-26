import re
from functools import reduce

s=input()
a = sorted(re.findall(r'[a-z]',s))
A = sorted(re.findall(r'[A-Z]',s))
odd = sorted(re.findall(r'[13579]',s),key=int)
even = sorted(re.findall(r'[02468]',s),key=int)
l = ''.join(a + A   + odd + even)
print(l)