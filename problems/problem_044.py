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


def translate(key_list, dictionary):
    empty_list = []
    for key in key_list:
        empty_list.append(dictionary.get(key))

    return empty_list


print(translate(["name", "age"], {"name": "Noor", "age": 29}))
print(translate(["eye color", "age"], {"name": "Noor", "age": 29}))
print(translate(["age", "age", "age"], {"name": "Noor", "age": 29}))


# key_list parameter is what we want to get from the dictionary parameter
# Return a list of values from the key_list parameter
