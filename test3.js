// Problem 2: Delete a Line
// Task: Remove the line with `const unusedVar = 42;`.
// Hint: Use `dd` in Vim or in VS Code.
const unusedVar = 42;
const activeVar = "Hello";


// Problem 4: Wrap with Parentheses
// Task: Wrap `number * 2` with parentheses.
// Hint: Use `vt;d` then p to paste in Vim.
const double = number * 2;

// Problem 5: Change Word
// Task: Replace `red` with `blue`.
// Hint: Place the cursor on `red` and press `ci"`, then type `blue`.
const color = "red";

// Problem 8: Swap Variables
// Task: Swap the values of `x` and `y`.
// Hint: Use `x$p` and `x_P` in Vim or manually swap the lines.
let x = 5;
let y = 10;
y = x

// Problem 9: Navigate Between Matching Brackets
// Task: Move between `{}` brackets.
// Hint: Use `[{` or `]}` in Vim.
function example()
{
    if (true)
    {
        console.log("Inside block");
    }
}

// Problem 10: Navigate Between Matching Brackets
// Task: Move between `{}` brackets of the functions.
// Hint: Use `[[` or `]]` in Vim.
function example2()
{
    if (true)
    {
        console.log("Inside block");
    }
}

// Problem 11: comment without selecting. 
// Task: comment out the inner block. 
// Hint: Use `gc3j` . 
function example3()
{
    if (true)
    {
        console.log("Inside block");
    }
}
