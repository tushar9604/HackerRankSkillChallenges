# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
print('\n'.join(re.findall(r'(?<=[%s])([%s]{2,})[%s]'%(c,v,c),input(),re.I) or ['-1']))
