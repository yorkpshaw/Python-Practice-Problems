# Complete the translate function which accepts two
# parameters, a list of keys and a dictionary. It returns a
# new list that contains the values of the corresponding
# keys in the dictionary. If the key does not exist, then
# the list should contain a None for that key.
#
# Examples:
#   * keys:       ["name", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     ["Noor", 29]
#   * keys:       ["eye color", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [None, 29]
#   * keys:       ["age", "age", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [29, 29, 29]
#
# Remember that a dictionary has the ".get" method on it.

# Return an empty list of Values from a dictionary
# loop over the list of keys
# if that key in the list is in the dictionary,
# use .get to retrieve the values from the dictionary parameter
# pass the key variable as an argument in .get() to check if there
# append those values


def translate(key_list, dictionary):
    result = []

    for k in key_list:
        result.append(dictionary.get(k))

    return result


print(translate(["name", "age"], {"name": "Noor", "age": 29}))
print(translate(["eye color", "age"], {"name": "Noor", "age": 29}))
print(translate(["age", "age", "age"], {"name": "Noor", "age": 29}))
