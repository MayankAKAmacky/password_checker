
def check_password_length(password):
    return len(password) >= 8 and len(password) <= 16
    
def check_password_has_uppercase(password):
    return any(char.isupper() for char in password) 

def check_password_has_lowercase(password):
    return any(char.islower() for char in password)

def check_password_has_digit(password):
    return any(char.isdigit() for char in password)
    
def check_password_has_special_char(password):
    special_characters = "!@#$%^&*()_+-=[]{}|;':\",.<>/?"
    return any(char in special_characters for char in password)

def password_strength(password):
    score = 0
    if check_password_length(password):
        score += 1
    if check_password_has_uppercase(password):
        score += 1
    if check_password_has_lowercase(password):
        score += 1
    if check_password_has_digit(password):
        score += 1
    if check_password_has_special_char(password):
        score += 1
    return score

def main():
    password = input("Enter a password: ")
    score = password_strength(password)
    if score == 5:
        print("Password is valid.")
    else:
        print(f"Password is invalid. {score}/5 criteria met.")
        

        if not check_password_length(password):
            print("Password must be between 8 and 16 characters.")
        if not check_password_has_uppercase(password):
            print("Password must contain at least one uppercase letter.")
        if not check_password_has_lowercase(password):
            print("Password must contain at least one lowercase letter.")
        if not check_password_has_digit(password):
            print("Password must contain at least one digit.")
        if not check_password_has_special_char(password):
            print("Password must contain at least one special character.") 
        
        main()
        
        


if __name__ == "__main__":    
    main()