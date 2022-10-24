# Give a natural number (N). Write a program that lists prime factors of (N)


from re import M


n = int(input("Enter Your number (N): "))

list1 = []
i = 2

while i * i <= n:
    if n % i == 0:
            list1.append(i)
            n = n // i
    else:
            i += 1
if n > 1:
    list1.append(n)
print(f'\nList of prime fctors: {list1}\n')
