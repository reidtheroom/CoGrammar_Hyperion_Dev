str_manip = input("Enter a sentence: ")
print(len(str_manip))
last_letter = str_manip[-1]
replace_string = str_manip.replace(last_letter,"@")
print(replace_string)
str_splice = str_manip[-1:-4:-1]
print(str_splice)
extract_letter_3 = str_manip[0:3]
extract_letter_2 = str_manip[-2::1]
join_str_manip = "".join(extract_letter_3 + extract_letter_2)
print(join_str_manip)