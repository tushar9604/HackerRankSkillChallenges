import numpy
N,M,P = map(int,input().split())

NP = numpy.array([input().split() for _ in range(N)],int)
MP = numpy.array([input().split() for _ in range(M)],int)

print(numpy.concatenate((NP,MP),axis=0))