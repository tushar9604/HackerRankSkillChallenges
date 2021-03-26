# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
#[print('YES') if (re.match(r'^[789][0-9]{9}$',input())) else print('NO') for _ in range(int(input()))]
[print('YES') if (re.match(r'^[789]\d{9}$',input())) else print('NO') for _ in range(int(input()))]