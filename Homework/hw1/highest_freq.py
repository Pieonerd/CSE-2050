from letters import letter_count, letter_frequency

def highest_freq(file):
    """
    This function calculates the letter with the highest frequency in which it appears in a text document
    """
    #Creates the letter frequency dictionary and searches for the value with the highest frequency
    freq_dict = letter_frequency(file)
    MAX = max(freq_dict.values())

    #Searches for the key with the corresponding value in order to return the letter with the highest frequency
    for key, value in freq_dict.items():
        if value == MAX:
            return key, value

#Assertion test for the highest_frequency function
expected_max = ('t', 0.2727272727272727)
actual_max = highest_freq('test.txt')
assert(expected_max == actual_max)

#Asks for user input and prints results
user_input = input('Enter file name:\n')
print(highest_freq(user_input))