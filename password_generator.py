import random
import string

# Password Generator Class
class PasswordGenerator:
    def __init__(self, length=8, include_uppercase=True, include_digits=True, include_special=True):
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_digits = include_digits
        self.include_special = include_special

    def generate_password(self):
        # Define character sets
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase if self.include_uppercase else ''
        digits = string.digits if self.include_digits else ''
        special = string.punctuation if self.include_special else ''
        
        # Combine all selected character sets
        all_characters = lower + upper + digits + special
        
        if not all_characters:
            raise ValueError("No character types selected. Please enable at least one type of character.")
        
        # Randomly choose characters
        password = ''.join(random.choice(all_characters) for _ in range(self.length))
        return password


def create_password(length=8, uppercase=True, digits=True, special=True):
    password_generator = PasswordGenerator(length, uppercase, digits, special)
    return password_generator.generate_password()


if __name__ == "__main__":
    
    #MODIFY PARAMETERS
    password = create_password(length=12, uppercase=True, digits=True, special=True)
    print(f"Generated password: {password}")
