# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m = map(int,input().split())
d = defaultdict(list)
d['n'] = [input() for _ in range(n)]
d['m'] = [input() for _ in range(m)]

[print(*k) for k in [[i+1 for i,wordn in enumerate(d['n']) if wordn == wordm] if wordm in d['n'] else [-1] for wordm in d['m']]]