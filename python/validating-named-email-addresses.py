# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

for _ in range(int(input())):
    name,emailID = email.utils.parseaddr(input())
    matchObj = re.search(r'^[a-z][\w\.-]*@[a-z]+\.[a-z]{1,3}$',emailID,re.I)
    
    if (matchObj):
        print(email.utils.formataddr((name,emailID)))
    