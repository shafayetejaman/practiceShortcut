# Problem 1: Duplicate and Edit a Line
# Task: Duplicate the line with the shortcut and change the function name from `greet_user` to `greet_admin`.


def greet_user(name):
    return f"Hellow, {name}!"


# Hint: Use `Shift + Alt + Down Arrow` to duplicate the line.


# Problem 2: Move a Line
# Task: Move the last print statement to the top of the file.

print("This is a test")
print("Hello, World!")
print("End of Program")

# Hint: Use `Alt + Up Arrow` to move lines.


# Problem 3: Select and Comment
# Task: Comment out the `Add` function using the shortcut.


def Add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# Hint: Use `Ctrl + /` to toggle comments.


# Problem 5: Multi-Cursor Editing all occurrence
# Task: Change all variable names `Temp` to `Temperature` simultaneously.

Temp = 25
if Temp > 30:
    print("It's hot!")
elif Temp > 40:
    print("It's very hot!")
elif Temp > 50:
    print("It's supper hot!")

# Hint: Use `Ctrl + Shift + L` to select the next occurrence.


# Problem 5: Format Document
# Task: Format the following messy code snippet.


def sum(a, b):
    return a + b


# Hint: Use `ctrl + s`  to save and format the code.


# Problem 6: Split and Merge Lines
# Task: Split the first line into multiple lines for better readability.

user = {"name": "John", "age": 30, "is_admin": True}

# Hint: Use `alt + right` to inset `,` then `ctrl + s` to formate.


# Problem 7: Rename a Function
# Task: Change the function name `print_message` to `display_message` everywhere in the file.


def print_message(message):
    print(message)


print_message("Hello!")


# Problem 8: Navigate to a Specific Symbol
# Task: Quickly navigate to the `multiply` function definition.


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print(add(2, 3))

# Hint: Use `Ctrl + P`  to open the file navigator, then type `@multiply`.


# Problem 10: Replace All Instances
# Task: Replace all occurrences of the word `color` with `colour`.

settings = {"background_color": "white", "text_color": "black"}

# Hint: Use `Ctrl + H` to replace all.

# Problem 11 Transform to upper case for All Instances
# Task: Uppercase all occurrences of the word `font` with `FONT`.

font = "arial"
font = "new roman"
font = "roboto"
font = "nard font"
font = "arial"
font = "new roman"
font = "roboto"
font = "nard font"


# Hint: Use  `Cmd + Alt + up/down` to replace all.

# Problem 12 edit the lines and go to last edit cursor position
# Task: Uppercase all occurrences of the word `font` with `FONT` then revrse it just after that.

font = "arial"
font = "new roman"
font = "roboto"
font = "nard font"

# Hint: Use  `Cmd + y ` to go to the last edit cursor possition.

# Problem 13 edit the lines and go to last cursor position
# Task: Uppercase all occurrences of the word `font` with `FONT` then revrse it just after that.

font = "arial"
font = "new roman"
font = "roboto"
font = "nard font"

# Hint: Use  `Cmd + U ` to go to the last cursor possition.


# Problem 14 remove the text from the ""
# Task: Use shortcut to go the end of the line and remove evry thing iside the "".

font = "arial"
font = "new roman"
font = "roboto"
font = "nard font"

# Hint: Use `Ctrl + Shift + =` to select the block and  `Shift + Alt + i ` to make cursor at the end.
