# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# if the ingredient list contains flour, eggs, and oil, return true
# if it contains anything else, return false
# loop over the list to see if it contains those 3 elements


def can_make_pasta(ingredients):
    if (
        "flour" in ingredients
        and "eggs" in ingredients
        and "oil" in ingredients
    ):
        return True
    else:
        return False


print(can_make_pasta(["flour", "eggs", "oil"]))
print(can_make_pasta(["flour", "eggs", "oil", "sugar"]))
print(can_make_pasta(["flour", "bacon", "oil"]))
print(can_make_pasta(["pickles", "are", "gross"]))
