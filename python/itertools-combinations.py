# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,n = input().split()
[print('\n'.join([''.join(j) for j in i]))for i in [list(combinations(sorted(s),i)) for i in range(1,int(n)+1)]]