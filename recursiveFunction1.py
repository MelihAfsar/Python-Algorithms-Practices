def papyon(n):
    if n<1:
        pass
    else:
        print("*" * n)
        papyon(n-1)
        if n!=1:
            print("*" * n)
papyon(5)