import logging

logging.basicConfig(level=logging.DEBUG)

def dates():
    print("Podaj dzialanie, posugujc sie odpowiednia liczba: \n 1 Dodawanie \n 2 Odejmowanie \n 3 Mnozenie \n 4 Dzielenie")
    operation = int(input("Wskaz numer wybranego dzialania "))

    print("Podaj pierwsza liczbe dzialania: ")
    x = float(input("Podaj swoja pierwsza liczbe: "))
    print("Podaj druga liczbe dzialania: ")
    y = float(input("Podaj swoja druga liczbe: "))
    return operation, x, y

def add(x, y):
    logging.info(f"Dodawanie {x} + {y} rowna sie: ")
    return x + y

def subtract(x, y):
    logging.info(f"Odejmowanie {x} - {y} rowna sie: ")
    return x - y

def multiply(x, y):
    logging.info(f"Mnozenie {x} * {y} ronwa sie: ")
    return x * y 

def divide(x, y):
    logging.info(f"Dzielenie {x} / {y} rowna sie: ")
    return x / y

def main():
    operation, x, y = dates()

    if operation == 1:
        print(add(x, y))
    elif operation == 2:
        print(subtract(x, y))
    elif operation == 3:
        print(multiply(x, y))
    elif operation == 4:
        print(divide(x, y))

if __name__ == "__main__":
    main()