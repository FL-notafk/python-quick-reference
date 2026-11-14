# Python Quick Reference/Help

An interactive glossary of 5 Python concepts used in almost every script.

## Topics Covered
* **`print()`**: Basic console output
* **Functions**: Defining reusable blocks of code
* **Loops**: Iteration using `for` and `while` loops
* **Math in Python**: Arithmetic operators (`+`, `-`, `*`, `/`, `//`, `**`, `%`)
* **If-Statements**: Conditional logic with `if`, `elif`, and `else`

## Features
* **Flexible Keyword Search**: Recognizes topic names and related terms (like `functions` and `def`)
* **Built-in Table of Contents**: Offers the list of topics covered if search word isn't recognized

## Prerequisites
* Python 3 installed on device
* No external dependencies (uses Python Standard Library only)

## How to Run

1. **Download the code:**
   * **Option A (Git):** Clone the repository to your computer:
     ```bash
     git clone https://github.com/FL-notafk/python-quick-reference.git
     cd python-quick-reference
     ```
   * **Option B (Direct Download):** Click the green **Code** button at the top of this page, select **Download ZIP**, and extract the folder.

2. **Run the script:**
   Open your terminal or command prompt inside the project folder and run:
   ```bash
   python python-qr.py
   ```
   *(Note: Depending on your system, you may need to use `python3 python-qr.py`.)*

## Example Usage
```text
Welcome to Python help!


Would you like to search for a python term? yes/no: yes

Search here to learn more about it: print()

print():
	The print() function takes an input of
	any data-type and displays it in the test
	window.

Would you like to search for another term? yes/no: yes

Search here to learn more about it: variables

Oops! Couldn't find "variables".

Would you like to see the table of contents? yes/no: yes

1. print()
2. Functions
3. Loops
4. Math in Python
5. If-statements

Enter the index number of the topic: 2
Functions:
	Functions are a great way to shorten
	programs and make code more efficient. To
	declare a function, use this format:

	def yourFunctionName():
		#your code goes here
		#every time a function is called,
		 the code inside it will execute

Would you like to search for another term? yes/no: no

Thank you for using Python help!
```

## License
* This project is licensed under the [MIT License](LICENSE)
