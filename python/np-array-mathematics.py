import numpy
N,M = map(int,input().split())

A = numpy.array([input().strip().split() for _ in range(N)],int)
B = numpy.array([input().strip().split() for _ in range(N)],int)
#print(A)
#print(B)

Tasks = ['add','subtract','multiply','divide','floor_divide','mod','power']

#for task in Tasks:
 #   print(eval('numpy.%s(%s,%s)' % (task,A,B))) Doesn't work with numpy numpy.add([[1 2 3 4]],[[5 6 7 8]])
   

print(numpy.add(A,B),numpy.subtract(A,B),numpy.multiply(A,B),numpy.floor_divide(A,B),numpy.mod(A,B),numpy.power(A,B),sep='\n')

