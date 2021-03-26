'''for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    l = [*range(1,i+1)] + [*range(i-1,0,-1)]
    print(*l,sep='') 
    '''
for i in range(1,int(input())+1):    
    print((sum([10 ** j for j in range(0, i)])) ** 2)