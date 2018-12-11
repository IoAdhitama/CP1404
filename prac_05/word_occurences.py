word_occurences = {}

text = str(input("Text: "))
words = text.split()

for word in words:
    if word in word_occurences:
        word_occurences[word] += 1
    else:
        word_occurences[word] = 1

word_occurences_keys = [key for key in word_occurences]
word_occurences_keys.sort()

max_word_length = 0
for word in word_occurences_keys:
    if len(word) > max_word_length:
        max_word_length = len(word)

for i in word_occurences_keys:
    print("{:{}} : {}".format(i, max_word_length, word_occurences[i]))
