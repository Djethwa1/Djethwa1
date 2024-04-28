import spacy
nlp = spacy.load("en_core_web_sm")

tokens = nlp("cat apple monkey banana ")
for token1 in tokens:
  for token2 in tokens:
    print(token1.text, token2.text, token1.similarity(token2))

'''
******similarities between cat, monkey and banana*******

--Output--

cat cat 1.0
cat apple 0.20368057489395142
cat monkey 0.5929929614067078
cat banana 0.2235882729291916
apple cat 0.20368057489395142
apple apple 1.0
apple monkey 0.2342509627342224
apple banana 0.6646700501441956
monkey cat 0.5929929614067078
monkey apple 0.2342509627342224
monkey monkey 1.0
monkey banana 0.4041501581668854
banana cat 0.2235882729291916
banana apple 0.6646700501441956
banana monkey 0.4041501581668854
banana banana 1.0

According to the output, we can observe these similarities

   - When the for loop iterates over "cat" and "monkey," the resulting similarity rate is 0.59299..., whereas when it compares "cat" to "apple," the similarity rate is lower
   - The reason for the discrepancy in similarity rates between "cat" and "monkey" (0.59299...) and "cat" and "apple" (0.20368...) when the for loop is applied is due to the fact that spaCy recognizes "cat" and "monkey" as both being animals, while "cat" and "apple" are recognized as an animal and a fruit, respectively.
   - Similarly to the previous comparison, the similarity rate between "apple" and "banana" is higher at 0.664670... because spaCy recognizes both as fruits.
   - Based on the above results, the noteworthy observation is that the relationship rate between "monkey" and "banana" is as high as 0.404150, despite the objects being different. This demonstrates the model's ability to recognize practical real-world relationships between objects. However, we cannot observe a similar relationship between "cat" and "banana," or "cat" and "apple."
'''

print()
print("****Comparison on my own example****")
print(" ")


# Creating list of token for each item
my_token = nlp("man monkey chicken frog")

# create a loop to compare the similarities
for token1 in my_token:
  for token2 in my_token:
    print(token1.text, token2.text, token1.similarity(token2))
similarity = token1.similarity(token2)





