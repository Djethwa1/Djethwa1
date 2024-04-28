import spacy

nlp = spacy.load('en_core_web_sm')

# List of garden Garden path sentences, the first two sentences were found on the internet, the other three were already provided in the task

garden_1 = "The florist sent the flowers was pleased."
garden_2 = "The horse named Jonny raced passed the barn fell."
garden_3 = "Mary gave the child a band-Aid."
garden_4 = "That Jill is never here hurts."
garden_5 = "The cotton clothing is made of grows in Mississippi."

gardenpathSentences = [garden_1, garden_2, garden_3, garden_4, garden_5]

#Tokenization 

print()
print(" Results after tokenizing each sentence")
print()
for sentences in gardenpathSentences:
    doc_nlp = nlp(sentences)
    for token in doc_nlp:
        print(token.text , token.orth_, token.pos_) 

# Tokenisation

# Named Entity recognition
print(" ")
print(" Results after Named entity recognition")
print(" ")
for sentences in gardenpathSentences: 
        print([(token, token.label_, token.label) for token in nlp(sentences).ents])


# Get an explanation of two of the entities and print it
        
print(" ")
print(" Results of explanation of Entities")

print(" ")

print("The entity GPE is associated with :" , spacy.explain("GPE"))

print(" ")

print("The entity PERSON is associated with:" , spacy.explain("PERSON"))


'''The two entities i looked up were "GPE" and "PERSON" 
the explanation of "GPE" was that its a Country, City or State
the explanation of "PERSON" was people
GPE did not make any sense but the entity PERSON did make sense in terms of the word associated with it i.e MARY was the name of a person'''
