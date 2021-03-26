if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        inp = input().split()
        cmd = inp[0]
        args = inp[1:]
        
        if (cmd != 'print'):
            eval('arr.{}({})'.format(cmd,','.join(args)))
        else:
            print(arr)
        