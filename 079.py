import string

def long_enough(pw):
    'Password must be at least 6 characters'
    return len(pw) >= 6

def short_enough(pw):
    'Password cannot be more than 12 characters'
    return len(pw) <= 12

def has_lowercase(pw):
    'Password must contain a lowercase letter'
    return len(set(string.ascii_lowercase).intersection(pw)) > 0

def has_uppercase(pw):
    'Password must contain an uppercase letter'
    return len(set(string.ascii_uppercase).intersection(pw)) > 0

def has_numeric(pw):
    'Password must contain a digit'
    return len(set(string.digits).intersection(pw)) > 0

def has_special(pw):
    'Password must contain a special character'
    return len(set(string.punctuation).intersection(pw)) > 0

def test_password(pw, tests=[long_enough, short_enough, has_lowercase, has_uppercase, has_numeric, has_special]):
    for test in tests:
        if not test(pw):
           # print(test.__doc__)
           print("The password must be 6 to 12 characters long, contain one uppercase letter, one lowercase letter, one digit and one special character")
        return False
    return True

def main():
    pw = input('Please enter a test password:')
    if test_password(pw):
        print('That is a good password!')

if __name__=="__main__":
    main()


# #COURSE ANSWER - Requires one upper, one lower, one digit, length of min 5
# while True:
#     psw = input("Enter new password: ")
#     if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
#         print("Password is fine")
#         break
#     else:
#         print("Password is not fine")