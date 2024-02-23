'''In This program the first part alternates the individual characters in a string between 
uppercase and lowercase and 
the second part alternates the words in a string between lowercase and uppercase'''


sentence = "hello world"
character_storage = [] #blank list to store all the sentences characters
char = 0

for i in (sentence): 
    if char % 2 == 0:
        character_storage += i.upper()
    else:   
        character_storage += i.lower()
    char += 1

print("".join(character_storage))


new_sentence=sentence.split()
word_storage = []
char = 0

for i in new_sentence:
    if char % 2 == 0:
        word_storage += i.lower()
    else:   
        word_storage += i.upper()
    char += 1
    if char !=0:
      word_storage += " "
print("".join(word_storage))

