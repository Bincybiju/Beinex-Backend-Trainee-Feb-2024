"""Write a function that takes a sentence as input and returns a new sentence 
with the words reversed, while keeping the order of the words in the 
sentence."""

def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(sentence)
print("Reversed sentence:", reversed_sentence)
