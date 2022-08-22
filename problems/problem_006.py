# Complete the can_skydive function so that determines if
# someone can go skydiving based on these criteria
#
# * The person must be greater than or equal to 18 years old, or
# * The person must have a signed consent form

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# create an input statement asking their age
# create an input statement asking if they have signed a consent form
# create an age variable (with a int()) and a consent form variable (str)
# create an age variable
# create a consent form variable
# create an if/or statement that says if they're >= 18 years old OR
# has signed a form, they can skydive
# if the person have not done either, return a print statement
# that says you cannot go


# def can_skydive(age, has_consent_form):

#     person_age = int(input("How old are you? \n"))
#     # consent_form = str(input("Did you have a parent sign a consent form?"))

#     if person_age >= 18:
#         print("Ok. You do not need a consent form and you can go skydiving!")
#         exit()
#     elif person_age < 18:
#         consent_form = str(input("Did you have a parent sign a consent form?"))
#         if consent_form == "yes":
#             print("You have cool parents. Go skydiving!")
#             exit()
#         else:
#             print("Get older or sign the consent form :(")
#             exit()


# can_skydive(18, "yes")


def can_skydive(age, has_consent_form):
    if age >= 18 or has_consent_form.lower() == "yes":
        return True
    else:
        return False


print(can_skydive(21, "no"))
print(can_skydive(15, "YES"))
print(can_skydive(15, "no"))
print(can_skydive(15, "yes"))
print(can_skydive(100, "yes"))
print(can_skydive(-3, "nah"))
