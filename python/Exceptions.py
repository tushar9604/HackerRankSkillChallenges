# Enter your code here. Read input from STDIN. Print output to STDOUT 
#Code
for _ in range(int(input())):
    
    try:
        a,b = map(int,input().split())
        print(a//b)
    except ValueError as e:
        print("Error Code:",e)
    except ZeroDivisionError as f:
        print("Error Code:",f)