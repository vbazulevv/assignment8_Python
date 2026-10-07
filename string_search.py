text = "Hello World. Welcome to the World of python."

first = input ("Choose a word from a text above: ")
second = input ("Choose one more word from a text above: ")

First = text.find(first)
Second = text.rfind(second)

print("Text:", text)
print("First World:", First)
print("Second World:", Second)
