# def print_upper_words(words):
#     """for a list of words, print each word in upper case on a separate line"""
#     for word in words:
#         print(word.upper())
   
# print_upper_words(["hello", "and", "goodbye"])


# def print_upper_e_words(words):
#     """for a list of words, print each word that begins with 'e' in upper case on a separate line"""
#     for word in words:
#         if word[0].upper() == 'E':
#             print(word.upper())
   
# print_upper_e_words(["Excited", "to", "exclaim", "hello", "and", "goodbye", "to", "everyone", "everywhere"])


def print_upper_some_words(words, must_start_with):
    """for a list of words, print each word that begins with a letter in the input list, in upper case, on a separate line"""
    for word in words:
        for letter in must_start_with:
            if word[0].upper() == letter.upper():
                print(word.upper())
   
print_upper_some_words(["Excited", "to", "exclaim", "hello", "or", "hey", "and", "yo", "goodbye", "to", "everyone", "everywhere"], ["h", "y"])
print_upper_some_words(["Excited", "to", "exclaim", "hello", "or", "hey", "and", "yo", "goodbye", "to", "everyone", "everywhere"], ["e", "g"])
