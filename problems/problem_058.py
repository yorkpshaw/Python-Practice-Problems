# Write a function that meets these requirements.
#
# Name:       group_cities_by_state
# Parameters: a list of cities in the format "«name», «st»"
#             where «name» is the name of the city, followed
#             by a comma and a space, then the two-letter
#             abbreviation of the state
# Returns:    a dictionary whose keys are the two letter
#             abbreviations of the states in the list and
#             whose values are a list of the cities appearing
#             in that list for that state
#
# In the items in the input, there will only be one comma.
#
# Examples:
#     * input:   ["San Antonio, TX"]
#       returns: {"TX": ["San Antonio"]}
#     * input:   ["Springfield, MA", "Boston, MA"]
#       returns: {"MA": ["Springfield", "Boston"]}
#     * input:   ["Cleveland, OH", "Columbus, OH", "Chicago, IL"]
#       returns: {"OH": ["Cleveland", "Columbus"], "IL": ["Chicago"]}
#
# You may want to look up the ".strip()" method for the string.


def group_cities_by_state(cities):
    dict = {}
    for city_name in cities:
        cityname = city_name.split(", ")
        city = cityname[0]
        state = cityname[1]
        if state not in dict:
            dict[state] = [city]  # dict[key] = value
        else:
            dict[state].append(city)
    return dict


print(group_cities_by_state(["San Antonio, TX"]))
print(group_cities_by_state(["Springfield, MA", "Boston, MA"]))
print(group_cities_by_state(["Cleveland, OH", "Columbus, OH", "Chicago, IL"]))


# dict[key].append(newvalue) is the same as value.append(newvalue)

# If the cities have the same abbreviated state, they belong in the same value
# to the abbreviated state's key
# Index 1 in each list will be the dictionary's key
# Index 0 in each list will be the dictionary's value

# if "key1" in d:
#     print("this will execute")

# if "nonexistent key" in d:
#     print("this will not")


# if index 1 is not in the dictionary, then set the index 1 to be a key,
# and the value to be a list
# If index 1 is in the dictionary,

# Index 0 will go into that and you don't need another index 1
# append index 0 into the value
# where is the value of the key

# return a dictionary,
# the dictionary's key should be the state abbrevation
# the dictionary's value(s) should be the city name(s)
# .strip
