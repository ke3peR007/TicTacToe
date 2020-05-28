text = input()
text = text.lower()
# words = text.split(maxsplit=2)
# print(words)
words = text.split(" ")
print(words)
for word in words:
    # finish the code here
    if word.endswith(".com"):
        print(word)
