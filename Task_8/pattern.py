count = 4

# range(start, end, step); does not include end, need end to stop at 5 if you want 4 asteriks
for n in range(1, count + 1):
    print("*" * n)
    if n == 4:
        for y in range(count - 1, 0, -1):
            print("*" * y)





