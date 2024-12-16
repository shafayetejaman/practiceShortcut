# Problem 1: Duplicate and Edit a Line
# Task: Duplicate the line with the shortcut and change the function name from `greet_user` to `greet_admin`.


def greet_user(name):
    return f"Hello, {name}!"


# Hint: Use `Shift + Alt + Down Arrow` (Windows/Linux) or `Shift + Option + Down Arrow` (Mac) to duplicate the line.


# Problem 2: Move a Line
# Task: Move the last print statement to the top of the file.

print("This is a test")
print("Hello, World!")
print("End of Program")

# Hint: Use `Alt + Up Arrow` (Windows/Linux) or `Option + Up Arrow` (Mac) to move lines.


# Problem 3: Select and Comment
# Task: Comment out the `add` function using the shortcut.


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# Hint: Use `Ctrl + /` (Windows/Linux) or `Cmd + /` (Mac) to toggle comments.


# Problem 4: Multi-Cursor Editing
# Task: Change all variable names `temp` to `temperature` simultaneously.

temp = 25
if temp > 30:
    print("It's hot!")
else:
    print("It's cool!")

# Hint: Use `Ctrl + D` (Windows/Linux) or `Cmd + D` (Mac) to select the next occurrence.


# Problem 5: Format Document
# Task: Format the following messy code snippet.


def sum(a, b):
    return a + b


# Hint: Use `Shift + Alt + F` (Windows/Linux) or `Shift + Option + F` (Mac) to format the code.


# Problem 6: Split and Merge Lines
# Task: Split the first line into multiple lines for better readability.

user = {"name": "John", "age": 30, "is_admin": True}

# Hint: Use `Ctrl + Enter` (Windows/Linux) or `Cmd + Enter` (Mac) to insert a new line below.


# Problem 7: Rename a Function
# Task: Change the function name `print_message` to `display_message` everywhere in the file.


def print_message(message):
    print(message)


print_message("Hello!")

# Hint: Use `F2` to rename symbols globally.


# Problem 8: Navigate to a Specific Symbol
# Task: Quickly navigate to the `multiply` function definition.


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print(add(2, 3))

# Hint: Use `Ctrl + P` (Windows/Linux) or `Cmd + P` (Mac) to open the file navigator, then type `@multiply`.


# Problem 9: Open Integrated Terminal
# Task: Open the terminal, run the following code, and execute the file.

# Save this file as script.py
print("Code Editing Practice!")

# Hint: Use `` Ctrl + ` `` to open the terminal, then run the command `python script.py`.


# Problem 10: Replace All Instances
# Task: Replace all occurrences of the word `color` with `colour`.

settings = {"background_color": "white", "text_color": "black"}

# Hint: Use `Ctrl + H` (Windows/Linux) or `Cmd + Shift + H` (Mac) to replace all.
