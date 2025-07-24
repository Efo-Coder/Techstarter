# This is a simple Python program that prints a greeting message.

def greet(name):
    """Function to greet a person by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))