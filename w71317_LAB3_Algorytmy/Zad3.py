class KolejkaLista:
    def __init__(self):
        self.kolejka = []
    def enqueue(self, element):
        """Dodaje element na koniec kolejki"""
        self.kolejka.append(element)
    def dequeue(self):
        """Usuwa i zwraca element z początku kolejki"""
        if not self.is_empty():
            return self.kolejka.pop(0)
        raise IndexError("Kolejka jest pusta!")
    def front(self):
        """Podgląda pierwszy element kolejki bez usuwania"""
        if not self.is_empty():
            return self.kolejka[0]
        return None
    def is_empty(self):
        """Sprawdza, czy kolejka jest pusta"""
        return len(self.kolejka) == 0
    def size(self):
        """Zwraca rozmiar kolejki"""
        return len(self.kolejka)


GraWZiemniaka = KolejkaLista()

GraWZiemniaka.enqueue("Brad")
GraWZiemniaka.enqueue("Bill")
GraWZiemniaka.enqueue("David")
GraWZiemniaka.enqueue("Susan")
GraWZiemniaka.enqueue("Jane")
GraWZiemniaka.enqueue("Kent")

print("Gra w Gorącego Ziemniaka: Brad -> Bill -> David -> Susan -> Jane -> Kent")

while GraWZiemniaka.size() > 1:
    print(f"\nZiemniaka trzyma {"\033[91m"}{GraWZiemniaka.front()}{"\033[0m"}")
    iloscPodanZiemniaka = input("Ile razy podasz ziemniaka? ")
    for i in range(1, int(iloscPodanZiemniaka)):
        GraWZiemniaka.enqueue(GraWZiemniaka.dequeue())
    GraWZiemniaka.dequeue()

print(f"\n\n{"\033[93m"}Grę wygrał(a) {GraWZiemniaka.front()} 👑 !!!{"\033[0m"}")