n = float(input("Enter a number: "))

number = 0

counter = 0

while n != -1:
    counter += 1
    number += n
    n = float(input("Enter a number: "))

if counter > 0:
    print(f"Your average is {number /  counter}")
else:
    print("No average could be calculated.")


        




