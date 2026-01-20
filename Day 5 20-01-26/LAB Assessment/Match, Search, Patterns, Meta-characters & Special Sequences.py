import re

#Uses re.match() to check whether a string starts with a valid employee ID in the format EMP followed by 3 digits
emp_id = "EMP123"

pattern_emp = r"^(EMP\d{3})"

match_emp = re.match(pattern_emp,emp_id)

if match_emp:
    print("Valid Employee ID found",match_emp.group())

else:
    print("Invalid Employee ID")

print("-" * 50)

#Uses re.search() to find the first occurrence of a valid email address in a given text
text = "Please contact us at support@gmail.com for assistance"

email_pattern = r"([\w.-]+@[\w\.-]+\.\w+)"

search_email = re.search(email_pattern,text)

if search_email:
    print("Email found:",search_email.group())
else:
    print("No email found")

print("-" * 50)

#Demonstrates the use of meta-characters (., *, +, ?)
# and special sequences (\d, \w, \s) in the patterns

sample_text = "User1 has 3 files."

pattern_meta = r"(\w+)\s(\w+)\s(\d+)\s(\w+)\."
# \w+  → word characters (letters, digits, _)
# \s   → space
# \d+  → digits
# .    → any character (here literal dot)
match_meta = re.search(pattern_meta, sample_text)

if match_meta:
    print("Meta-characters pattern matched!")
else:
    print("No match")

print("-" * 50)

#Prints matched groups using capturing parentheses
if match_meta:
    print("Captured Groups")
    print("Group1:",match_meta.group(1))
    print("Group2:", match_meta.group(2))
    print("Group3:", match_meta.group(3))
    print("Group4:", match_meta.group(4))

