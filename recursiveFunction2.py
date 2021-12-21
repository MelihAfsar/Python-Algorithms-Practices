def triangle(n):
    if n<1:
        pass
    else:
        print("*" * n)
        triangle(n-1)
triangle(5)