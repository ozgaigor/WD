# Lab 02 - Zapisywanie i wykonanie skryptów. Instrukcje sterujące.

## **1. Wprowadzanie danych ze standardowego wejścia**

Do wprowadzania danych możemy użyć komendy `input`.

**_Listing 1_**
```python
a = input("Tu jest jakiś komunikat np. Podaj liczbę\n")
print(a)

# Możemy użyć też komend readline() i write(s), które są w module sys
import sys

print("Podaj jakiś tekst")
s = sys.stdin.readline() #Wczytuje wiersz
print("Twój tekst to: " + s)
# Do wydruku można użyć też komendy write np.
sys.stdout.write(s)
```


**Zadanie 1**  
Napisz skrypt, który pobiera od użytkownika zdanie i liczy w nim spacje. Wynik wyświetla na ekranie (użyj instrukcji `input`)

**Zadanie 2**  
Napisz skrypt, który pobiera od użytkownika dwie wartości i mnoży je przez siebie. Wynik wyświetla na ekranie (użyj instrukcji `readline()` i `write()`).

## **2. Instrukcja warunkowa**

**Składnia:**  
```python
if warunek_1:
    Instrukcje_1
[elif warunek_2:
    Instrukcje_2:
…
elif warunek_n:
    Instrukcje_n
else:
    Inne_instrukcje]
```

**_Listing 2_**
```python
# Pobieramy od użytkownika liczbę
# Chcemy sprawdzić czy jest dodatnia czy ujemna
liczba = input("Podaj jakąś liczbę")

# liczba jest typu string musimy ją rzutować na całkowitą
liczba = int(liczba)
if liczba > 0:
    print("Podano liczbę dodatnią")
elif liczba < 0:
    print("Podano liczbę ujemną")
else:
    print("Podano liczbę równą zero")

# Sprawdzamy, która liczba jest większa
liczba = input("Podaj pierwszą liczbę")
k = input("Podaj drugą liczbę")

# liczba, k są typu string musimy ją rzutować na całkowitą
liczba = int(liczba)
k = int(k)

# przy wyświetlaniu zmieniamy liczbę na typ string
if liczba > k:
    print("Liczba=" + str(liczba) + " jest większa")
else:
    print("Liczba=" + str(k) + " jest większa")
```

**Zadanie 3**  
Odszukaj w dokumentacji, jakie operatory można używać w instrukcjach warunkowych (np. równe, różne, mniejsze bądź równe itp.)

**Zadanie 4**  
Napisz skrypt, który pobiera od użytkownika liczbę i wypisuje na ekran wartość bezwzględną tej liczby

**Zadanie 5**  
Napisz skrypt, który pobiera od użytkownika trzy liczby a, b i c. Sprawdza następujące warunki:
* czy a zawiera się w przedziale (0,10> 
* oraz czy jednocześnie a>b lub b>c. 

Jeśli warunki są spełnione lub nie to ma się wyświetlić odpowiedni komunikat na ekranie.

## **3. Instrukcja iteracyjna for**

**Składnia:**

for licznik in sekwencja:
    Instrukcje
[else:
    inne_instrukcje]


Sekwencją może być łańcuch, lista lub krotka. Od obliczenia sekwencji zaczyna się działanie instrukcji iteracyjnej. Licznik przyjmuje wartość pierwszego elementu wykonuje instrukcje, następnie przyjmuje wartość kolejnego elementu itd.

Do utworzenia sekwencji możemy użyć funkcji `range`:

**_Listing 3_**
```python
range([start], stop[, krok])

# Chcemy wyświetlić liczby od 1 do 5
for x in range(1, 6, 1):
    print(str(x) + " ")

# Tworzymy swoją listę i chcemy jej użyć jako sekwencji do wyświetlania wartości
lista = [3, 4, 2, 1, 6]
for x in lista:
    print(str(x) + " ")

# Wyświetlamy elementy za pomocą pętli ale na koniec odpowiedni komunikat
lista = [3, 4, 2, 1, 6]
for x in lista:
    print(str(x) + " ")
else:
    print("Koniec wyświetlania")
```


**Zadanie 6**  
Napisz pętlę, która wyświetla liczby podzielne przez 5 z zakresu <0,50>

**Zadanie 7**  
Napisz pętle, która pobiera liczby od użytkownika i wyświetla ich kwadraty na ekranie. Liczby pobierane są w postaci oddzielonej spacjami.

## **4. Instrukcja iteracyjna while**

**Składnia:**

while warunek:
instrukcje
[else:
inne_instrukcje]


**_Listing 4_**
```python
# skrypt wyświetla losowe liczby całkowite aż napotka 5
import random # biblioteka z funkcjami do losowania


random.seed() # inicjowanie generatora
z = random.randint(1, 15) # losowanie pierwszej liczby

while(z != 5):
    print(str(z))
    z = random.randint(1,15)
else:
    print("Znalazłem 5 koniec działania")
```

**Zadanie 8**  
Napisz skrypt, który odczytuje liczby od użytkownika i umieszcza je na liście. Wykorzystaj pętle while.

**Zadanie 9**  
Napisz skrypt, który odczytuje od użytkownika liczbę wielocyfrową i sumuje jej cyfry. Wynik wyświetla na ekranie. Wykorzystaj pętle while.

## **4. Instrukcje break i continue**

Instrukcje umieszczamy w pętlach. Sterują działaniem pętli.

Break – przerywa działanie pętli w której się znajduje (ale nie wszystkich pętli jeśli pętle zagnieżdżamy)

Continue – kończy przebieg aktualnej iteracji pętli i przechodzi do następnego przebiegu.

**_Listing 5_**
```python
# Użytkownik podaje liczbę
# Przeglądamy listę liczb i jeśli znajdziemy tę podaną przez użytkownika
# wyświetlamy komunikat i kończymy działanie pętli
lista = [1, 5, 3, 2, 6, 7, 8, 9, 10]
print("Podaj liczbę a sprawdzę czy jest na liście")
liczba = input()
licznik = 0

while licznik < 10:
    # Jeśli znajdziemy liczbę przerywamy
    if int(liczba) == lista[licznik]:
        print("Twoja liczba: " + liczba + "znaleziona na pozycji: " + str(licznik))
        break
    else:
        licznik += 1 
```    
**Instrukcje iteracyjne zagnieżdżone**

Pętle, instrukcje warunkowe możemy umieszczać jedna w drugiej. Nazywamy to zagnieżdżaniem.

**Przykład**

Chcemy wyświetlić wzór na ekranie:
```
H   H
H   H
HHHHH
H   H
H   H
```

**_Listing 6_**
```python
import sys


for i in [1, 2, 3, 4, 5]:
    for j in [1, 2, 3, 4, 5]:
        #sprawdza czy jest w pionowej linii H
        if i == 3:
            sys.stdout.write('H')
        #jeśli nie to rysuje H na brzegach
        else:
            #sprawdzamy czy j zawiera się na liście, czyli jest na brzegach
            if j in [1, 5]:
                sys.stdout.write('H')
            #jeśli nie piszemy spację
            else:
                sys.stdout.write(' ')
    sys.stdout.write('\n')
```

**Zadanie 10**  
Napisz skrypt, który rysuje wieżę z literek. Użytkownik podaje wysokość wieży ale nie więcej jak 10.
```
A
AA
AAA
AAAA
AAAAA
AAAAAA
```
**Zadanie 11**  
Napisz skrypt, który rysuje diament. Użytkownik podaje wysokość nie mniej jak 3 i nie więcej jak 9
wysokość=3
```
 o
ooo
 o
```
wysokość równa 5
```
  o
 ooo
ooooo
 ooo
  o
```
itd.

**Zadanie 12**  
Napisz skrypt, który wyświetla i oblicza tabliczkę mnożenia od 1 do 100 w formie znanej z lekcji matematyki w szkole podstawowej.