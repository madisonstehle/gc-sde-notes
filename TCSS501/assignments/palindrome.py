"""
Name: Madison Stehle
UWNetId: 2279369
TimeComplexity: O(n)
"""


def is_palindrome(the_string):
    """
       Evaluates a given string and determines whether or not it is a palindrome.
       :param the_string: The string to evaluate.
       :returns: True when the string is a palindrome, False otherwise.
    """

    reverse_array = []
    clean_string = the_string.replace(' ', '').lower()

    for i in range(len(clean_string), 0, -1):
        reverse_array.append(clean_string[i-1])

    reverse_string = ''.join(reverse_array)

    return reverse_string == clean_string
