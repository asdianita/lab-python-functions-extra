import string


def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    # your code goes here
    list2set = set(lst) # Change the list into a set to remove duplicate elements.
    lista = list(list2set) # Change back to list.
    return lista

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    # your code goes here
    lowercase = sum(map(str.islower, string))
    uppercase = sum(map(str.isupper, string))
    count = (f'Count of uppercase letters: {uppercase}',f'Count of lowercase letters: {lowercase}')
    return count

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    # your code goes here
    import string
    new_sentence = sentence.translate(str.maketrans('','',string.punctuation))
    return new_sentence

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    # your code goes here

    frase_limpita = remove_punctuation_f(sentence).replace(' ','!') # To count words, let's replace " " with "!", that will get one ! for each word.
    while "!!" in frase_limpita:
        frase_limpita = (frase_limpita).replace('!!','!') # In case of two or more spaces together, this loop cleans it.
    print(frase_limpita)
    
    if frase_limpita.endswith("!"): #If the sentence ends with !, there would be one ! for each word.
        conteo = 0
    else: # If not, we need to take into account the last word.
        conteo = 1

    for char in frase_limpita:
        if char == '!':
            conteo += 1

    return conteo