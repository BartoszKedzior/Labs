# Funkcje cwiczenia
# Lekcja 49.
# Lekcja 50.
# Lekcja 51.

# Program liczący powierzchnie figur




import math

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h

PoleKwadrat = print("1. Pole kwadratu")
PoleProst = print("2. Pole Prostokąta")
PoleKola = print("3. Pole koła")
PoleTrojkat = print("4. Pole trójkąta")
PoleTrapez = print("5. Pole trapezu")
             
select = input('Wybierz z menu od 1 do 5 figure dla ktorej chcesz obliczyc pole: ')

if input == "1":
    a = str(input("Podaj dlugosc boku a: "))
    if a == 0:
        print("Podales nieprawidlowa liczbe!")
        a = input("Podaj liczbe calkowita: ")
    else:    
        b = input("Podaj dlugosc boku b: ")
        if b == 0:
            print("Podales nieprawidlowa liczbe!")
            b = input("Podaj liczbe calkowita: ")

Odpowiedz = print(pole_kwadratu(a, b))

                    

