side1 = (float(input("Enter one side of a triangle: ")))
side2 = (float(input("Enter another side of a triangle: ")))
side3 = (float(input("Enter another side of a triangle: ")))

import math
semi = float((side1 + side2 + side3) / 2)
root = (semi*(semi - side1)*(semi - side2)*(semi - side3))
area = float(math.sqrt(root))
print(area)
