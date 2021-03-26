L,B = map(int,input().split())

pattern = [('.|.'*(2*i+1)).center(B,'-') for i in range(L//2)]
print('\n'.join(pattern + ['WELCOME'.center(B,'-')] + pattern[::-1]))

for i in range(1,L,2):
    print(('.|.'*i).center(B,'-'))
  
print('WELCOME'.center(B,'-'))

for i in range(L-2,0,-2):
    print(('.|.'*i).center(B,'-'))
