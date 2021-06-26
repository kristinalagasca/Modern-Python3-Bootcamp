<h1 align="center">
Data Types</h1>

### Objectives
* Understand how to assign and use variables
* Learn Python naming restrictions and conventions
* Learn and use some of the different data types in Python
* Learn why Python is a dynamically typed language
* Understand how to convert data types
* Learn the ins and outs of strings
* Build a program that gets user input
---

#### *Variable Assignment*

A variable in Python is similar to a variable in mathematics—it’s a named symbol that 
holds a value. They are always assigned with the variable name on the left and the 
value on the right of the equal sign.

Variables must be assigned before they can be used.

**Naming restrictions:** 
* Variables must start with a letter or underscore
* The rest of the variable must consist of letters, numbers, or underscores
* Names are case-sensitive

**Naming conventions:**

Most Python programmers prefer to use standard style conventions when naming things.
* Most variables should be snake case (underscores between words)
* Most variables should be lower case, with some exceptions:
* CAPITAL_SNAKE_CASE refers to constants (i.e. PI = 3.14)
* UpperCamelCase usually refers to a class
* Variables that start and end with two underscores, aka dunder (**d**ouble 
  **under**score) are supposed to be private or left alone

#### *Data Types*

In any assignment, the assigned value must always be a valid data type. Those data 
types include
* bool — or Boolean, True or False values
* int — integer (1, 2, 3)
* str — string, or a sequence of unicode characters
* list — an ordered sequence of values of other data types
* dict — or dictionary which contains a collection of keys: values

**What is Dynamic Typing?** Python is highly flexible about reassigning variables to 
different types.

    awesome = True
    awesome = “a dog”
    awesome = None
    awesome = 22 / 7 

Since the variables above can change types readily, this is dynamic typing.
Languages such as C++ are statically-typed because the variables are stuck with their 
originally assigned type.

More to read in this link here: 
https://hackernoon.com/i-finally-understand-static-vs-dynamic-typing-and-you-will-too-ad0c2bd0acc7

#### *The special value of None*
The keyword None is used to define a null value, or no value at all. 

#### *Declaring Strings*
String literals in Python can be declared with either single or double quotes. Either 
one is perfectly fine however, it is important to stick to the same convention 
throughout the same file.

In Python, there are also ‘escape characters’, which are ‘metacharacters’ that get 
interpreted by Python to do something special. 

Escape Sequence | Meaning | Notes
---|---|---
\\newline | Backslash and newline ignored | 
\\\ | Backslash(\) | 
\\' | Single quote (') | 
\\" | Double quote(") | 
\\a | ASCII Bell (BEL) | 
\\b | ASCII Backspace (BS) | 
\\f | ASCII Formfeed (FF) | 
\\n | ASCII Linefeed (LF) | 
\\r | ASCII Carriage Return (CR) | 
\\t | ASCII Horizontal Tab (TAB) | 
\\v | ASCII Vertical Tab (VT) | 
\\ooo | Character with octal value *ooo* | (1, 3)
\\xhh | Character with hex value *hh* | (2, 3)

The table above was found from the following link: 
https://docs.python.org/3/reference/lexical_analysis.html

String Concatenation — is combining multiple strings together. In Python, you can 
simply do this with the ‘+’ operator.

#### *Formatting Strings*
There are also several ways to format strings in Python to interpolate variables.

The new way in Python3.6+ is by using f-strings.

	i.e. 
	x = 10
    formatted = f”I\’ve told you {x} times already!”

#### *Converting Data Types*

In string interpolation, data types are implicitly converted into string form. You 
can also explicitly convert variables by using the name of the builtin type as a 
function.
