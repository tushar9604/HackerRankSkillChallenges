"""import re
re.match(r'^[4,5,6]{1}',input())
re.match(r'[\d]{16}',input())
re.match(r'[^\d-]',input())
re.match(r'[^\d-]{16}',input())
[ for _ in range(int(input()))]
"""
import re
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")
    
import re


for _ in range(int(input())):
    s = input()

    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")    
        
def validate_credit_cards(credit_cards):
    valid_structure = r"[456]\d{3}(-?\d{4}){3}$"
    no_four_repeats = r"((\d)-?(?!(-?\2){3})){16}"
    filters = valid_structure, no_four_repeats

    for cc in credit_cards:
        if all(re.match(f, cc) for f in filters):
            print("Valid")
        else:
            print("Invalid")        
            
import re

for _ in range(int(input())):
    n = input().strip()
    try:
        assert re.match(r'(\d{4}-){3}\d{4}$', n) or re.match(r'\d{16}$', n)
        n = re.sub(r'-', '', n)
        assert re.match(r'[456]', n)
        assert not re.search(r'(\d)\1{3,}', n)
    except:
        print('Invalid')
    else:
        print('Valid')

import re

is_grouping = re.compile(r'^(?:.{4}\-){3}.{4}$').match
is_consecutive = re.compile(r'(.)\1{3}').search
is_valid = re.compile(r'^[456]\d{15}$').match

for _ in range(int(input())):
    card_no = input()
    if is_grouping(card_no):
        card_no = card_no.replace('-', '')
    if is_valid(card_no) and not is_consecutive(card_no):
        print('Valid')
    else:
        print('Invalid')        
        
card_no equals input
if card_no is a grouping,
    replace the dashes with nothing
if card_no is valid and it is not consecutive,
    print that it is valid
else,
    print that it is invalid        