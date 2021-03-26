# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A = set(input().split())

isSuperSetList = []
for _ in range(int(input())):
    set_x = set(input().split())
    isSuperSetList.append(set_A.issuperset(set_x) and not set_A.issubset(set_x))
    
print(all(isSuperSetList))