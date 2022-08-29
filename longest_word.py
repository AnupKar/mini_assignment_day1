fin = open("longest_word.txt","r")
str = fin.read()
words = str.split()
max_len = len(max(words, key=len))
for word in words:
    if len(word)==max_len:
        longest_word =word
print(longest_word)