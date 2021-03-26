n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    try :
        method, key = input().split()
    except:
        method = 'pop'
    if (method=='pop'):
        try: s.pop()       
        except:
            pass
    elif (method=='remove'):
        try:s.remove(key)         
        except:
            pass      
    else:
        s.discard(key)      

print(s)

n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))


n = int(input())
s = set(map(int, input().split())) 
t = int(input())

for i in range(t):

    c, *args = map(str,input().split())

    getattr(s,c) (*(int(x) for x in args))


print (sum(s))