def count_stair_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n-1) + count_stair_ways(n - 2)

"""Write a function that takes a list s and returns
   a new list that keeps only the even-indexed 
   elements of s and multiplies them by theri 
   corresponding index"""
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    ###先写出for循环的形式，重点在遍历的是index而不是
    ###元素
    ###result = []
    ###for i in range(len(s)):
    ###    if i % 2 == 0:
    ###        result += i * s[i]
    ###return result
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]

"""Write a function that takes in a list and returns
   the maximum product that can be formed using
   nonconsecutive elements of the list. The input list
   will contain only numbers greater than or equal to 1
"""
def max_product(s):
    """Return the maximum product that can be formed
    using non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2]) # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])# 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()