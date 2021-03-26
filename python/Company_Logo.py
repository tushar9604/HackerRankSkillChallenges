from collections import Counter

string = Counter(sorted(input())).most_common(3)

for string,count in string:
    print(string,count) 