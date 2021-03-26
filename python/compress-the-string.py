from itertools import groupby
print(*[(len(list(y)),int(x)) for x,y in groupby(input())])