import string

def letter_count(file):
    """
    Processes how many times each letter appears in a text document
    """

    #Creates an empty dictionary
    num_occurrences = {}

    #Opens the file and reads each line
    f = open(file)
    text = f.readlines()
    f.close()

    #Iterating through each letter
    for word in text:
        for letter in word.lower():
            if letter in string.ascii_letters:
                #Creates a new dictionary key for every new letter that appears
                if letter not in num_occurrences:
                    num_occurrences[letter] = 1
                #If letter exists in dictionary, adds one to its value
                else:
                    num_occurrences[letter] += 1

    #Returns the dictionary
    return num_occurrences


def letter_frequency(file):
    '''
    Calculates the frequency of each letter in a text document
    '''
    #Creates an empty dictionary
    num_frequency = {}

    #Recalls the letter_count function
    counts = letter_count(file)

    #Finds the total number of letters
    total_num_letters = 0
    for values in counts.values():
        total_num_letters += values

    #Calculates the ratio of a specific letter to the total number of letters
    for key, value in counts.items():
        ratio = value / total_num_letters
        num_frequency[key] = ratio

    #Returns the dictionary
    return num_frequency

if __name__ == '__main__':
    #Assertion test for the letter_count function
    expected_count = {'t': 3, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 1}
    actual_count = letter_count('test.txt')
    assert(expected_count == actual_count)

    #Assertion test for the letter_frequency function
    expected_frequency = {'t': 0.273, 'h': 0.091, 'i': 0.182, 's': 0.273, 'a': 0.091, 'e': 0.091}
    actual_frequency = letter_frequency('test.txt')
    for key, value in actual_frequency.items():
        actual_frequency[key] = round(value, 3)
    assert(expected_frequency == actual_frequency)

#Asks for file input and prints results
    user_input = input('Enter file name:\n')
    print(letter_count(user_input))
    print(letter_frequency(user_input))