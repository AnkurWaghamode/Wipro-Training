import re

# STRONG PASSWORD VALIDATION
def validate_password(password):
    #Uses lookahead assertions (?=)
    pattern = r"^(/=.*[A-Z])(?=.*[a-z])(?=\*\d)(?=.*[@$!%*?&]).{8,}$"
    if re.match(pattern, password):
        print("Strong Password")
    else:
        print("Weak password")

validate_password("Ankur@123")
validate_password("ankur123")

# REGEX MODIFIERS DEMONSTRATION
def regex_modifiers_demo():
#re.IGNORECASE
    text1 = "Python is awesome"
    pattern1 = "python"

    match1 = re.search(pattern1, text1, re.IGNORECASE)
    print("matched text:",match1.group())

#re.MULTILINE
    text2 = """Python is easy 
    Java is powerful
    Python is popular"""

    pattern2 = r"^Python"

    matches2 = re.findall(pattern2, text2, re.MULTILINE)
    print("Matched lines:",matches2)

#re.DOTALL
    text3 = "Hello\nWorld"
    pattern3 = "Hello.World"

    match3 = re.search(pattern3, text3, re.DOTALL)
    print("DOTALL match:",match3.group())

regex_modifiers_demo()
