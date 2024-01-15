string = "my name is jubaydah, and i am the best in the world."

string_alternate = ''

# switching between each letter/index value

for x in range(len(string)):
    if x % 2 == 0:
        string_alternate += string[x].lower()
    else:
        string_alternate += string[x].upper()
print(string_alternate)

# switching between each word

seperate_string = string.split()

alternate = []

string_alternate = ''

for x in range(len(seperate_string)):
    if x % 2 == 0:
        alternate.append(seperate_string[x].lower())
    else:
        alternate.append(seperate_string[x].upper())

string_alternate = ' '.join(alternate)
print(string_alternate)