# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
ordered_dictionary = OrderedDict()
for _ in range(int(input())):
    *item_name,price = input().split()
    item_name = ' '.join(item_name)
    price = int(price)
    
    if (item_name in ordered_dictionary.keys()):
        ordered_dictionary[item_name] += price
    
    else :
        ordered_dictionary[item_name] = price
    
[print('{0} {1}'.format(i[0],int(i[1]))) for i in ordered_dictionary.items()]

from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)