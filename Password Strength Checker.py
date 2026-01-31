#Home Work Question
# generate random password
# check password strength
# count character used in password
# gives a strength score using math
# saves the result in a file using OS

import string
import math
import os
from collections import Counter
# taking password from user
password = input("Enter your password: ")
# checking password strength
has_upper = any(c.isupper() for c in password) # checks capital letters
has_lower = any(c.islower() for c in password) # checks small letters
has_digit = any(c.isdigit() for c in password) # checks numbers
has_symbol = any(c in string.punctuation for c in password) # checks symbols
# counting how many conditions are true
strength_value = sum([has_upper, has_lower, has_digit, has_symbol])
# giving score using maths
score = math.ceil((strength_value / 4) * 100)
# deciding strength level
if score < 40:
    level = "Weak"
elif score < 70:
    level = "Medium"
else:
    level = "Strong"
# counting each character in password
char_count = Counter(password)
# saving result in file using os
folder = "password_reports"
if not os.path.exists(folder): # create folder if not there
    os.mkdir(folder)
path = os.path.join(folder, "report_user.txt")
file = open(path, "w")
file.write("User Password: " + password + "\n")
file.write("Character Count: " + str(char_count) + "\n")
file.write("Strength Score: " + str(score) + "%\n")
file.write("Strength Level: " + level + "\n")
file.close()
# printing output
print("Password Entered:", password)
print("Character Count:", char_count)
print("Score:", score, "%")
print("Strength Level:", level)