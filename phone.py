import re
import niki

phone = open("my-directory-list.txt", "r")
regex = re.compile(r'^[7-9][0-9]{9}$')

for line in phone:
    phone_numbers = regex.findall(line)
    for word in phone_numbers:
        print word