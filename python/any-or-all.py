# Enter your code here. Read input from STDIN. Print output to STDOUT
n,nlist = input(),map(int,input().split())
print(any(map(lambda x:str(x)[::-1]==str(x),nlist)) & all(map(lambda x:x>0,nlist)))