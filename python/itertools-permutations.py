# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
string,size = input().split()
[print(''.join(tup)) for tup in list(permutations(sorted(string),int(size)))]