# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the string is empty, then return the empty string.
# create an empty string variable
# if the letter is not in there, increment


def remove_duplicate_letters(s):
    if len(s) == 0:
        return " "
    str = ""
    for letter in s:
        if letter not in str:
            str += letter

    return str


print(remove_duplicate_letters("abcabc"))
print(remove_duplicate_letters("abccba"))
print(remove_duplicate_letters("abccbad"))
print(remove_duplicate_letters("abc"))
print(remove_duplicate_letters(""))
