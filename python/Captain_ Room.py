# Enter your code here. Read input from STDIN. Print output to STDOUT
k,*room_list = int(input()),*map(int,input().split())
print((sum(set(room_list))*k - sum(room_list))//(k-1))
