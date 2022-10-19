def mult(a=0, b=0):
    result = 0
    for i in range(a):
        result += b
    return result


def exp(n=0, e=0):
    result = 1
    for i in range(e):
        result *= n
    return result


def square(c=0):
    return exp(c, 2)


def main():
    print(mult(2, 3))
    print(exp(2, 3))
    print(square(3))


main()
