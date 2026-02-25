# --- 3.1 List Operations ---
foods = ["Udon", "Cheesecake", "Hotpot", "Cheesy Rice Cakes", "Bread"]

# 1. Print the second food in the list.
print(foods[1])

# 2. Print the last food using negative indexing.
print(foods[-1])

# 3. Add a new food to the end of the list using .append().
foods.append("Cinnamon Roll")

# 4. Insert ”apple” at the start of the list.
foods.insert(0, "apple")

# 5. Remove the third item in the list using del or .remove().
del foods[2]

# 6. Print the length of the list with len().
print(len(foods))

# 7. Loop through the list and print each food in uppercase.
# Hint: Use .upper().
for food in foods:
    print(food.upper())

# 8. Create a new list containing only the first and last food (use slicing).
first_and_last = foods[::len(foods)-1]
print(first_and_last)

# 9. Use an if statement to check if ”potato” is in the list. If it is, print "A potato!". Otherwise,
# print "No potato!".
if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

# --- 3.2 Slicing and Striding ---
numbers = list(range(21))

# 1. get first 15(numbers)
# Takes a list of numbers and returns the first 15 elements.
def get_first_15(numbers): 
    return numbers[:15]
'''
I encountered this error:
"NameError: name 'get_first_15' is not defined"
I originally wrote: step1 = get_first_15(numbers)
I forgot to import the function from my file into the terminal session. 
I fixed it by typing "h4." in front of the function name after importing the module.
'''

# 2. get every 5th(lst)
# Takes the list from get first 15() and returns every 5th element from it.
# (So index 0, 5, 10...)
def get_every_5th(lst):
    return lst[::5]

# 3. reverse and stride(lst)
# Takes the list from get every 5th() and:
# • Reverses it
# • Then returns every 3rd element of the reversed list
def reverse_and_stride(lst):
    reversed_lst = lst[::-1]
    return reversed_lst[::3]

# --- 3.3.1 Nested List Operations ---
numbersNested = [[1,2,3],[4,5,6],[7,8,9]] 

# 1. Print the third row. Hint: Use list[row][column] indexing.
print(numbersNested[2])

# 2. Print the second item in the second row.
print(numbersNested[1][1])

# 3. Add [10, 11, 12] as a new row using .append().
numbersNested.append([10, 11, 12])

# 4. Write a function called sum nested() that loops through each row, sums all numbers, and
# returns the total.
def sum_nested(nested_list):
    total = 0
    for row in nested_list:
        for num in row:
            total += num
    return total

# --- 3.4 Create a 5x5 List ---
# Write a function that uses nested for loops to create a 5x5 list of numbers from 1 to 25. Store
# the result in a new variable.
def create_5x5():
    grid = []
    counter = 1
    for i in range(5):       
        row = []
        for j in range(5):   
            row.append(counter)
            counter += 1
        grid.append(row)
    return grid

# 1. Write a function that replaces all multiples of 3 with “?”. Store the updated 5x5 list in a
# new variable.
def replace_multiples_of_3(nested_list):
    for row_index in range(len(nested_list)):
        for col_index in range(len(nested_list[row_index])):
            value = nested_list[row_index][col_index]
            if value % 3 == 0:
                nested_list[row_index][col_index] = "?"
    return nested_list

# 2. Write a function that adds all elements not equal to “?” and returns the sum. Save the
# result in a variable
def sum_non_question_marks(nested_list):
    total_sum = 0
    for row in nested_list:
        for item in row:
            if item != "?":
                total_sum += item
    return total_sum
'''
I encountered this error:
"TypeError: unsupported operand type(s) for +=: 'int' and 'str'"
I originally wrote: total_sum += item
I tried to sum a list that contained the string "?". I fixed it by using if item != "?": to skip over the strings and only sum the numbers.
'''

# --- 4.1 Dictionary Operations ---
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

# 1. Print “Katie”’s age
print(ages["Katie"])
'''
I encountered this error:
"KeyError: 'katie'"
I originally wrote: print(ages["katie"])
I used a lowercase 'k', but dictionary keys are case-sensitive. 
I fixed it by capitalizing "Katie" to match the dictionary key exactly.
'''

# 2. Change Mira’s age to 100
ages["Mira"] = 100

# 3. Add “Milana" with an age of 52
ages["Milana"] = 52

# 4. Remove “Mariam" from the dictionary
del ages["Mariam"]

# 5. Use a for loop to print out each person’s name and age
for name, age in ages.items():
    print(f"{name} is {age} years old.")


print(f"Total Sum: {sum_nested(numbersNested)}") # Include code at the bottom of your file that calls this function and prints the result.