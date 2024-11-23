Password Generator

A Python-based password generator that allows you to create secure, customizable passwords by specifying the desired length and the inclusion of different character types.
Features

    Choose the length of your password.
    Include any combination of:
        Uppercase letters
        Lowercase letters
        Special characters
        Numbers
    Generates secure passwords using Python's secrets module for randomness.

Requirements

    Python 3.6 or higher

Usage

    Clone or download the repository:

git clone https://github.com/your-username/password-generator.git
cd password-generator

Run the script:

    python password_generator.py

    Follow the prompts:
        Indicate whether to include uppercase, lowercase, special characters, or numbers by typing yes or no.
        Specify the desired length of the password.

    The generated password will be displayed in the terminal.

Example

Include CAPITAL? (yes/no) yes
Include LOWERCASE? (yes/no) yes
Include SPECIAL CHAR? (yes/no) no
Include NUMBERS? (yes/no) yes
How many digits do you want your password to be?

10
Your generated password: A3b7D2c8E1

Notes

    If no options are selected (all inputs are no), the script will generate an empty password.
    The password length must be specified; the script will prompt until a valid length is provided.

License

This project is licensed under the MIT License.
