import secrets
import string

# Choosing what user wants in password
# variables for user choice
opt_cap = input('Include CAPITAL? (yes/no) ') == 'yes'
opt_low = input('Include LOWERCASE? (yes/no) ') == 'yes'
opt_spec = input('Include SPECIAL CHAR? (yes/no) ') == 'yes'
opt_num = input('Include NUMBERS? (yes/no) ') == 'yes'

# Ask user for password length
print("How many digits do you want your password to be?\n")

length = input('')

# Make sure they fill in the blank
while length == "":
    print("How many digits do you want your password to be?\n")
    length = input()

password_list = []

# Generating random characters
length = int(length)
for i in range(length):
    cap = ''
    low = ''
    spec = ''
    num = ''

    # Choose which var to apply
    if opt_cap:
        cap = secrets.choice(string.ascii_uppercase)
    if opt_low:
        low = secrets.choice(string.ascii_lowercase)
    if opt_spec:
        spec = secrets.choice(string.punctuation)
    if opt_num:
        num = secrets.choice(string.digits)

    if cap: password_list.append(cap)
    if low: password_list.append(low)
    if spec: password_list.append(spec)
    if num: password_list.append(num)

# Ensure the password is exactly the desired length
password_final = ''.join(password_list[:length])

print(password_final, end='')