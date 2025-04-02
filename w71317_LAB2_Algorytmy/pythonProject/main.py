from os import remove

def zad1(tablica):
    if len(tablica)<2:
        raise ValueError("Tablica musi zawierać co najmniej 2 elementy")

    unikalne = list(set(tablica))
    if len(unikalne)<2:
        raise ValueError("Tablica musi zawierać co najmniej 2 elementy")

    unikalne.sort(reverse=True)
    return unikalne[1]

def zad2(tablica, kierunek, krok):

    if len(tablica) < 1:
        raise ValueError("Tablica musi zawierać conajmniej jeden element")

    if kierunek == "prawo":
        return tablica[-krok:]+tablica[:-krok]
    elif kierunek == "lewo":
        return tablica[krok:]+tablica[:krok]
    else:
        raise ValueError("Podaj prawo lub lewo")

def zad3(tablica, wartosc):

    if len(tablica)==0:
        raise ValueError("Tablica musi zawierać jakieś elementy")

    for i in range(0, len(tablica)-1):
        if tablica[i] == wartosc:
            print("W tablicy znajduje się", wartosc)
            return

    print("W tablicy nie znajduje się", wartosc)

def zad4(tablica, i):
    if i <= 0 or i > len(tablica):
        raise ValueError("Wartość i musi zawierać się w zakresie od 1 do ", len(tablica) )
    i = i-1
    tablica.remove(tablica[i])
    print(tablica)

def zad5(tablica1, tablica2):

    for i in range(len(tablica1)):
        for j in range(len(tablica1)):
            if(tablica1[i] < tablica1[j]):
                tablica1[i], tablica1[j] = tablica1[j], tablica1[i]

    for i in range(len(tablica2)):
        for j in range(len(tablica2)):
            if(tablica2[i] < tablica2[j]):
                tablica2[i], tablica2[j] = tablica2[j], tablica2[i]

    scalonaTablica = []

    i, j = 0, 0

    while i < len(tablica1) and j < len(tablica2):
        if tablica1[i] < tablica2[j]:
            scalonaTablica.append(tablica1[i])
            i += 1
        else:
            scalonaTablica.append(tablica2[j])
            j += 1

    while i < len(tablica1):
        scalonaTablica.append(tablica1[i])
        i += 1

    while j < len(tablica2):
        scalonaTablica.append(tablica2[j])
        j += 1

    print(scalonaTablica)

def zad6(tablica, liczbaDoWstawienia):

    for i in range(len(tablica)):
        if liczbaDoWstawienia <= tablica[i]:
            tablica.insert(i, liczbaDoWstawienia)
            print(tablica)
            return

    tablica.append(liczbaDoWstawienia)

    print(tablica)

if __name__=='__main__':
    tablica = [1, 2, 4, 5, 123, 12, 11]
    tablica1 = [1, 2]
    tablica2 = [1, 1, 1, 1, 1, 1, 2]
    tablica3 = [22, 56, 16]
    tablica4 = [12, 16, 33, 40]

    print("-------Zad1-------")
    print("Elementy tablicy:", tablica)
    print("Druga unikalna wartość maks: ", zad1(tablica))
    print("\nDruga unikalna wartość maks: ", tablica1)
    print("Druga unikalna wartość maks: ", zad1(tablica1))
    print("\nDruga unikalna wartość maks: ", tablica2)
    print("Druga unikalna wartość maks: ", zad1(tablica2))

    print("-------Zad2-------")
    print(tablica)
    print(zad2(tablica, "prawo", 2))

    print("-------Zad3-------")
    print(tablica)
    zad3(tablica, 123)

    print("-------Zad4-------")
    print(tablica)
    zad4(tablica, 3)

    print("-------Zad5-------")
    print(tablica)
    print(tablica3)
    zad5(tablica, tablica3)

    print("-------Zad6-------")
    print(tablica4)
    zad6(tablica4, 17)
