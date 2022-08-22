# Complete the is_divisible_by_3 function to return the
# word "fizz" if the value in the number parameter is
# divisible by 3. Otherwise, just return the number.
#
# You can use the test number % 3 == 0 to test if a
# number is divisible by 3.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


# return "fizz" if number is divisible by 3
# use a divider operator to check if number / 3 == 0
# if it is, return fizz
# if the number != 3, then return the number


def is_divisible_by_3(number):
    if number % 3 == 0:
        return "Fizz"
    else:
        return number


print(is_divisible_by_3(3))
print(is_divisible_by_3(6))
print(is_divisible_by_3(1))
print(is_divisible_by_3(10))
print(is_divisible_by_3(66))
print(is_divisible_by_3(100))
