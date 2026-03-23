# Password Checker

A simple Python CLI project that checks whether a password meets basic strength requirements.

## What this project does
This program asks the user to enter a password and then checks whether it:
- is between 8 and 16 characters long
- contains at least one uppercase letter
- contains at least one lowercase letter
- contains at least one digit
- contains at least one special character

It gives the password a score out of 5 based on how many conditions are passed.
A password is accepted only if it scores **5/5**.

## Concepts used
This project practices:
- functions
- conditionals
- strings
- loops through characters
- boolean return values
- basic program structure

## File
- `main.py` — main password checker script

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```

## Example
```text
Enter a password: Hello123
Password is invalid. Score: 4
Password must contain at least one special character.
```

## Rules used
The program checks:
1. Length must be between 8 and 16 characters
2. Must contain at least one uppercase letter
3. Must contain at least one lowercase letter
4. Must contain at least one digit
5. Must contain at least one special character

## Current behavior note
If the password is invalid, the program currently calls `main()` again to ask for another password.
This means it is using a recursive retry approach.

That works for learning and small runs, but later it would be better to replace it with a loop.

## Possible future improvements
- show score as `x/5`
- classify password as weak / medium / strong
- replace recursive retry with a loop
- hide password input using `getpass`
- make special characters configurable

## Why I built this
This is a Month 1 Python practice project for improving problem-solving, function design, and basic CLI program structure.
