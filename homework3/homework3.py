# 3.1 Say Goodbye
def say_goodbye(name):
	print("Goodbye,", name)

# 3.2 Area of a Circle
def circle_area(radius):
	print(3.14*(radius**2))

# 4.1 Subtract, Multiply, and Divide
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b!= 0:
    	return a / b

# 5.1 What Should I Wear?
def get_temp_range(temps):
    return (min(temps), max(temps))

# 5.2 Check if it's the Weekend
def is_weekend(day_num):
    return day_num == 6 or day_num == 7

# 5.3 Fuel Efficiency Calculator
def calculate_mpg(distance, fuel_used):
    return distance/fuel_used

# 5.4 Secret Code
def encrypt_data(n):
    last_digit = n % 10
    remaining_digits = n // 10
    power = len(str(remaining_digits))
    return (last_digit * (10 ** power)) + remaining_digits

# 6.1 Oski Stole Your Power
def manual_power(x, y):
    result = 1
    for i in range(y):
        result = result * x
    return result

# 6.2.1 For Loops
def find_min_for(nums):
    minimum = nums[0]
    for n in nums:
        if n < minimum:
            minimum = n
    return minimum

def find_max_for(nums):
    maximum = nums[0]
    for n in nums:
        if n > maximum:
            maximum = n
    return maximum

# 6.2.2 While Loops
def find_min_while(nums):
    minimum = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] < minimum:
            minimum = nums[i]
        i += 1
    return minimum

def find_max_while(nums):
    maximum = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] > maximum:
            maximum = nums[i]
        i += 1
    return maximum

# 6.3 Calculate the Sum
def calculate_sum(n):
    total = 0
    while n > 0:
        total += n % 10 
        n //= 10 
    return total

n = 2468
result = calculate_sum(2468) # sum of 2, 4, 6, and 8 (20)
print(f"The result of Calculate Sum (6.2) with n = {n} is {result}")
