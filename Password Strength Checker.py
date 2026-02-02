#Home Work Question
# generate random password
# check password strength
# count character used in password
# gives a strength score using math
# saves the result in a file using OS

import re
import math
import os
from collections import Counter
# taking password input from user
password = input("Enter your password: ")
# checking rules using regex
has_upper = bool(re.search(r"[A-Z]", password))        # checks uppercase
has_lower = bool(re.search(r"[a-z]", password))        # checks lowercase
has_digit = bool(re.search(r"[0-9]", password))        # checks numbers
has_symbol = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))  # checks symbols
# counting how many conditions are satisfied
strength_value = sum([has_upper, has_lower, has_digit, has_symbol])
# giving score using math
score = math.ceil((strength_value / 4) * 100)
# deciding strength level
if score < 40:
    level = "Weak"
elif score < 70:
    level = "Medium"
else:
    level = "Strong"
# counting each character used in password
char_count = Counter(password)
# saving result into file using os
folder = "password_reports"
if not os.path.exists(folder):   # create folder if it doesn't exist
    os.mkdir(folder)
path = os.path.join(folder, "regex_report.txt")
file = open(path, "w")
file.write("Password Entered: " + password + "\n")
file.write("Character Count: " + str(char_count) + "\n")
file.write("Strength Score: " + str(score) + "%\n")
file.write("Strength Level: " + level + "\n")
file.close()
# printing output
print("Password:", password)
print("Character Count:", char_count)
print("Score:", score, "%")
print("Strength Level:", level)
