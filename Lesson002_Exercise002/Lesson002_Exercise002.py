# Write a code which will check either ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is TRUE or FALSE

x = int(input("Enter X: "))
y = int(input("Enter Y: "))
z = int(input("Enter Z: "))

c = ~(x + y + z) == ~(x) * ~(y) * ~(z)

print(c)