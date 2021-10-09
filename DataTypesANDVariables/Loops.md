<h1 align="center">
Looping in Python
</h1>

### Objectives
* Understand what loops are and how they are useful
* Learn what an “iterable object” is
* Use ***for*** and ***while*** loops to iterate over ranges and strings
* Learn how to control exiting a loop

#### *For Loops*
In Python, for loops are written like this:
```
for item in iterable_object:
	do something with item
```

An **iterable object** is some kind of collection of items, for instance: a list of 
numbers, a string of characters, a range, etc.

*Item* is a new variable that can be called whatever the user chooses. It references 
the current position of our **iterator** within the *iterable*. It will iterate over (run 
through) every item of the collection and then go away when it has visited all items.

*What is a range?* A range is an immutable sequence of numbers and is commonly used for 
looping through an iterable object a specific number of times, i.e.

```
for number in range(1, 8):
	print(number)
```

More to read on ranges here: 
https://docs.python.org/3/library/stdtypes.html#typesseq-range

Python ranges come in multiple forms:

* range(7) gives integers from 0 through 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  *Count starts at 0 
  and is exclusive*<br><br>
* range(1, 8) will give you integers from 1 to 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  *Two parameters 
  are (start, end)*<br><br>
* range(1, 10, 2) will give you odds from 1 to 10&nbsp;&nbsp;&nbsp;&nbsp;*Third param 
  indicates how many <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  steps to skip. Also,
  which way to <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  count, up + or down -*<br><br>
* range(7, 0, -1) will give you integers from 7 to 1
