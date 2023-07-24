def get_primes(numbers):
    prime_numbers = [n for n in numbers if n > 1
                     and (n % 2 != 0 or n == 2)
                     and (n % 3 != 0 or n == 3)
                     and (n % 5 != 0 or n == 5)
                     and (n % 7 != 0 or n == 7)]
    for n in prime_numbers:
        yield n


# from math import sqrt
#
# 
# def get_primes(numbers: list):
#     for number in numbers:
#         if number <= 1:
#             continue
#
#         for divisor in range(2, int(sqrt(number)) + 1):
#             if number % divisor == 0:
#                 break
#         else:
#             yield number


print(list(get_primes([1000000007, 2, 4, 3, 5, 6, 9, 1, 0])))
#print(list(get_primes([-2, 0, 0, 1, 1, 0])))