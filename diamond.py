def main(size):
    for i in range(size):
        for j in range(size - i - 1):
            print(' ', end='')
        for j in range(2 * i + 1):
            print('*', end='')
        print()

    for i in range(size - 1):
        for j in range(i + 1):
            print(' ', end='')
        for j in range(2*(size - i - 1) - 1):
            print('*', end='')
        print()    
main(7)    