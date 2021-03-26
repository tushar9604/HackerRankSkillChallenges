# Enter your code here. Read input from STDIN. Print output to STDOUT
n,set_n,b,set_b = input(),set(input().split()),input(),set(input().split())
print(len(set_n.union(set_b)))