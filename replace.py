"""Using the replace function to substitute exclamation marks in a sentence with spaces,
use upper function to conver the sentence to upper case and finaly reversing the sentence"""
sentence= "The!quick!brown!fox!jumps!over!the!lazy!dog!"
new_sentence=sentence.replace("!" , " ")
print(new_sentence)
uppercase_sentence= new_sentence.upper()
print(uppercase_sentence)
reverse_sentence=uppercase_sentence[::-1]
print(reverse_sentence)