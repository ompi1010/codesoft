#****TASK 03****
#****PASSWORD-GENRATOR****
import random
import string

# Function to generate a unique password
def generate_unique_password(length, complexity, generated_passwords):
    while True:
        password = generate_password(length, complexity)
        if password not in generated_passwords:
            generated_passwords.append(password)
            return password

# Function to generate a password with the specified length and complexity
def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Unique Password Generator")
    generated_passwords = []

    while True:
        length = int(input("Enter the desired length of the password: "))
        complexity = input("Enter the complexity level (low/medium/high): ").lower()

        password = generate_unique_password(length, complexity, generated_passwords)

        print("Generated Password:", password)

        another = input("Generate another password? (yes/no): ").lower()
        if another != "yes":
            break

if __name__ == "__main__":
    main()
