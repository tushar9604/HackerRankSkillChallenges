import re
for _ in range(int(input())):
    # hexcodes = re.findall(r'(?<!^)(#[0-9a-f]{6}|#[0-9a-f]{3})',input(),re.I)
    hexcodes = re.findall(r'(?<!^)(#(?:[\da-f]{3}){1,2})',input(),re.I)


    for hexcode in hexcodes:
        print(hexcode)