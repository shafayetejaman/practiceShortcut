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


# Problem 6: Split and Merge Lines
# Task: Split the first line into multiple lines for better readability.

user = {"name": "John", "age": 30, "is_admin": True}

# Hint: Use `alt + right` to inset `,` then `alt + shift + f` to formate.


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

# Hint: Use `Ctrl + o`  to open the file navigator, then type `@multiply`.


# Problem 10: Replace All Instances
# Task: Replace all occurrences of the word `color` with `colour`.

settings = {"background_color": "white", "text_color": "black"}

# Hint: Use `Ctrl + H` and `shift + enter/enter` to replace all.

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

# Problem 13 go to each lines and go to last cursor position
# Task: go to all the occurrence of the word then reverse travel just after that.

font = "arial"
font = "new roman"
font = "roboto"
font = "nard font"

# Hint: Use  `Cmd + U ` to go to the last cursor possition.


# Problem 14 remove the text from the ""
# Task: Use shortcut to go the end of the line and remove evry thing iside the "".

font = "arial"
font = "newroman"
font = "roboto"
font = "nardfont"

# Hint: Use `Ctrl + Shift + =` to select the block and  `Shift + Alt + i ` to make cursor at the end.


# Problem 15 open terminal
# Task: Use shortcut to quickly open the terminal both in workspace and integrated modes.

# Hint: Use `Ctrl + ~` to sopen in workpace then and  `Shift + Alt + enter ` to open in integrated mode.


# Problem 16 close a tab
# Task: Use shortcut to close a opened tab.

# Hint: Use `Ctrl + w` to close the opend tab.


# Problem 17 reopen a closed tab
# Task: Use shortcut to quickly reopen last closed tab.

# Hint: Use `Ctrl + shift + t` to reopen the tab.
