import re


print(*[re.sub(r'(?<= )(&&|\|\|)(?= )',lambda x: 'and' if ('&&' == x.group(0)) else 'or',input()) for _ in range(int(input()))],sep='\n')