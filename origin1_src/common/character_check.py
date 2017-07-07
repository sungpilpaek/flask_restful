import string


def is_valid(input_string):
    invalidChars = set(string.punctuation.replace("_", ""))

    if any(char in invalidChars for char in input_string):
        return False
    
    return True