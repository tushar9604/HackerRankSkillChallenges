# Enter your code here. Read input from STDIN. Print output to STDOUT
nStudents,nSubjects = map(int,input().split())
[print(sum(i)/len(i)) for i in zip(*[list(map(float,input().split())) for _ in range(nSubjects)])]