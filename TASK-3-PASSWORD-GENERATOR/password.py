# Importing necessary modules:
import random
import string

# This function helps in deciding whether user want NUMERAL DIGITS in their password: If yes, then How many;
def number_decision():
    numbers=input("\nDo you want NUMERAL DIGITS in you password, Enter [yes/no]: ")
    numbers.lower()
    if numbers=='yes':
        num_len=int(input("How many numeral digits you want in you password: "))
        return num_len
    else:
        return 0
# This function helps in deciding whether user want SPECIAL CHARACTERS in their password: If yes, then How many;
def special_Char_decision():
    special_Char=input("\nDo you want SPECIAL CHARACTERS in you password, Enter [yes/no]: ")
    special_Char.lower()
    if special_Char=='yes':
        special_Char_len=int(input("How many special characters you want in you password: "))
        return special_Char_len
    else:
        return 0

# Intro Line:
print("\nHello...!\nWelcome to Password Generator\nCreated by: Aaryan Kumar\nTry me out if you need help generating password...!\n")

decision=input("\nDo you want to generate password, Enter [yes/no]: ")
decision.lower()
while decision=='yes':
    # Getting the full password length needed by the user
    full_pass_len=int(input("Enter length of password you want: "))

    print("\nA bit more information please...!")

    # Using functions to decide whether user wants numbers and special characters in password.
    num_len = number_decision()
    special_Char_len = special_Char_decision()

    pass_non_letters=num_len+special_Char_len
    # Making rough group of characters for password separately for letters, numbers, special characters as entered in input by user.
    pass_letter=''.join(random.choice(string.ascii_letters) for _ in range(full_pass_len - pass_non_letters))
    pass_num=''.join(random.choice(str(string.digits)) for _ in range(num_len))
    pass_special_Char=''.join(random.choice(str(string.punctuation)) for _ in range(special_Char_len))

    # Joining all characters first to make unshuffled final string list:
    pre_final_pass = list(pass_letter + pass_num + pass_special_Char)
    # To shuffle the password characters:
    random.shuffle(pre_final_pass)
    # Storing the final password:
    final_pass = ''.join(pre_final_pass)

    # Printing Result:
    print('\n\nThis is your password: ',final_pass)
    print("\nLength: ", len(final_pass))
    decision=input("\nDo you want to generate password again: ")
else:
    print("\nNo issue...!\nSee you next time...!")