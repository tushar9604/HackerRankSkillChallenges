len_arr,len_set = map(int,input().split())
arr = list(map(int,input().split()))
set_A = set(map(int,input().split()))
set_B = set(map(int,input().split()))

print(sum([1 if i in set_A else (-1 if i in set_B else 0) for i in arr]))
print(sum([(i in set_A) - (i in set_B) for i in arr]))