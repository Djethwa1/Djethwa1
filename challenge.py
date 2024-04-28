'''Little sisters coding challenge - help little sister with English vocabulary homework.
Her class is learning to create new words by adding prefixes and suffixes to a word, removing suffixes from 
a word and transforning words from one form to another'''

## Adding a prefix "un"

'''The function add_prefix_un(<word>) takes a word as a parameter and returns a 
new un prefixed word:'''

def add_prefix_un(word: str) -> str:
    """
    Adds the prefix 'un' to a given word.
    """
    return "un" + word

print(" 1. Add a prefix 'un' to a word:")
print(" ")

print(add_prefix_un("happy"))  # Output: "unhappy"
print(add_prefix_un("manageable"))  # Output: "unmanageable"

## Adding prefix to word groups

'''The function make_word_groups(<vocab_words>) takes a vocab_words as a 
parameter in the following form: [<prefix>, <word_1>, <word_2> .... <word_n>], and returns 
a string with the prefix applied to each word that looks like:
<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'''

def make_word_groups(vocab_words: list) -> str:
    """
    Groups vocabulary words with a prefix using '::'.
    """
    prefix = vocab_words[0]
    return f"{prefix} :: " + " :: ".join(f"{prefix}{word}" for word in vocab_words[1:])

print(" ")
print("2. Adding a prefix to word groups:")
print(" ")
print(make_word_groups(['en', 'close', 'joy', 'lighten']))
print(" ")

# Output: "en :: enclose :: enjoy :: enlighten"

## Removing suffix "ness"

'''The function remove_suffix_ness(<word>) takes in a word, and returns the root word 
without the ness suffix in it.'''

def remove_suffix_ness(word: str) -> str:
    """
    Removes the suffix 'ness' from a word, or replaces it with 'y' if the word ends with 'i'.
    """
    return word[:-4] if word[-5] != "i" else word[:-5] + "y"

print("3. Removing suffix 'ness' from a word:")
print(" ")
print(remove_suffix_ness("happiness"))  # Output: "happy"
print(" ")

## Extract and transform a word

'''This function returns the extracted adjective as a verb by using the adjective_to_verb
(<sentence>, <index>) function that takes two parameters.
A sentence using the vocabulary word, and the index of the word, once that sentence is split 
apart.'''

def adjective_to_verb(sentence: str, index: int) -> str:
    """
    Extracts an adjective from a sentence and turns it into a verb by adding the 'en' suffix.
    Args:
        sentence (str): The input sentence containing the vocabulary word.
        index (int): The index of the word in the sentence (once split apart).

    Returns:
        str: The transformed verb.
    """
    result = ""
    for char in sentence.split(" ")[index]:
        if char.isalpha():
            result += char
    return result + "en"

# Example usage:
print("4. Extract and transform a word - verbs extracted from adjectives in a sentence:")
print(" ")
print(adjective_to_verb('I need to make that bright.', -1))  # Output: "brighten"
print(adjective_to_verb('It got dark as the sun set.', 2))  # Output: "darken"