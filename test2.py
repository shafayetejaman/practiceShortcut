# Problem 12: Create a New Line Above
# Task: Insert a new line above the `return` statement and add a print statement:
#       print("Adding two numbers").
# Hint: Place the cursor on the line with `return` and press `Ctrl + Shift + Enter`
#       to insert a new line above. Type the new code.


def Add(a, b):
    return a + b


# Problem 14: Move Block of Code
# Task: Move the entire `divide` function to appear above the `adder` function.
# Hint: Select the `divide` function, then use `Alt + Up Arrow` to move it up.


def adder(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Problem 16: Multi-Cursor on Multiple Lines
# Task: Add a default value `= 0` to all the function arguments.
# Hint: Place the cursor on the first parameter. Press `Alt + Click` on each argument
#       or use `Ctrl + Alt + Down Arrow` for multi-line editing.
def calculate_total(price, discount, tax):
    return price - discount + tax


# Problem 17: Refactor
# Task: Ask ai what is the ouput
# Hint: Hover over `total` with your mouse or place the cursor on it and press `Ctrl+Shift+R`
#       to view and apply the quick fix.
print(settings)  # type: ignore


# Problem 18: Surround with Quotes
# Task: Wrap the variable `greeting` with double quotes.
# Hint: Select `Hello`, press `Shift + "`, or use `Ctrl + Shift + P`
#       to open the Command Palette and search for "Surround with Quotes".
def assign(Hello: str) -> None:
    greeting = Hello


# Problem 19: Duplicate and Modify and delete the first
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


# Problem 23: Collapse and Expand Code
# Task: Collapse the `hello_world` function and then expand it.
# Hint: Click the `-` icon next to the function or press `Ctrl + K, Ctrl + 0`
#       to collapse all code. Press `Ctrl + K, Ctrl + J` to expand all.
def hello_world():
    print("Hello, World!")


def add(a, b):
    return a + b


# Problem 24: Goto previous cursor possion
# Task: Switch to the next cursor or previous cursor position
# Hint: Use "Alt+'[' \ ']'"
# No code required for this task.

# Problem 25: Navigate Between Open Tabs
# Task: Switch to the next tab in your open files.
# Hint: Use `Ctrl + Tab` to cycle through open tabs or `Ctrl + Shift + Tab` to go backward.
# No code required for this task.

# Problem 26: Goto next reference
# Task: Switch to the next reference or previous reference position
# Hint: Use 'Ctrl+m'


class NewUser:
    def __init__(self, name) -> None:
        self.name = name


user = NewUser("akash")
print(user.name)
user.name = "shafayet"
print(user.name)

# Problem 27: indent farther
# Task: Switch to the next reference or previous reference position
# Hint: Use "Ctrl+'[' \ ']'"


class NewUser2:
    def __init__(self, name) -> None:
        self.name = name


# Problem 28: add propertites to both class eatch line simultaniasly
# Task: Switch to the next reference or previous reference position
# Hint: Use "Ctrl+q"


class NewUser3:
    def __init__(self, name) -> None:
        self.name = name


class NewUser4:
    def __init__(self, name) -> None:
        self.name = name


# Problem 30: Multi-cursor Column Selection
# Task: Add type hints to all parameters simultaneously
# Hint: Use Alt+Shift+Click or Alt+Shift+drag
def process_user_data(name, age, email):
    return {"name": name, "age": age, "email": email}


# Problem 31: Split Editor and Compare
# Task: Practice viewing two parts of the file simultaneously
# Hint: Ctrl+\ to split editor, Alt+Shift+1 for single view
def part_one():
    print("This is in the top part")


def part_two():
    print("This is in the bottom part")


# Problem 32: Quick suggestion
# Task: replace function with another function
# Hint: Hover over function Ctrl+spacebar
sorted([3, 1, 2])
len("test")
sum([1, 2, 3])


# Problem 33: Extract Variable Refactoring
# Task: Extract the calculation into a variable
# Hint: Select expression, alt+/, select "Extract Variable"
def calculate_price():
    return 100 * 1.2 + (100 * 1.2 * 0.15)


# Problem 34: Toggle Line Comment
# Task: Comment/uncomment multiple lines at once
# Hint: Select lines and use Ctrl+/
def debug_section():
    x = 10
    y = 20
    z = 30
    print(x + y + z)
