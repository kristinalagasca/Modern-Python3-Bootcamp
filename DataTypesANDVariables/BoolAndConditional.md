<h1 align="center">
Boolean and Conditional Logic
</h1>

### Objectives
* Learn how to get user input in Python
* Learn about “Truthiness”
* Learn how to use comparison operators to make a basic program
    * How do we make decisions in our programs using comparison operators and boolean 
      logic?
---

#### *User Input*
There is a built-in function within Python called ‘input’ that will prompt the user 
and store the result to a variable. 
```
# prompts the user to input name
i.e. name = input(“Enter your name here: “)
```

#### *Boolean Expressions*
**Conditional Statements** — are conditional logic using *if* statements to represent 
different paths a program can take based on some type of comparison input.

This pseudocode was written to represent a conditional statement:
```
if CONDITION_1 is True:
	do something
elif CONDITION_2 is True:
	do something
else:
	do something
```

#### *Truthiness*

In Python, all conditional checks resolve to **True** or **False**.

We can call values that resolve to True “truthy”, or values that resolve to False 
“falsey”.

Besides False conditional checks, other things that are naturally falsey include: 
empty objects, empty strings, *None*, and zero.

Operation | What is does | Example
--- | --- | ---
== | Truthy if **a** has the exact same value as **b** | a **==** b
!= | Truthy if **a** does NOT have the same value as **b** | a **!=** b
\> | Truthy if **a** is greater than **b** | a **>** b
\< | Truthy if **a** is lesser than **b** | a **<** b
\>= | Truthy if **a** is greater than or equal to **b** | a **>=** b
\<= | Truthy if **a** is lesser than or equal to **b** | a **<=** b

#### *Logical Operators*
In Python, the following operators can be used to make Boolean logical comparisons 
or statements:

Operation | What is does | Example
--- | --- | ---
and | Truthy if both **a** AND **b** are true (logical conjunction) | if a **and** b: <br> print (c)
or | Truthy if either **a** OR **b** are true (logical disjunction) | if a **or** b: <br> print(c)
not | Truthy if opposite of **a** is true (logical negation) | if **not** a: <br> print(b)


#### *is vs ==*
“It depends upon what the meaning of the word ‘is’ is.” - Bill Clinton

In Python, both is and == are very similar comparators; however, they are not the same.

    a = [1, 2, 3]
    b = [1, 2, 3]
    a == b		# returns True (checks if values are the same)
    a is b		# returns False (checks if stored in the same 
                    place in memory)
