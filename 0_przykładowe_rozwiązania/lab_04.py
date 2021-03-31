# zadanie 1

# brak drobnego szczegółu o liczbie tych liczb - przyjmijmy 10
liczby = [str(liczba) for liczba in range(4, 41, 4)]
with open('podzielne_przez_4.txt', 'w') as plik:
    # plik.writelines(liczby) jedna linia
    # można użyć metody join(lista) klasy str,
    # która iteracyjnie połączy '\n'+elem1+\n+elem2...
    plik.writelines('\n'.join(liczby))


# zadanie 2

with open('podzielne_przez_4.txt', 'r') as plik:
    # mały plik to możemy tak
    # print(plik.read())
    # ale lepiej od razu
    # robić to bezpieczniej
    # jednak pamiętajmy o domyślnej wartości atrybutu
    # 'end' funkcji print() czyli end='\n'
    for line in plik:
        print(line, end='')


# zadanie 3

# właściwie to to samo co w poprzednich, więc pomijam

# zadanie 4

class NaZakupy:

    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    
    def wyswietl_produkt(self):
        # można ręcznie formatować string (print() + fstring) z wartościami, ale można też
        # posłużyć się wbudowaną zmienną przechowującą wszystkie atrybuty klasy
        return self.__dict__

    def ile_produktu(self):
        return f'{self.ilosc} {self.jednostka_miary}'

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed
    

# test klasy
nazakupy = NaZakupy('jajka', 12, 'szt.', 1.00)
print(nazakupy.wyswietl_produkt())
print(nazakupy.ile_produktu())
print(nazakupy.ile_kosztuje())


# zadanie 5

class Ciag:

    def __init__(self):
        self.elementy = []
        self.pierwszy = 0
        self.krok = 1
        self.ilosc = 0

    def wyswietl_dane(self):
        # jeżeli chcemy element na linię, można po prostu dać
        # print(self.elementy)
        for elem in self.elementy:
            print(elem)

    def pobierz_elementy(self, *elems):
        # tutaj można rozwiązać to na kilka sposobów, np. używając input
        # ale zrobimy to korzystając z *elems, który został wprowadzony na
        # zajęciach a oznacza możliwość przekazania nieokreślonej ilości atrybutów pozycyjnych
        # powinniśmy również wykonać update atrybutów start, step oraz quantity, ale pominę te operacje
        # bardzo trudne byłoby automatyczne obliczenie kroku, jeżeli ten ciąg nie będzie wpisywał się w definicję znanych ciągów (wykładniczy, geometryczny itp.)
        if elems is not None:
            self.elementy = list(elems)
        else:
            self.elementy = []

    def pobierz_parametry(self, pierwszy, krok, ilosc):
        # tutaj również można wykorzystać input(), ale przedstawię inny przykład
        # po podaniu parametrów należy wygenerować ciąg
        # nadpisujemy poprzednie wartości
        self.elementy = [elem for elem in range(pierwszy, krok*ilosc, krok)]
        self.ilosc = ilosc
        self.krok = krok
        self.pierwszy = pierwszy

    def policz_sume(self):
        # oczywiście zakładamy, że elementy są liczbami
        return sum(self.elementy)

    def policz_elementy(self):
        return len(self.elementy)   

# kilka testów klasy

ciag1 = Ciag()
print(ciag1.wyswietl_dane())
ciag1.pobierz_parametry(0, 5, 20)
ciag1.wyswietl_dane()
print(ciag1.policz_sume())
ciag1.pobierz_elementy(1,3,5,7,9)
ciag1.wyswietl_dane()