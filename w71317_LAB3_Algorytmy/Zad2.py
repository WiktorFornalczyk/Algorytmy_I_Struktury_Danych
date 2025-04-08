import math

def WyrazenieONP():
    stos = []
    print(f"{"\033[91m"}!!! Aby zakończyć, podaj operator '=' !!!{"\033[0m"}")
    print(f"{"\033[93m"}! Nie można podać pustego wyrażenia !{"\033[0m"}")
    print(f"{"\033[93m"}! Pierwsze dwa pola nie mogą być operatorami !{"\033[0m"}")
    print(f"{"\033[93m"}! Można używać tylko liczb bądź operatorów: '+' '-' '/' '*' '^' '=' !{"\033[0m"}")

    i = 1
    while True:
        liczbaLubZnak = input(f"Podaj {i} liczbę/znak: ")

        if liczbaLubZnak == "":
            raise ValueError("Podano pustą wartość")

        if i == 1 or i == 2:
            if math.isnan(int(liczbaLubZnak)):
                raise ValueError(f"Pod indeksem 1 i 2 musi znaleźć się liczba ")

        if liczbaLubZnak == "=":
            print(stos)
            break

        if liczbaLubZnak == "+":
            l2 = int(stos.pop())
            l1 = int(stos.pop())
            wynik = l1 + l2
            stos.append(int(wynik))
            i += 1
            print(stos)
            continue
        elif liczbaLubZnak == "-":
            l2 = int(stos.pop())
            l1 = int(stos.pop())
            wynik = l1 - l2
            stos.append(int(wynik))
            i += 1
            print(stos)
            continue
        elif liczbaLubZnak == "/":
            l2 = int(stos.pop())
            l1 = int(stos.pop())
            wynik = l1 / l2
            stos.append(int(wynik))
            i += 1
            print(stos)
            continue
        elif liczbaLubZnak == "*":
            l2 = int(stos.pop())
            l1 = int(stos.pop())
            wynik = l1 * l2
            stos.append(int(wynik))
            i += 1
            print(stos)
            continue
        elif liczbaLubZnak == "^":
            l2 = int(stos.pop())
            l1 = int(stos.pop())
            wynik = math.pow(l1, l2)
            stos.append(int(wynik))
            i += 1
            print(stos)
            continue

        if not math.isnan(int(liczbaLubZnak)):
            stos.append(int(liczbaLubZnak))
            i += 1
            print(stos)
            continue

        raise ValueError("Wprowadzono niepoprawny znak!")

WyrazenieONP()
