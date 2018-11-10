# sentence = input("Please enter some text to find out which word is the longest: \n")
sentence = 'aa aa bbb bbb bbb ae do ab bb fq bbb bbb'
words = sentence.split()
print(words)

longest_word = []

for word in words:
    if longest_word == []:
        longest_word.append(word)
    else:
        if len(word) == len(longest_word[0]):
            longest_word.append(word)
        if len(word) > len(longest_word[0]):
            longest_word = [word]


print(longest_word)
