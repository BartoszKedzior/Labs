import string
import math
first_name = str('Bartosz')
last_name = str('Kedzior')
full_name = first_name + ' ' + last_name
print(full_name)

print("\n")

first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
message = print(f"Dear {first_name}, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at {full_name}. We are looking forward to seeing you!")
message2 = print(full_name)
message3 = print(f"Dear {first_name}, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at {full_name}. We are looking forward to seeing you!")


print("\n")

print(first_name[:])
print(first_name[1:])
print(first_name[:1])
print(first_name[0])
print(first_name[1])
print(first_name[-1])
print(last_name[1:3])

print("\n")

length = 2.75
width = 1.75
area = length * width
show = f"With width {width} and length {length} of the room, its area is equal to {area}."
print(show)

# print("With width: " + str(width) + "and length: " + str(length) + " of the room, its area is equal to: " str(area))

print("With width:", width, "and length:", length,
      "of the room, its area is equal to:", area)

print("\n")

complex = 3.14 + 1j
print(complex)  # (3.14+1j)

complex = 3.14 + 1j
print(complex.real)  # 3.14
print(complex.imag)  # 1.0

print("\n")

a = -2 + 3j
b = 4 + 2.1j
result = a + b
print(result)
print(result.real)
print(result.imag)

print("\n")

a = math.sqrt(100)
b = math.floor(10.1)
c = math.pi**2
z = a/b * c
print(z)

print("\n")

a = -2
b = 7
c = -6
D = (b**2) - (4 * a * c)
print("D: ", D)

x1 = (-b + D**0.5) / (2 * a)

x2 = (-b - D**0.5) / (2 * a)

print("x1:", x1)
print("x2:", x2)
print(x1 + x2)

print("\n")

1 > 2  # Fałsz

print(1 > 2)

"""Python posiada operatory relacji do porównywania ze sobą wartości zmiennych:

    < (mniej niż)
    <= (mniejszy lub równy)
    > (więcej)
    >= (większy lub równy)
    == (równe)
    != (nie równy)

    bool jest podtypem True/False liczby całkowitej. Może posiadać wartość 1 (odpowiadającą True) lub 0 (odpowiadającą False).
"""
is_active = bool(1)
is_delete = bool(0)
print(is_active)
print(is_delete)
print(is_active, is_delete)

print("")
name = 'Bartosz'
age = 43
is_active = bool(1)
subscription = None
print(f"{name} plus {age} plus {is_active} plus {subscription}.")

print("")

age = 43  # input("Ile masz lat?")
age = int(age)
print("Mam", age, "lata")
pi = float('3.14')
print(pi)
print(bool(''))
print(bool())
print(bool([]))
print(bool(0))
print(bool(45))
bool(0)  # False
bool(1)  # True

print("")

length = "2.75"
width = "1.75"
area = float(length)*float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print(show)
print("With width:", width, "and length:", length,
      "of the room, its area is equal to:", area)
print("")
"""Współrzędne Kijowa w stopniach:
    Szerokość geograficzna lat1 = 50.45
    Długość geograficzna lon1 = 30.523
Współrzędne Londynu w stopniach:
    Szerokość geograficzna lat2 = 51.5072
    Długość geograficzna lon2 = -0.1275
Przyjmijmy, że promień Ziemi wynosi 6371,01 km. Odległość w kilometrach między miastami, biorąc pod uwagę krzywiznę planety, można znaleźć według następującego wzoru:
odległość = 6371.01 · arccos(sin(lat1) · sin(lat2) + cos(lat1) · cos(lat2) · cos(lon1 - lon2))
Należy pamiętać, że funkcje trygonometryczne w Pythonie działają w radianach. Oznacza to, że stopnie muszą zostać przekonwertowane na radiany przed obliczeniem odległości między punktami. Aby to zrobić, moduł math posiada funkcję o nazwie radians
<radians> = math.radians(<degrees>)
Również:
    arccos(x) — to math.acos(x)
    sin(x) — to math.sin(x)
    cos(x) — to math.cos(x)
Oblicz distance za pomocą podanego wzoru, korzystając z sugerowanych metod math."""

"""
RADIUS = 6371.01

lat1 = math.degrees(50.45)
lat1a = math.radians(lat1)
print(lat1a)
lon1 = math.degrees(30.523)
lon1a = math.radians(lon1)
print(lon1a)
print("")

lat2 = math.degrees(51.5072)
lat2a = math.radians(lat2)
print(lat2a)

lon2 = math.degrees(-0.1275)
lon2a = math.radians(lon2)
print(lon2a)
"""

print("Zadanie 14/16.")
RADIUS = 6371.01
print("Earth's radius is:", RADIUS)
print("Współrzędne Kijowa w stopniach, skonwertowanych do radianów:")
lat1 = math.radians(50.45)
print(lat1)
lon1 = math.radians(30.523)
print(lon1)
print("Współrzędne Londynu w stopniach, skonwertowanych do radianów:")
lat2 = math.radians(51.5072)
print(lat2)
lon2 = math.radians(-0.1275)
print(lon2)
distance = RADIUS * math.acos(((math.sin(lat1)) * math.sin(lat2)) +
                              (math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)))
print("Distance between Kiev and London is:", distance)
print("\n")

print("Zadanie 15/16.")
name = string.capwords(input("State your full name: "))
email = str(input("Enter your email address: "))
while '@' not in email:
    print('Submitted email address is incorrect')
    email = input('Enter correct email address: ')

age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
print("A person with the name", name, "with email address",
      email, "is", age, "years old and is", height, "feet tall")
is_active = bool(input(
    ("Do you want to receive notifications? Click 1 for yes, otherwise click enter:  ")))
print("")
if (is_active):
    print(f"{name} wyrazil zgodę na przesyłanie powiadomień")
else:
    print(f"{name} nie wyrazil zgody na przesyłanie powiadomień")


print("\n")

print("Zadanie 16/16.")

length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = (length*width)
show = area
print(show)
