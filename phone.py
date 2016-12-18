import re

bible = open("my-directory-list.txt", "r")
regex = re.compile(r'^[7896]\d{9}$')

for line in bible:
    four_letter_words = regex.findall(line)
    for word in four_letter_words:
        print word