#Prints welcome statement
print("Welcome to Python help!\n\n")

###Functions ----------------------------
def scanTable(table, boolean, search):
    for i in range(len(table)):
        boolean = search.lower() == table[i]
        
        if boolean:
            return True
    return False 

###Tables/Lists -------------------------
#Yes/no answers
validAnswers = ["yes", "yeah", "yea", "ye", "yep"]

#print()
printList = [
    "print",
    "prin",
    "print function",
    "print()",
    "print() function",
    "1",
    "1.",
    "one"
]
printB = None
printString = "print()"
printDef = "The print() function takes an input of\n\tany data-type and displays it in the test\n\twindow."

#Functions
funcList = [
    "func",
    "functions",
    "function",
    "def",
    "define",
    "2",
    "2.",
    "two"
]
funcB = None
funcString = "Functions"
funcDef = "Functions are a great way to shorten\n\tprograms and make code more efficient. To\n\tdeclare a function, use this format:\n\n\tdef yourFunctionName():\n\t\t#your code goes here\n\t\t#every time a function is called,\n\t\t the code inside it will execute"

#Loops
loopList = [
    "loops",
    "loop",
    "for loops",
    "for loop",
    "while loop",
    "while loops",
    "for-loops",
    "for-loop",
    "while-loop",
    "while-loops",
    "3",
    "3.",
    "three"
]
loopB = None
loopString = "Loops"
loopDef = "Loops are how iteration is added to an\n\talgorithm. There are two main types of\n\tloops: for loops and while loops. For loops\n\trepeat code for a fixed amount and are good\n\tat iterating through tables. They are\n\twritten like this when \"n\" is the number of\n\titerations:\n\n\t\tfor i in range(n):\n\t\t\t#code goes here\n\t\t\t#the code will execute \"n\"\n\t\t\t times\n\n\tWhile loops are meant to have code run over\n\tand over until a condition is not met\n\tanymore. This is how while loops are\n\twritten:\n\n\t\twhile (condition):\n\t\t\t#code goes here\n\t\t\t#once a condition is False,\n\t\t\t the loop will automatically\n\t\t\t stop"

#Math
mathList = [
    "math",
    "mathematics",
    "maths",
    "math in python",
    "add",
    "addition",
    "sub",
    "subtract",
    "subtraction",
    "mult",
    "multiplication",
    "multiply",
    "div",
    "divide",
    "division",
    "mod",
    "modulus",
    "remainder",
    "sum",
    "quotient",
    "exponenents",
    "powers",
    "difference",
    "square root",
    "product",
    "order of operations",
    "arithmetic",
    "4",
    "4.",
    "four"
]
mathB = None
mathString = "Math in Python"
mathDef = "Use of mathematical knowledge is crucial to\n\tcoding in any language, not just Python.\n\tHowever, there is a specific syntax that\n\tis used when writing in Python. Here are the\n\tsigns for all the mathematical operations:\n\n\t\tAddition: sum = x + y\n\n\t\tSubraction: difference = x - y\n\n\t\tMultiplication: product = x * y\n\n\t\tDivsion: x / y\n\n\t\tInteger Division: x // y (this\n\t\t divides x by y but it ignores the\n\t\t decimal)\n\n\t\tExponentiation: x ** y\n\n\t\tModulus (Mod): x % y (returns the\n\t\t remainder of x / y)\n\n\tThe order of operations is also slightly\n\tdifferent than the one used in natural\n\tlanguages (1 = highest priority and 4 =\n\tlowest):\n\n\t1.\tParenthesis (())\n\n\t2.\tExponents (**)\n\n\t3.\tMultiplication (*),\n\t\tDivision (/),\n\t\tInt Division (//),\n\t\tMod (%)\n\n\t4.\tAddition (+),\n\t\tSubtraction (-)"

#If-statements
ifList = [
    "if",
    "if:",
    "if statement",
    "if statements",
    "if-statement",
    "if-statements",
    "if else",
    "if-else",
    "if else statement",
    "if else statements",
    "if-else statement",
    "if-esle statements",
    "else",
    "else:",
    "elif",
    "elif:",
    "else if",
    "elseif",
    "if-elif-else",
    "elif-else",
    "if elif else",
    "if elif",
    "elif statements",
    "elif-statements",
    "elif:"
    "selection",
    "select",
    "option",
    "options",
    "5",
    "5.",
    "five"
]
ifB = None
ifString = "If statements"
ifDef = "If-statements allow a program to have\n\toptions. To write an if-statement, on must\n\twrite the keyword \"if\", the condition, and\n\twhat happens when a condition is met or not.\n\tThis is the format:\n\n\t\tif condition:\n\t\t\t#code goes here\n\t\t\t#if condition is not met,\n\t\t\t code will not execute\n\n\tThere is also a way to provide an\n\talternative code in case the condition is\n\tnot met. This is called the if-else\n\tstatement, and it is written like this:\n\n\t\tif condition:\n\t\t\t#code goes here\n\n\t\telse:\n\t\t\t#alternative code goes here\n\n\tThe last way to write an if-statement is to\n\tuse elif, which provides the code for a\n\tsecondary condtion in the event that it is\n\tmet. This is how if-elif-else/if-elif\n\tstatements are written:\n\n\t\tif condition:\n\t\t\t#code goes here\n\n\t\telif secondaryCondition:\n\t\t\t#secondary code goes here\n\n\t\telse:\n\t\t\t#alternative code goes here\n\t\t\t#this will only execute if\n\t\t\t none of the conditions are\n\t\t\t met"

#Table of Contents
TOC = [
    "1. print()",
    "2. Functions",
    "3. Loops",
    "4. Math in Python",
    "5. If-statements"
]

#List of topics (listed in TOC)
topics = [
    
    #print()
    {
        "table" : printList,
        "boolean" : printB,
        "term" : printString,
        "definition" : printDef
    },
    
    #Functions
    {
        "table" : funcList,
        "boolean" : funcB,
        "term" : funcString,
        "definition" : funcDef
    },
    
    #Loops
    {
        "table" : loopList,
        "boolean" : loopB,
        "term" : loopString,
        "definition" : loopDef
    },
    
    #Math
    {
        "table" : mathList,
        "boolean" : mathB,
        "term" : mathString,
        "definition" : mathDef
    },
    
    #If-statements
    {
        "table" : ifList,
        "boolean" : ifB,
        "term" : ifString,
        "definition" : ifDef
    }
]

###Non-reseting variables ---------------
rep = 0

###Search algorithm ---------------------
while True:
    if rep == 0:
        answer = input("Would you like to search for a python term? yes/no: ")
    else:
        answer = input("Would you like to search for another term? yes/no: ")
    
    answerBool = answer.lower() in validAnswers
    
    #Ends program if user selects "no"
    if answerBool == False:
        print("\nThank you for using Python help!")
        break
    
    print()
    searchItem = input("Search here to learn more about it: ")
    print()
    
    found = False

    #Scans all tables for a valid input
    for topic in topics:
        if scanTable(topic["table"], topic["boolean"], searchItem):
            found = True
            print(topic["term"] + ":\n\t" + topic["definition"] + "\n")
            rep += 1

    
    if found == False:
        print("Oops! Couldn't find \"" + searchItem + "\".\n")
        TOCInput = input("Would you like to see the table of contents? yes/no: ")
        TOCInputBool = TOCInput.lower() in validAnswers
        
        if TOCInputBool:
            print()
            
            for i in range(len(TOC)):
                print(TOC[i])
            
            print()
            TOCSearch = input("Enter the index number of the topic: ")
            
            for topic in topics:
                if scanTable(topic["table"], topic["boolean"], TOCSearch):
                    found = True
                    print(topic["term"] + ":\n\t" + topic["definition"] + "\n")
                    rep += 1
                    
        else:
            print("\nThank you for using Python help!")
            break
