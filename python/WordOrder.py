from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())

# Enter your code here. Read input from STDIN. Print output to STDOUT
word_dict = {}
for _ in range(int(input())):
    x = input()
    if (x in word_dict.keys()):
        word_dict[x] += 1
    else:
        word_dict[x] = 1

print(len(word_dict.keys()))
print(*word_dict.values())
