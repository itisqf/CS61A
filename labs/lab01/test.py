def sum_digits(n):
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

a = 0
a = sum_digits(880)
print (a)