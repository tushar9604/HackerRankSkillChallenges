import re

output= []
for _ in range(int(input())):
    s = input()
    
    if (re.match(r'(\d|\d\d|1\d\d|2[01234]\d|25[012345])\.(\d|\d\d|1\d\d|2[01234]\d|25[012345])\.(\d|\d\d|1\d\d|2[01234]\d|25[012345])\.(\d|\d\d|1\d\d|2[01234]\d|25[012345])',s)):
        output.append('IPv4')

    elif (re.match(r'([\dabcdef]{4}|[\dabcdef]{1}):([\dabcdef]{4}|[\dabcdef]{1}):([\dabcdef]{4}|[\dabcdef]{1}):([\dabcdef]{4}|[\dabcdef]{1}):([\dabcdef]{4}|[\dabcdef]{1}):([\dabcdef]{4}|[\dabcdef]{1}):([\dabcdef]{4}|[\dabcdef]{1}):([\dabcdef]{4}|[\dabcdef]{1})',s)):
        output.append('IPv6')

    else:
        output.append('Neither')

print('\n'.join(output))
#'(\d|\d\d|1\d\d|2[01234]\d|25[012345])\.(\d|\d\d|1\d\d|2[01234]\d|25[012345])\.(\d|\d\d|1\d\d|2[01234]\d|25[012345])\.(\d|\d\d|1\d\d|2[01234]\d|25[012345])'