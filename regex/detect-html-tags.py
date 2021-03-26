import re

string = ''.join([input() for _ in range(int(input()))])
print(';'.join(sorted(set(re.findall(r'<([\w]+).*?>',string)))).lower())