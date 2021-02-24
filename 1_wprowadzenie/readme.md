# Lab 01 - Przygotowanie środowiska pracy. Podstawowe typy danych, deklaracja zmiennych i operatory.

## **1. Składnia i organizacja kodu języka Python**

Podstawowym dokumentem opisującym organizację kodu języka Python jest dokument PEP8 znajdujący się pod adresem: https://www.python.org/dev/peps/pep-0008/

## **2. Zmienne. Podstawowe typy danych języka Python**

Zmienna to nazwa, identyfikator, który używany jest aby móc przechować wartość (wartości) do późniejszego ich wykorzystania i jednoznacznego przywołania danej porcji danych. To alias, który wskazuje na miejsce w pamięci (pośrednio) zarezerwowane dla danego obiektu (i jego danych).

**Deklaracja**  
nazwa_zmiennej = wartość

**Usuwanie**  
del a # usuwa zmienna

**Drukowanie** (wypisanie)  
print(nazwa_zmiennej) # drukuje zmienną
print(id(nazwa_zmiennej)) # drukuje adres zmiennej

**Deklaracja wielokrotna**  
zm1, zm2, zm3, …, zmn = wart1, wart2, wart3, …, wartn

Poniższy listing zawiera przykład deklaracji kilku zmiennych używających podstawowych typów danych języka Python.

**_Listing 1_:**

```python
# jest to komentarz jednowierszowy, wszelkie znaki są traktowane jako zwykły tekst, nie są interpretowane

""" to może być traktowane jako komentarz
    wielowierszowy, zmienna znakowa a często w taki sposób
    w kodzie (skryptach) umieszcza się dokumentację dotyczącą
    danego skryptu i nazywane jest to docstringiem 
"""

# typy liczbowe
liczba_calkowita = 1 # typ integer
liczba_rzeczywista = 1.0 # typ float
liczba_zespolona = 2 + 3j # typ complex

# typ logiczny (bool)
prawda = True
falsz = False

# typ znakowy
imie = 'Ariadna'
nazwisko = "Kowalska"
studia = """Informatyka,
            rok I,
            sem 2"""

# typ danych (właściwie nazwa klasy), który aktualnie jest przypisany do zmiennej można sprawdzić używając funkcji type() i przekazując zmienną jako jej argument

type(imie)

# jednak aby na standardowym wyjściu efekt działania funkcji był widoczny powinniśmy w większości przypadków użyć funkcji print() (o wyjątkach od tej reguły później)

print(type(imie))

```

## **3. Operatory**

Python posiada szereg operatorów, które wykorzystujemy w zależności od potrzeb. Poniższy listing prezentuje je w pigułce.

**_Listing 2_**:
```python
# operatory arytmetyczne

# operator dodawania
print(1 + 2)
# operator odejmowania
print(1 - 2)
# operator mnożenia
print(1 * 2)
# operator dzielenia z resztą
print(1 / 2)
# operator dzielenia bez reszty (dzielenie całkowite)
print(1 // 2)

# pamiętajmy o kolejności operacji arytmetycznych
suma = 1 + 2 * 3 / 4.0

# operatory przypisania
zmienna = "wartość" # przypisanie wartości do zmiennej
# są też skrócone postacie operatorów przypisania w połączeniu z innymi operatorami
suma = 10
suma += 1 
# to samo co
suma = suma + 1
# podobnie możemy uzywać operatorów -, *, /, //, **, % i operatorów bitowych (zachęcam do poczytania w dokumentacji)


# modulo czyli reszta z dzielenia
reszta = 12 % 5
# operator potęgowania
kwadrat = 5 ** 2
szescian = 5 ** 3

# operacje na zmiennych znakowych (string)
full_name = "Krzysztof" + " " + "Ropiak"

# tak też można
spam = "SPAM " * 10
print(spam)


# operatory porównania
liczba1 = 1
liczba2 = 2
print(liczba1 > liczba2)
print(liczba1 < liczba2)
print(liczba1 <= liczba2)
print(liczba1 >= liczba2)
print(liczba1 == liczba2)
print(liczba1 != liczba2)

# powyższe porównania zwrócą wartości typu bool czyli True lub False

prawda = True
falsz = False

# operatory logiczne
print(prawda and falsz) # koniunkcja logiczna
print(prawda or falsz) # alternatywa logiczba
print(not prawda) # negacja
print(not not prawda) # podwójna negacja
print(bool(prawda or falsz)) # użycie metody bool(), która jest tutaj wywołaniem konstruktora klasy bool (więcej w kolejnych labach)

# operatory tożsamości (identity)
liczba = 1
liczba2 = liczba

print(liczba is liczba2)
print(liczba is not liczba2)

# operatory przynależności (membership)
lista = [1, 2, 3, 4]
print(1 in lista)
print(5 not in lista)


```

Python w bardziej złożonych wyrażeniach wykonuje działania w określonej kolejności:

1. najpierw **
2. następnie *, / oraz %
3. a dopiero na końcu + i -


**W Pythonie jako fałsz traktowane są:**

* liczba zero (0, 0.0, 0j itp.)
* False
* None (null)
* puste kolekcje ([], (), {}, set() itp.)
* puste napisy
* w Pythonie 2 – obiekty posiadające metodę __nonzero__(), jeśli zwraca ona False lub 0
* w Pythonie 3 – obiekty posiadające metodę __bool__(), jeśli zwraca ona False


> W języku Python wszystko jest obiektem, a obiekty mają zazwyczaj swoje metody (funkcja zdefiniowana wewnątrz definicji klasy danego typu) i oprócz korzystania z operatorów w przedstawionej formie można również robić to z użyciem metod/funkcji właśnie. Przykłady w dokumentacji: https://docs.python.org/3/library/operator.html


### 3.1 Moduł math

Jeżeli pojawia sie potrzeba skorzystania z bardziej złożonych formuł matematycznych, stałych to najprostszym sposobem jest zaimportowanie modułu math, który jest standardowo umieszczany w środowisku python. Musimy go tylko zaimportować do przestrzeni nazewniczej naszego skryptu.

**_Listing 3_**
```python
# importowanie modułu math z aliasem m
import math as m
# można też zaimportować zawartość modułu math bez aliasu
# from math import *

# wykorzystanie kilku funkcji z modułu math
print(m.sqrt(4))
print(m.pi)
print(m.pow(2, 3))
```


**_Zadanie 1_**  
Korzystając z modułu math wykonaj poniższe działania i wyświetl ich wynik w oknie konsoli.

* $e^{10}$
* $\sqrt[6]{ln(5 + sin^28)}$
* $\lfloor 3.55 \rfloor$
* $\lceil 4.80 \rceil$

## 4. Typy wbudowane (ang. python builtins)

Już w dokumencie PEP8 możemy wyczytać, że istnieją nazwy zarezerwowane, których nie możemy używać dla naszych zmiennych (problemy pojawią się również przy nazywaniu pakietów i modułów) gdyż prowadzi to często nie tyle do jawnego błędu składniowego (ang. syntax error) zgłaszanego przez interpreter Pythona, ale częściej do błędów logicznych lub czasu wykonania (ang. logical error, runtime errors), które są dużo trudniejsze do wychwycenia i zdebugowania.

> Listę tych wbudowanych typów możemy znaleźć w dokumentacji:
>* funkcje wbudowane: https://docs.python.org/3.8/library/functions.html#built-in-funcs
>* stałe wbudowane: https://docs.python.org/3.8/library/constants.html#built-in-consts

Aktualną (z punktu widzenia uruchamianego skryptu) listę mozna również wyświetlić "w locie" czyli w dowolnym momencie w skrypcie.

**_Listing 4_**
```python

# najpierw zawartość aktualnej przestrzeni
#  czyli wszystkie niejawnie zaimportowane i do tej
# pory zadeklarowane zmienne, moduły

print(dir())

# na liście będzie prawdopodobnie wartość __builtins__
# możemy więc
print(dir(__builtins__))

```

## 5. Więcej o typie znakowym

Ciąg tekstowy w Pythonie to tablica znaków co daje z miejsca wiele możliwości manipulacji i dostępu do
składowych tego ciągu. Inna ważna cecha stringów to fakt, że po ich zadeklarowaniu nie możemy zmienić
zadeklarowanych znaków ciągu (jest to tzw. typ niemutowalny, ang. immutable). Oczywiście możemy nadpisać zmienną nową wartością lub dokleić do niej kolejny ciąg tekstowy (co tworzy niejawnie nową zmienną typu znakowego),ale pierwotny fragment jest niezmienny. Poniżej kilka przykładów.

**_Listing 5_**

```python
artykul = """Recenzja "Władcy Pierścieni"."""
imie = 'Krzysztof'
hobby = "piłka nożna"
imie = "Krzysztof"
nazwisko = "Ropiak"

# string to tablica znaków więc możemy odwołać się do jej elementów
print(imie[0])
# indeks elementu możemy również określać jako pozycja od końca ciągu
print(imie[-1])
# można również pobrać fragment ciągu (slice) określając jako indeks
# element początkowy i końcowy. Zwróć uwagę na wartość tych indeksów.
print(imie[0] + imie[-2] + imie[4:6])
# można również określic tylko jeden z dwóch indeksów
print(imie + nazwisko[3:])
# inny sposób złączania ciągów
print(imie + " " + nazwisko)

# Elementów ciągu nie można zmieniać więc poniższa instrukcja zwróci błąd.
# nazwisko[0] = "P"
# Potwierdzeniem tego, że ciąg tekstowy jej również obiektem jest możliwość
# wykonania na nim metod dla tego typu zdefiniowanych. Metoda count() zlicza
# ilość wystąpień danego ciągu w wartości przechowywanej przez zmienną.
print(imie.count("z"))

# Co ciekawe w Pythonie możemy wywoływać funkcje dla danego obiektu już podczas deklaracji
# co na pierwszy rzut oka może wyglądać dość egzotycznie.
print("Jesteś szalona!".count("a"))
# Potwierdzeniem niezmienności zadeklarowanego stringa może być również poniższy kod
print(imie.lower())
print(imie)

# Aby zwrócić długość ciągu tekstowego należy posłużyć się wbudowaną funkcją
len()
print(len(nazwisko))
```

**Zadanie 2**  
Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami. Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe. (trzeba użyć metody capitalize)
**Zadanie 3**  
Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba użyć metody count)
**Zadanie 4**  
Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu. Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0]. Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.
**Zadanie 5**  
Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy. (trzeba użyć metody split)