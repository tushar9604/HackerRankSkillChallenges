def wrapper(f):
    def func(l):
        # complete the function
        l = ['+91 '+ num[-10:-5] + ' ' + num[-5:] for num in l]
        f(l)
    return func

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

#sort_phone = wrapper(sort_phone)
if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


