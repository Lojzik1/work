def sčítání(x, y):
    return x + y

def odčítání(x, y):
    return x - y

def násobení(x, y):
    return x * y

def dělení(x, y):
    return x / y

def vstup():
    x = int(input("Zadejte první číslo: "))
    y = int(input("Zadejte druhé číslo: "))
    return x,y

def result(výsledek):
    print("Výsledek:", výsledek)

def program():
    x,y = vstup()
    operace = input("Zadejte operaci (+, -, *, /): ")
    if operace == "+":
        výsledek = sčítání(x,y)
    elif operace == "-":
        výsledek = odčítání(x,y)
    elif operace == "*":
        výsledek = násobení(x,y)
    elif operace == "/":
        výsledek = dělení(x,y)
    else:
        print("Neplatná operace.")
        return
    result(výsledek)

if __name__ == '__main__':
    program()