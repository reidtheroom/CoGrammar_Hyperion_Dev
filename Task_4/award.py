swimming_time = float(input("How long (in minutes) did it take to complete your swimming event? "))
cycling_time = float(input("How long (in minutes) did it take you to complete your cycling event? "))
running_time = float(input("How long (in minutes) did it take you to complete your running event? "))

total_time = swimming_time + cycling_time + running_time
print(f"Your total triathlon time was {total_time} minutes.")

if total_time < 101:
    print("You receive the provincial colours award! Well Done!")
elif total_time < 106:
    print("You receive the provincial half colours award! Well Done!")
elif total_time < 111:
    print("You receive the provincial scroll award! Well Done!")
else: 
    total_time >= 111
    print("You receive no award. Better luck next time!")
    
    