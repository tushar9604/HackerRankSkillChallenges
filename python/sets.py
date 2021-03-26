# Enter your code here. Read input from STDIN. Print output to STDOUT
m,set_m,n,set_n = input(),set(map(int,input().split())),input(),set(map(int,input().split()))
[print(i) for i in sorted(set_m.union(set_n) - set_m.intersection(set_n))]