# Create function Types_of_integer to display result

def Types_of_integer(*num):
    num = sorted(set(num))
    for i in num:
        isPrime = 0
        for c in range(i):
            if i % (c+1) == 0:
                isPrime += 1
        if isPrime == 2 :
            print('{:>4} : Prime Number'.format(i))
        else:
            print('{:>4} : Composite Number'.format(i))


if __name__ == '__main__':
    Types_of_integer(10, 9, 22, 32, 45, 9, 2, 103, 71, 45)
    print()
    Types_of_integer(49, 37, 14, 37)
