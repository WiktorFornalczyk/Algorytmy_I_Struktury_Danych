tab = [1, 3, 6, 5, 4, 8, 2, 7]

def sortowanie_babelkowe(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1]:
                temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = temp
    return tab


print(sortowanie_babelkowe(tab))