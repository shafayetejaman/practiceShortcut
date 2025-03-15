# Problem 12: Create a New Line Above
# Task: Insert a new line above the `return` statement and add a print statement:
#       print("Adding two numbers")
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
#       or use `ea` and for vim motions.
def calculate_total(price, discount, tax):
    return price - discount + tax


# Problem 17: Code action
# Task: Ask ai what is the output
# Hint: Hover over `total` with your mouse or place the cursor on it and press `Alt+;`
#       to view and apply the quick fix.
print(settings)  # type: ignore


# Problem 18: Surround with Quotes
# Task: Wrap the variable `greeting` with double quotes.
# Hint: Select `Hello`, press `ysiw"` or yss" for hole line
def assign(Hello: str) -> None:
    greeting = Hello


# Problem 32: Convert the sorted functin to and array
# Task: arr = [sorted([3, 1, 2])]
# Hint: yss[
sorted([3, 1, 2])
len("test")
sum([1, 2, 3])

# Problem 19: Duplicate and Modify and delete the first
# Task: Duplicate the last `print` statement and change the number to `42`.
# Hint: Place the cursor on the line, then press `Shift + Alt + Down Arrow` to duplicate.
#       Edit the duplicated line using `<lideer>a` to increment and `<lideer>x` to decrement the number
#        and delete the line using `dd` 

print(10)
print(20)
print(30)


# Problem 20: Replace Specific Words
# Task: Replace all occurrences of `False` with `None`.
# Hint: Press `Ctrl + H` to open Find and Replace. Type `False` in the "Find" field
#       and `None` in the "Replace" field. Use `Alt + Enter` to replace all occurrences.
settings = {"dark_mode": False, "notifications": False, "auto_save": False}


# Problem 21: Replace "" with ''
# Task: Replace all occurrences of "<word>" with '<word>'  
# Hint: Press `cs"'` 
settings = {"dark_mode": False, "notifications": False, "auto_save": False}


# Problem 23: Collapse and Expand Code
# Task: Collapse the `hello_world` function and then expand it.
# Hint: Click the `-` icon next to the function or press `za` to toggle collaps and `zM` 
#       to collapse all code. Press `zR` to expand all.


def hello_world():
    print("Hello, World!")


def add(a, b):
    return a + b


# Problem 25: Navigate Between Open Tabs
# Task: Switch to the next tab in your open files.
# Hint: Use `Ctrl + Tab` to cycle through open tabs or `Ctrl + < / >` to go backward and forword.
# No code required for this task.

# Problem 25: Navigate Between files
# Task: Switch to another files.
# Hint: Use `Ctrl + P` to open or go to file.
# No code required for this task.


# Problem 26: Goto next reference
# Task: Switch to the next reference or previous reference position
# Hint: Use '*'


class NewUser:
    def __init__(self, name) -> None:
        self.name = name


user = NewUser("akash")
print(user.name)
user.name = "shafayet"
print(user.name)

# Problem 27: indent farther
# Task: Switch to the next reference or previous reference position
# Hint: Use `>>` or `<<` indent line or use `V` to select muliline then `>` or `<` to indent multiline.


class NewUser2:
    def __init__(self, name) -> None:
        self.name = name


# Problem 31: Split Editor and Compare
# Task: Practice viewing two parts of the file simultaneously
# Hint: Ctrl+\ to open split editor then Alt+\ to toggle between them


def part_one():
    print("This is in the top part")


def part_two():
    print("This is in the bottom part")



# Problem 33: Extract Variable Refactoring
# Task: Extract the calculation into a variable
# Hint: Select expression, Alt+;, select "Extract Variable"
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
