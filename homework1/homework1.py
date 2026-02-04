# File: homework1. py

# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a in an integer

b = 1.5
print(b)
print(type(b)) # b is a float

c = 3j
print(c)
print(type(c)) # c is complex, which represents a number with both real and imaginary parts 'a + bj'

d = "hello"
print(d)
print(type(d)) # d is a string

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary

g = (1,2)
print(g)
print(type(g)) # g is a tuple, which unlike lists, are immutable

h = ["apple", " banana", "strawberry"]
print(h)
print(type(h)) # h is a list

i = True
print(i)
print(type(i)) # i is a boolean

j = None
print(j)
print(type(j)) # j has type None, which means it has no value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list

l = str(14)
print(l)
print(type(l)) # l is a string

m = 1e4
print(m)
print(type(m)) # m is a float

# 1. I found nine different data types in the provided code.
# 2. int, float, complex, str, list, dict, tuple, bool, None
# 3. b and m are both floats; d and l are both strings; e, h, and k are all lists
# 4. The data type was string because even though 14 is a number, str() converts the input value (which in this case is 14) to a string.
# 5. A data type not included was a set, which is a collection of unique elements and are useful for removing duplicates. defined with {}

n = {1, 2, 2, 3, 4}
print(n)
print(type(n))

# --- Booleans ---
print(10 > 9) # True
print(10 == 9) # False
print(10 <= 9) # False
print(bool("abc")) # True
print(bool(123)) # True
print(bool(["apple", "cherry", "banana"])) # True
print(bool(True)) # True
print(bool(False)) # False
print(bool(0)) # False
print(bool("")) # False
print(bool(" ")) # True
print(bool(())) # False
print(bool([])) # False
print(bool({})) # False
print(bool(True and False)) # False
print(bool(True and True)) # True
print(bool(False and False)) # False
print(bool(True or False)) # True
print(bool(True or True)) # True
print(bool(False or False)) # False
print(bool(not(False))) # True
print(bool(not(True))) # False

# 1. Almost everything evaluates to True as long as it has some content. If values are empty or zero like 0, empty containers, and None and False, they evaluate to False.
# 2. I was surprise by bool(" ") because the space makes it feel empty but since the space is technically content, the experession evaluated to True.
# 3. bool(15) is True because it is an integer that contains a value.
# 4. 5 == 4 is False because the expression is False.

# --- Arithmetic Operators ---
print(10 + 5)   # 15, + performs addition
print(10 - 5)   # 5, - performs subtraction
print(2 * 4)    # 8, * performs multiplication
print(6 / 3)    # 2.0, / performs division (always returns a float)
print(5 % 2)    # 1, % (modulo) returns the remainder of the division
print(3 ** 2)   # 9, ** performs exponentiation (3 to the power of 2)
print(15 // 2)  # 7, // (floor division) divides and rounds down to the nearest whole number

# --- Comparison Operators ---
print(5 == 2)   # False, == checks if two values are equal
print(10 != 10) # False, != checks if two values are NOT equal
print(2 < 5)    # True, < checks if the left is less than the right
print(12 > 5)   # True, > checks if the left is greater than the right
print(5 <= 6)   # True, <= checks if the left is less than or equal to the right
print(1 >= 10)  # False, >= checks if the left is greater than or equal to the right

# --- Assignment Operators ---
x = 5           # Assigns the value 5 to variable x
x += 5          # x is now 10 (Equivalent to x = x + 5)
x -= 4          # x is now 6  (Equivalent to x = x - 4)
x *= 3          # x is now 18 (Equivalent to x = x * 3)
print(x)        # 18

# --- Logical Operators ---
# 1. and returns True only if both statements are true
#        True Expression: (5 > 2) and (5 > 3)
#        False Expression: (2 > 5) and (5 > 2)
# 2. or returns True if at least one of the statements is true
#        True Expression: (5 > 2) or (5 < 2)
#        False Expression: (5 > 7) or (5 > 12)
# 3. not reverses the result (True becomes False & vice versa)
#        True Expression: not(5 == 2)
#        False Expression: not(5 == 5)

# 1. / is Float Division and always returns a decimal, while // is Floor Division which chops off the decimal and returns the largest whole number <= result
# 2. // gives the quotient, while % gives the remainder
# 3. You would use %. Ex) 10 % 3 = 1
# 4. They update a variable based on its current value. They perform the operation and then update with the new value

# --- Strings ---
my_string = "hello"

print(my_string)      # Prints: hello (displays the whole variable)
print(my_string[0])   # Prints: h (displays the first character (index 0))
print(my_string[1])   # Prints: e (displays the second character)
print(my_string[2])   # Prints: l (displays the third character)
print(my_string[3])   # Prints: l (displays the fourth character)
print(my_string[4])   # Prints: o (displays the fifth character)
print(my_string[-1])  # Prints: o (displays the last character using a negative)
print(my_string[1:3]) # Prints: el (displays the characters from index 1 up to (but not including) 3)
print(my_string[0:5:2]) # Prints: hlo (displays the characters from 0 to 5, skipping every 2nd char)
print(len(my_string)) # Prints: 5 (displays the total count of characters in the string)
print(my_string + "goodbye") # Prints: hellogoodbye (joins two strings together)
print(7 * my_string)  # Prints: hellohellohellohellohellohellohello (repeats the string 7 times)

# 1. Slicing is used to extract a specific chunk of a sequence by indicating a start, stop, and sometimes a step index as well. It was used in steps 8 & 9.
name = "Oski"
print("Hello, my name is", name)
# 2. prints the string "Hello, my name is Oski". A space is automatically added.
name = "Oski"
print(f"Hello, my name is {name}")
# 3. prints the string "Hello, my name is Oski".
# 4. The first version uses the print function to combine pieces and add spaces. The second version allows you to inject the variable directly inside the string.

# --- Terminal Commands ---
# 1. cd
# Changes the current working directory.
# Example: cd Documents

# 2. ls
# Lists files and folders in the current directory except for hidden ones
# Example: ls

# 3. ls -a
# Lists all files, including hidden ones (which start with a dot)
# Example: ls -a

# 4. mkdir
# Makes a new directory (folder)
# Example: mkdir python_decal

# 5. cat
# Concatenates and displays the content of a file in the terminal.
# Example: cat hello.txt

# 6. pwd
# Print Working Directory. Shows the full path of where you currently are
# Example: pwd

# 7. cd ..
# Moves you up one level to the parent directory.
# Example: cd ..

# 8. cd .
# Refers to the current directory 
# Example: ./my_script.sh

# 9. cd ~
# Moves you directly to your "Home" directory 
# Example: cd ~

# 10. cp
# Copies a file or directory from one place to another.
# Example: cp file.txt copy_of_file.txt

# 11. mv
# Moves or renames a file or directory
# Example: mv old_name.txt new_name.txt

# 12. rm
# Permanently deletes a file
# Example: rm unwanted_file.txt

# 13. clear
# Clears the terminal screen so you have a blank slate
# Example: clear

# 14. grep
# Searches for a specific text pattern in files
# Example: grep "hello" notes.txt

# 1. 
#   touch: creates a new empty file.
#       Ex) touch index.html
#   man: ("manual") shows you the documentation for any command
#       Ex) man grep
#   whoami: displays the username of the current user logged into the shell
#       Ex) whoami

# 2. ls only shows you visible files while ls -a shows everything, including hidden files that start with a period

# 3. A hidden file is any file that starts with a dot ( . ). They are usually configuration files that are hidden from the user to make things seem cleaner or prevent accidental deletion.

# 4. 
#   -l: used with ls. It shows extra details like file size, permissions, and the last modified date.
#       Ex) ls -l
#   -r: used with rm or cp. It allows the command to act on a folder and everything inside it.
#       Ex) rm -r folder_name
#   -i: used with grep. It searches for text regardless of whether it is in upper or lower case. 
#       Ex) grep -i "apple" fruit.txt