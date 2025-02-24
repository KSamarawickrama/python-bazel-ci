def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s 

def count_vowels(s):
    return sum(1 for char in s.lower())

def capitalize_words(s):
    """
    Capitalizes the first letter of each word in the string.
    """
    return " ".join(word.capitalize() for word in s.split())

def remove_duplicates(s):
    """
    Removes duplicate characters from the string while preserving order.
    """
    seen = set()
    return "".join(seen.add(char) or char for char in s if char not in seen)