import operator

def person_lister(f):
    def inner(people):
        # complete the function        
        return [f(i[1]) for i in sorted(enumerate(people),key=lambda x:(x[1][2],x[0]))]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')