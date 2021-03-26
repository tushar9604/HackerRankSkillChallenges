# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n,*cubes = int(input()),*map(int,input().split())
    min_index = cubes.index(min(cubes))
    if (cubes[0:min_index+1] == sorted(cubes[0:min_index+1],reverse=True) and cubes[min_index:] == sorted(cubes[min_index:])):
        print('Yes')
    else:
        print('No')