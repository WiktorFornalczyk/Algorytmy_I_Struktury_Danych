#push(element)
#pop(element)
#top/pik(element)
#size(element)

#1. Rozpocznij z pustym stosem.
#2. Wczytaj ciąg znaków z nawiasami.
#3. Przetwarzaj ciąg idąc od lewej do prawej.
#4. Jeśli aktualny znak jest nawiasem otwierającym, wstaw go na stos.
#5. Jeśli aktualny znak jest nawiasem zamykającym, ściągnij nawias otwierający z wierzchołka stosu.
#6. Jeśli po dojściu do końca ciągu stos jest pusty i nie wystąpiły żadne błędy, nawiasy są poprawne.

from collections import deque

def parChecker(symbolString):
    stos = []
    for znak in symbolString:
        if znak == '(':
            stos.append(znak)
        if znak == ')':
            if not stos:
                return False
            stos.pop()

    return len(stos) == 0



#main
testy = [
    "((()))()",
    "((((()))))",
    "(()(())"
]

for ciag in testy:
    print(f"{ciag} -> {'Poprawny ciąg nawiasów' if parChecker(ciag) else 'Błędny ciąg nawiasów'}")

