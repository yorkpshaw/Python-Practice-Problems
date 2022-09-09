# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z) .islower
#   * It must have at least one uppercase letter (A-Z) .isupper
#   * It must have at least one digit (0-9) .isdigit
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it len(password) >= 6 and <= 12
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"


def check_password(password):
    is_valid = False
    lowercase_found = False
    uppercase_found = False
    number_found = False
    special_found = False
    password_length = False
    lowercase_letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    uppercase_letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_char = ["$", "!", "@"]
    for char in password:
        if char in lowercase_letters:
            lowercase_found = True
        if char in uppercase_letters:
            uppercase_found = True
        if char in numbers:
            number_found = True
        if char in special_char:
            special_found = True
    if len(password) >= 6 and len(password) <= 12:
        password_length = True
    # print(
    #     lowercase_found,
    #     uppercase_found,
    #     number_found,
    #     special_found,
    #     password_length,
    # )
    if (
        lowercase_found
        and uppercase_found
        and number_found
        and special_found
        and password_length
    ):
        is_valid = True

    return is_valid


print(check_password("aF69!#"))
print(check_password("GG"))
print(check_password("1A!ju90"))
