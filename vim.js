// 📝 1. Move to the beginning of the User class definition using a motion.
class User {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
}

// 📝 2. Jump to the factorial function using search (`/factorial`).
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// 📝 3. Move to the next occurrence of return (`/return`).
// 📝 4. Jump to the last curly brace of the factorial function (`}` motion).
function sum(a, b) {
    return a + b;
}

// 📝 5. Move forward by one word (`w`) inside the console.log statements.
console.log("This is a test message.");
console.log("Another log statement.");

// 📝 6. Jump to the fetchData function using `{` and `}` paragraph motions.
async function fetchData(url) {
    try {
        let response = await fetch(url);
        let data = await response.json();
            console.log("Fetched Data:", data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// 📝 7. Use `fx` to jump to specific characters inside a line.
// Example: Jump to the first occurrence of `:` in the following line.
const user = { name: "Alice", ages : 20, city: "New York" };

// 📝 8. Move to the array declaration using `/numbers`.
const numbers = [1, 2, 3, 4, 5, 5,7];

// 📝 9. Move to the `.map()` function call using search (`/map`).
const doubledNumbers = numbers.map(num => num * 2);

// 📝 10. Jump back to the last edit location (`gi`) after making a change.
console.log();


// 📝 11. Use `}` to jump to the next function definition.
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// 📝 12. Search for `return` using `/return` and jump between them with `n`.
function add(a, b) {
    return a + b;
}

// 📝 13. Use `%` to jump between the `{}` inside the loop.
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// 📝 14. Use `[[` and `]]` to jump between function blocks.
async function fetchData(url) {
    try {
        let response = await fetch(url);
        let data = await response.json();
        console.log("Data:", data);
    } catch (error) {
        console.error("Error:", error);
    }
}

// 📝 15. Set a mark with `ma` inside the function and jump back with `'a`.
const num = [1, 2, 3, 4, 5];
const doubled = num.map(num => num * 2);
console.log(doubled);

// 📝 16. Use `ge` to move to the last letter of each word in the string.
const message = "Hello, Vim is powerful!";
