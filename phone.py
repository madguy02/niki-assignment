import re

phone = open("my-directory-list.txt", "r")
regex = re.compile(r'^[7896]\d{9}$')

for line in phone:
    phone_numbers = regex.findall(line)
    for word in phone_numbers:
        print word