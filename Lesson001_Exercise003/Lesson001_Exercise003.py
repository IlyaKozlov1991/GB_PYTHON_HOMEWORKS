# Write a code which will receive coordinates of a point and check in which quadrant it is, or on which axle

x = int(input("Enter X: "))
y = int(input("Enter Y: "))

# block of checking for quadrants
if x > 0 and y > 0:
    print("Your point is in the FIRST(1) quadrant")
if x < 0 and y > 0:
    print("Your point is in the SECOND(2) quadrant")
if x < 0 and y < 0:
    print("Your point is in the THIRD(3) quadrant")
if x > 0 and y< 0:
    print("Your point is in the FOURTH(4) quadrant")

# block of checking for axles
if y == 0 and (x < 0 or x > 0):
    print("Your point is on X axle")
if x == 0 and (y < 0 or y > 0):
    print("Your point is on Y axle")