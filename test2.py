# Problem 11: Select and Delete
# Task: Delete the `hello_world` function and its docstring using shortcuts.
# Hint: Use `Ctrl + L` to select lines, or `Shift + Down Arrow` for manual selection.
#       Then press `Delete` or `Backspace` to remove the block.
def helloWorld():
    """
    This function prints 'Hello, World!'.
    """
    print("Hello, World!")


# Problem 12: Create a New Line Above
# Task: Insert a new line above the `return` statement and add a print statement:
#       print("Adding two numbers").
# Hint: Place the cursor on the line with `return` and press `Ctrl + Shift + Enter`
#       to insert a new line above. Type the new code.
def Add(a, b):
    return a + b


# Problem 13: Select a Block
# Task: Select the entire block of the `divide` function.
# Hint: Place the cursor inside the function and press `Ctrl + Shift + ]` to expand the selection.
def Divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Problem 14: Move Block of Code
# Task: Move the entire `divide` function to appear above the `add` function.
# Hint: Select the `divide` function, then use `Alt + Up Arrow` to move it up.
def addder(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Problem 15: Split One Line into Multiple Lines
# Task: Split the following dictionary into multiple lines for readability.
# Hint: Place the cursor where you want to split and press `Enter`. Repeat as needed.
settings = {"theme": "dark", "font_size": 12, "language": "en", "show_tutorial": True}


# Problem 16: Multi-Cursor on Multiple Lines
# Task: Add a default value `= 0` to all the function arguments.
# Hint: Place the cursor on the first parameter. Press `Alt + Click` on each argument
#       or use `Ctrl + Alt + Down Arrow` for multi-line editing.
def calculate_total(price, discount, tax):
    return price - discount + tax


# Problem 17: Quick Fix Suggestions
# Task: Use a quick fix to resolve the undefined variable `total` by creating a new variable.
# Hint: Hover over `total` with your mouse or place the cursor on it and press `Alt + /`
#       to view and apply the quick fix.
print(settings)


# Problem 18: Surround with Quotes
# Task: Wrap the variable `greeting` with double quotes.
# Hint: Select `Hello`, press `Shift + "`, or use `Ctrl + Shift + P`
#       to open the Command Palette and search for "Surround with Quotes".
def assign(Hello: str) -> None:
    greeting = Hello




# Problem 19: Duplicate and Modify
# Task: Duplicate the last `print` statement and change the number to `42`.
# Hint: Place the cursor on the line, then press `Shift + Alt + Down Arrow` to duplicate.
#       Edit the duplicated line as needed.
print(10)
print(20)
print(30)


# Problem 20: Replace Specific Words
# Task: Replace all occurrences of `False` with `None`.
# Hint: Press `Ctrl + H` to open Find and Replace. Type `False` in the "Find" field
#       and `None` in the "Replace" field. Use `Alt + Enter` to replace all occurrences.
settings = {"dark_mode": False, "notifications": False, "auto_save": False}


# Problem 21: Highlight Word Instances
# Task: Highlight all instances of the word `data` in the following snippet.
# Hint: Place the cursor on the word `data` and press `Ctrl + D` repeatedly
#       to select all instances.
data = [1, 2, 3]
for d in data:
    print(d)


# Problem 22: Extract Variable
# Task: Extract the `3.14` into a variable called `pi`.
# Hint: Select `3.14`, then press `Ctrl + .` and choose "Extract to variable".
def calculate_radius(radius: int) -> None:
    area = 3.14 * radius**2


# Problem 23: Collapse and Expand Code
# Task: Collapse the `hello_world` function and then expand it.
# Hint: Click the `-` icon next to the function or press `Ctrl + K, Ctrl + 0`
#       to collapse all code. Press `Ctrl + K, Ctrl + J` to expand all.
def hello_world():
    print("Hello, World!")


def add(a, b):
    return a + b


# Problem 24: Open Command Palette
# Task: Open the Command Palette and search for a command to convert indentation to spaces.
# Hint: Press `Ctrl + Shift + P` to open the Command Palette. Search for "Indentation: Convert to Spaces".
# Code with mixed tabs and spaces
def function():
    print("Hello")


# Problem 25: Navigate Between Open Tabs
# Task: Switch to the next tab in your open files.
# Hint: Use `Ctrl + Tab` to cycle through open tabs or `Ctrl + Shift + Tab` to go backward.
# No code required for this task.
