import doctest
"""Q1.1: Write a function that takes in a function and a number n
    and prints numbers from 1 to n where calling cond on that number
    returns True."""
def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1
"""
Q1.2: Write a function similar to keep_ints like before, but now
now it takes in a number n and returns a function that has one 
parameter cond. The returned function prints out numbers from 1
to n where calling cond on that number returns True.
"""
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.
    
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def keeper(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return keeper

def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)
        return g
    return f

curry2 = lambda h: lambda x: lambda y: h(x, y)

if __name__ == '__main__':
    import doctest
    doctest.testmod()