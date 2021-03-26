"""def merge_the_tools(string, k):
    # your code goes here
    l = len(string)
    list_t = [sorted(set(string[i-k:i]),key=string[i-k:i].index) for i in range(k,l+1,k)]
    print(*map(''.join,list_t),sep='\n')
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
"""
S, N = input(), int(input()) 
print(*zip(*[iter(S)] * N))
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))   