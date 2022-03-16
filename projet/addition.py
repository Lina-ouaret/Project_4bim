def addition(x,y):
    """

    computing the sum of x and y

    Args :
        x : (float)
        y : (float)

    Returns :
        float : sum

    >>> addition(3,4)
    7

    >>> addition(2.3,7.1)
    8

    """
    return(x+y)

if __name__ == "__main__" :
    import doctest
    print("Fonction addition")
    print(addition(5,8))


    doctest.testmod(verbose = True)
