# Write a function that meets these requirements.
#
# Name:       count_word_frequencies
# Parameters: sentence, a string
# Returns:    a dictionary whose keys are the words in the
#             sentence and their values are the number of
#             times that word has appeared in the sentence
#
# The sentence will contain now punctuation.
#
# This is "case sensitive". That means the word "Table" and "table"
# are considered different words.
#
# Examples:
#    * sentence: "I came I saw I learned"
#      result:   {"I": 3, "came": 1, "saw": 1, "learned": 1}
#    * sentence: "Hello Hello Hello"
#      result:   {"Hello": 3}

## FUNCTION PSEUDOCODE

# Create an empty dictionary variable to return
# Create a variable that splits the string into elements
# loop over the split variable
# if the word is in the empty dictionary, increment key value by 1
# otherwise, keep it at 1


def count_word_frequencies(sentences):

    counts = {}
    words = sentences.split(" ")

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


print(count_word_frequencies("Hello Hello Hello"))
print(count_word_frequencies("I came I saw I learned"))
