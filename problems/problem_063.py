# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem


def shift_letters(str):
    new_word = ""  # A string will be the result

    for letter in str:  # loop over the string
        if letter == "Z":  # If letter is Z or z, they become A or a
            new_letter = "A"
        elif letter == "z":
            new_letter = "a"
        else:  # Use if/elif/else statements to knock out those conditions, then append
            new_letter = chr(
                ord(letter) + 1
            )  # chr will output the letter from a unicode number, ord(letter) represents the unicode number of a letter
        new_word += new_letter

    return new_word


print(shift_letters("import"))
print(shift_letters("ABBA"))
print(shift_letters("Kala"))
print(shift_letters("zap"))
