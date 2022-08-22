# Complete the fizzbuzz function to return
# * The word "fizzbuzz" if number is evenly divisible by
#   by both 3 and 5
# * The word "fizz" if number is evenly divisible by only
#   3
# * The word "buzz" if number is evenly divisible by only
#   5
# * The number if it is not evenly divisible by 3 nor 5
#
# Try to combine what you have done in the last two problems
# from memory.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# check if number % 3 and number % 5 == 0; if so, return fizzbuzz
# if number only divisible by 3, return fizz
# if number only divisible by 5, return buzz


def fizzbuzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number


print(fizzbuzz(6))
print(fizzbuzz(15))
print(fizzbuzz(25))
print(fizzbuzz(29))
print(fizzbuzz(36))
print(fizzbuzz(45))
print(fizzbuzz(50))
print(fizzbuzz(67))
