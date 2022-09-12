# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.

# It uses the built-in function reversed and the join method
# for string objects.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


# set a variable to be the reversed string of word
# set another variable to be the reversed word variable, with with .join
# and no spaces
# if the test case (reversed word of parameter) is equal to the parameter, then return true
# otherwise, return false


def is_palindrome(word):
    reversed_word = reversed(word)
    new_word = "".join(reversed_word)

    if new_word == word:
        return True
    else:
        return False


print(is_palindrome("racecar"))
print(is_palindrome("nope"))
