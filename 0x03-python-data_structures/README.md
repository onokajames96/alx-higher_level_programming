# Python - Data Structures: Lists, Tuples
#Resources
Read or watch:

3.1.3. Lists
Data structures (until 5.3. Tuples and Sequences included)
Learn to Program 6 : Lists
#Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What are lists and how to use them
What are the differences and similarities between strings and lists
What are the most common methods of lists and how to use them
How to use lists as stacks and queues
What are list comprehensions and how to use them
What are tuples and how to use them
When to use tuples versus lists
What is a sequence
What is tuple packing
What is sequence unpacking
What is the del statement and how to use it
#Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
#C
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
You are not allowed to use global variables
No more than 5 functions per file
In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
The prototypes of all your functions should be included in your header file called lists.h
Don’t forget to push your header file
All your header files should be include guarded
#Write a function that prints all integers of a list.

Prototype: def print_list_integer(my_list=[]):
#Write a function that retrieves an element from a list like in C.

Prototype: def element_at(my_list, idx):
#Write a function that replaces an element of a list at a specific position (like in C).

Prototype: def replace_in_list(my_list, idx, element):
#Write a function that prints all integers of a list, in reverse order.

Prototype: def print_reversed_list_integer(my_list=[]):
#Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

Prototype: def new_in_list(my_list, idx, element):
#Write a function that removes all characters c and C from a string.

Prototype: def no_c(my_string):
#Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):
#Write a function that adds 2 tuples.

Prototype: def add_tuple(tuple_a=(), tuple_b=()):
#Write a function that returns a tuple with the length of a string and its first character.

Prototype: def multiple_returns(sentence):
#Write a function that finds the biggest integer of a list.

Prototype: def max_integer(my_list=[]):
#Write a function that finds all multiples of 2 in a list.

Prototype: def divisible_by_2(my_list=[]):
#Write a function that deletes the item at a specific position in a list.

Prototype: def delete_at(my_list=[], idx=0):
#Complete the source code in order to switch value of a and b

You can find the source code here
Your code should be inserted where the comment is (line 4)
Your program should be exactly 5 lines long
#Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Write a function in C that checks if a singly linked list is a palindrome.

Prototype: int is_palindrome(listint_t **head);
Return: 0 if it is not a palindrome, 1 if it is a palindrome
An empty list is considered a palindrome
