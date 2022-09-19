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


def shift_letters(word):
    new_word = ""
    for letter in word:
        if letter == "Z":
            new_letter = "A"
        elif letter == "z":
            new_letter = "a"
        else:
            new_letter = chr(ord(letter) + 1)
        new_word += new_letter
    return new_word


# Create an empty string variable to return
# loop over the string
# if the letter is Z/z, they become A/a
# use if/elif/else statements to knock those conditions out
# ord, the unicode number, is +1 for each character
# chr will convert all those unicode numbers into letters
