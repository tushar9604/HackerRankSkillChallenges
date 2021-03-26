#!/bin/python3

import math
import os
import random
import re
import sys

import re
x,y = list(map(int,input().split()))
rows =[input() for i in range(x)]
text = "".join([print(row[i]) for i in range(y) for row in rows])
print(1,text)
text = re.sub('([A-Za-z1-9])[^A-Za-z1-9]+([A-Za-z1-9])', r'\1 \2', text)
print(2,text)
text = re.sub('  ', ' ', text)
print(3,text)
