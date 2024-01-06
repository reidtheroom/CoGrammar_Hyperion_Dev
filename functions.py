def multiply(x, y):
    print(x * y) # x and y are integers/floats

def multiply2(a, b):
# can have default values in parameters, but can replace values when calling function
    return a * b 

multiply(3, 4)

# need to use print function to print the return value from multiply2 function
print(multiply2(4, 8)) 

num1 = int(input("Enter a number: ")) # typecast to integer/float
num2 = int(input("Enter a number: "))
multiply(num1, num2)

def is_even(num):

    while True:
        if num % 2 == 0:
            print("Your number is even")
            return
        else:
            print("Your number is NOT even")
            return
        
print(is_even(num = 19))

def get_int(display_string = "Please enter a number: "):

    while True:
        user_input = input(display_string)

        try:
            result = int(user_input)
            return result
        
        except:
            print("Please only enter a number.")

total = 0

while True:
    user_choice = get_int()

    if user_choice == -1:
        break

    total += user_choice

    print(f"This is the Total: {total}")