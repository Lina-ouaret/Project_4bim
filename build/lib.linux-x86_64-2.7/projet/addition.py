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
    
    >>> addition(2,7.1)
    9.1

    """
    return(x+y)

if __name__ == "__main__" :
    print("Fonction addition")
    print(addition(5,8))

    import doctest
    doctest.testmod(verbose = True)
