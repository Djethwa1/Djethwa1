'''This code requests user to input a sentence
the sentence is stored as a variable
the len function is used to calculate the length of the sentence
slicing is used to find the last word in the sentence at position (-1)
th replace function is used to replace all occurances of the last letter
use extended slicing to print last 3 and first 2 characters of sentence and
forming new word with sliced characters '''
sentence=input("Please enter a sentence:")
print(sentence)
str_manip=sentence
print(len(str_manip))
last_letter=str_manip[-1]
print(last_letter)
new_sentence=str_manip.replace(last_letter , "@")
print(new_sentence)
print(str_manip[:-4:-1])
x=(str_manip[:-4:-1]) #x=last 3 characters
y=(str_manip[:2:]) #=first 2 characters
print(x+y)