// Problem 1: Move Line Up
// Task: Move the `const name` declaration above the `console.log` statement.
// Hint: Use `Alt + Up Arrow`.
const age = 25;
console.log(name);
const name = "Shafayet";

// Problem 2: Delete a Line
// Task: Remove the line with `const unusedVar = 42;`.
// Hint: Use `dd` in Vim or `Ctrl + Shift + K` in VS Code.
const unusedVar = 42;
const activeVar = "Hello";

// Problem 3: Duplicate Line
// Task: Duplicate the `console.log(message);` line.
// Hint: Use `Shift + Alt + Down Arrow`.
const message = "Welcome to Vim!";
console.log(message);

// Problem 4: Wrap with Parentheses
// Task: Wrap `number * 2` with parentheses.
// Hint: Use `ysiw(` in Vim.
const double = number * 2;

// Problem 5: Change Word
// Task: Replace `red` with `blue`.
// Hint: Place the cursor on `red` and press `cw`, then type `blue`.
const color = "red";

// Problem 6: Select Multiple Occurrences
// Task: Select all instances of `let` and replace them with `const`.
// Hint: Use `Ctrl + D` multiple times in VS Code or `*` in Vim.
let a = 10;
let b = 20;
let c = 30;

// Problem 7: Extract Function
// Task: Extract the calculation into a function.
// Hint: Select the expression and use `Alt + ;`, then choose "Extract Function".
const price = 100 * 1.2 + (100 * 1.2 * 0.15);

// Problem 8: Swap Variables
// Task: Swap the values of `x` and `y`.
// Hint: Use `xp` in Vim or manually swap the lines.
let x = 5;
let y = 10;

// Problem 9: Navigate Between Matching Brackets
// Task: Move between `{}` brackets.
// Hint: Use `%` in Vim.
function example() {
    if (true) {
        console.log("Inside block");
    }
}

// Problem 10: Convert String to Template Literal
// Task: Convert the string concatenation to a template literal.
// Hint: Select the string and use `Ctrl + Shift + P` → "Convert to Template String".
console.log("Hello, " + name + "!");

// Problem 11: Toggle Line Comment
// Task: Comment out the `console.log` statement.
// Hint: Use `Ctrl + /` in VS Code or `gcc` in Vim.
console.log("This line should be commented");
