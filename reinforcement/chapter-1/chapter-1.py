# R 1.1

# Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

# Solution
"""
def is_multiple(n, m):
    return n / m == 0
"""


# R 1.2

# Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

# Solution
"""
def is_even(k):
    while k:
        if k-2 == 0:
            return True
        elif k-2 == 1:
            return False
        else:
            k -= 2
"""


# R 1.3

# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

# Solution
"""
def minmax(data):
    pass
"""


# R 1.4

# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

# Solution
"""
def sum_of_pos_int_below(n):
    total = 0
    for k in range(1, n):
        sqr = k * k
        total += sqr
    print(total)
"""


# R 1.5

# Give a single command that computes the sum from Exercise R-1.4, rely-
# ing on Python’s comprehension syntax and the built-in sum function.

# Solution
"""
def sum_of_pos_int_below(n):
    total = sum(k*k for k in range(1, n))
    return total
"""

# R 1.6

# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

# Solution
"""
def sum_of_pos_odd_int_below(n):
    total = 0
    for k in range(1, n):
        if k % 2 == 1:
            sqr = k * k
            total += sqr
        else:
            pass   
    return total
"""


# R 1.7

# Give a single command that computes the sum from Exercise R-1.6, rely-
# ing on Python’s comprehension syntax and the built-in sum function.

# Solution
"""
def sum_of_pos_odd_int_below(n):
    total = sum(k * k for k in range(1, n) if k % 2 == 1)
    return total
"""

# R 1.8

# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for in-
# dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?

# my solution
"""
j = n + k
"""


# R 1.9

# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80

# my solution
"""
range(50, 81, 10)
"""


# R 1.10

# What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

# my solution
"""
range(8, -9, -2)
"""
   
