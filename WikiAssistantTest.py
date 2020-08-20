import wikipedia
print()
print()
print()
search_phrase = input("Type in a search phrase: ")
number_of_sentences = input("How many sentences would you like me to collect for you: ")
output_sentence = wikipedia.summary(search_phrase, sentences=number_of_sentences)

print(output_sentence)

# print(wikipedia.summary("python"))
print(wikipedia.page("python").content)