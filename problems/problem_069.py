# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
#
# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
#
# Example:
#    student = Student("Malik")
#
#    print(student.get_average())    # Prints None
#    student.add_score(80)
#    print(student.get_average())    # Prints 80
#    student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#
# There is pseudocode for you to guide you.


# class Student
# method initializer with required state "name"
# self.name = name
# self.scores = [] because its an internal state

# method add_score(self, score)
# appends the score value to self.scores

# method get_average(self)
# if there are no scores in self.scores
# return None
# returns the sum of the scores divided by
# the number of scores


class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average(self):
        if len(self.scores) == 0:
            return None

        count = 0
        for sum in self.scores:
            count += sum
            average = count / len(self.scores)

        return average


student = Student("York")
print(student.get_average())
student.add_score(100)
student.add_score(90)
print(student.get_average())
student.add_score(66)
student.add_score(33)
print(student.get_average())
