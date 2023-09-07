def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    product = 1
    i = 0
    while i < k:
        product = product * (n - i)
        i += 1
    return product



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    n = 1
    while y//n >= 10:
        n = n * 10

    sum = 0
    while n > 0:
        sum = sum + y // n
        y = y % n
        n = n // 10
    return sum



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    "*** YOUR CODE HERE ***"
    i = 1
    while n//i >= 10:
        i = i * 10

    first_dig = n // i
    n = n % i
    i = i // 10

    while i > 0:
        second_dig = n // i
        if first_dig == second_dig and first_dig == 8:
            return True
        else:
            n = n % i
            i = i // 10
            first_dig = second_dig
    
    return False


