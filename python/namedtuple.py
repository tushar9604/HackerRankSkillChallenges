# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
nStudents,columns = int(input()),input()
StuDetails = namedtuple('StuDetails',columns)
print('{0:.2f}'.format(sum([int(StuDetails(*input().strip().split()).MARKS) for _ in range(nStudents)])/nStudents))