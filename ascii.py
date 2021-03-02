file_in = open("two_cities_ascii.txt","r")

"""creating a list with all the required characters from the ASCII file"""
asciichars = []
for line in file_in:
    for char in list(line):
        if ord(char) % 2 == 1 and ord(char) >= 97: 
            asciichars.append(ord(char))

"""excluded even ascii codes and characters before the letter a 
since their appearance percentages are too small to be considered"""

"""turning ASCII codes back to characters"""
chars = []
for i in asciichars:
    chars.append(chr(i))

file_in.close ()

"""counting all the characters"""
counted = {}
for i in sorted(chars):
    counted[i] = counted.get(i, 0) + 1

"""finding total amount of characters that fit our criteria"""
total = 0    
for i in counted.values():
    total += i

"""transforming counted amounts to percentage and printing the histogram"""
for i in counted:
    counted[i] = round(counted.get(i)*100/total) 
    print(i, '*' * counted[i])