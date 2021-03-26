import re

l = '\n'.join([input() for _ in range(int(input()))])

for _ in range(int(input())):
    print(len(re.findall(r'\w(%s)\w'%input(),l)))
    