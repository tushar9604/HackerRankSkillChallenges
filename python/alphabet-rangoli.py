def print_rangoli(size):
    # your code goes here
    for i in range((-size+1),size):
        print('-'.join([chr(97  + abs(i) + abs(j)) for j in range((-size + abs(i) + 1),(size - abs(i)))]).center((4*size - 3),'-'))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)