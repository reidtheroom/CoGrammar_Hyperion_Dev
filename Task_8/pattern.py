# print a pattern with increasing asteriks until line 4
count = 4

for n in range(1, count * 2):
    if n <= count:
        print("*" * n)
# asteriks pattern decreases by 1 after line 4
    else:
        print("*" * (count * 2 - n))




