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
# If the list is empty, then return the empty string.

# create an empty string variable
# loop over the string
# if the character is not in the empty string variable,
# then add that character to the empty string variable


def remove_duplicate_letters(s):
    # if s == "":
    #     return s
    no_duplicates = ""
    for char in s:
        if char not in no_duplicates:
            no_duplicates += char

    return no_duplicates


print(remove_duplicate_letters("abcabc"))
print(remove_duplicate_letters(""))
print(remove_duplicate_letters("abccba"))
print(remove_duplicate_letters("abccbad"))
