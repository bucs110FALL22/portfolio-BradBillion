def rstar_pyramid(num):
    for i in range(num):
        print("*" * (num - i))


def star_pyramid():
    numRows = int(input("Number of rows: "))
    for i in range(numRows):
        print("*" * (i + 1))
    rstar_pyramid(numRows)


star_pyramid()
