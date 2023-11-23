def hailstone(n):
    """Print out the hailstonen sequence starting at n, 
    and return the number of elements in the sequence.
    
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    if n == 1:
        print("1")
        return 1
    elif n % 2 == 0:
        print(n)
        return 1 + hailstone(n//2)
    else:
        print(n)
        return 1 + hailstone(n*3+1)

def merge(n1, n2):
    """Write a procedure merge(n1, n2) which takes numbers with 
    digits in decreasing order and returns a single number with
    all of the digits of the two, in decreasing order. Any num-
    ber merged with 0 will be that number (treat 0 as having no
    digits). Use recursion
    
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge(21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 <= n2 % 10:
        return n1 % 10 + 10 * merge(n1//10, n2)
    else:
        return n2 % 10 + 10 * merge(n1, n2//10)

if __name__ == '__main__':
    import doctest
    doctest.testmod()