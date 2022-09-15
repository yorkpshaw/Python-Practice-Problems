# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.


def has_quorum(attendees_list, members_list):
    # get number of people in attendees list
    num_attendees = len(attendees_list)

    # get the value of half of the members list
    num_members = len(members_list)

    # do a comparison of num attendees and to 50% of members

    if num_attendees / num_members >= 0.5:
        return True
    else:
        return False
    # use >=


print(has_quorum(["Bart", "Jay", "Terra", "York"], ["Onyx", "Catman"]))
print(has_quorum(["Bart", "Jay"], ["Onyx", "Catman", "Terra", "York"]))
print(has_quorum(["Bart"], ["Onyx", "Catman", "Jay", "Terra", "York"]))
print(has_quorum(["Bart", "Jay", "Terra", "York", "Onyx"], ["Catman"]))
