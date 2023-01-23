## Domineering
Ovaj repo predstavlja finalnu verziju aplikacije domineering za kurs: Vestacka inteligencija.

### Struktura:
    /reports - reporti za svaku od faza 
    /sounds - zvuci za samu igru
    /src - source code
    /src/board.py - sadrzi funkcionalnosti vezane za samu tablu
    /src/const.py - sadrzi neke globalne konstante za celokupnu app
    /src/domino.py - model domine
    /src/form.py - sadrzi funkcionalnosti vezane za pocetnu formu i za pokupljanje unetih podadatak na njoj
    /src/game.py - sadrzi funkcionalnosti za odigravanje igre i kontrolise tablu i interfejsno odigravanje poteza
    /src/main.py - sadrzi funkcionalnost za kreiranje same table kao matrice i za osvezavanje i slusanje evenata sa GUI-a
    /src/square.py - model koji predstavlja jedan square na tabli

### Krarak opis:

 - Dakle za resavanj ovog problema koristili smo pygame library koji sadrzi funkcionalnosti za GUI, za osvezavanje i slusanje evenata, za zvuke...
Glavna ideja bila je kreiranje table kao matrice objekata tipa Square, gde svaki od njih ima u sebi poziciju na tabli i deo domine koji drzi, u pocetku je to defaultovano na None, kao sto se moze videti u terminalu prilikom pocetka igre.

- Na svaki odigran potez slusa se event i okida se metoda koja na osnovu koordinata strelice i na osnovu trenutnog igraca odlucuje na kojim pozicijama u matrici je potrebno postaviti dominu. Gde se dalje vrse provere prvo da li je potez ispravan i da li je mesto za postavljanje domine slobodno.
- Ukoliko sve to prodje postavlja se properti objekata Square, i to piece i domino, na toj i toj poziciji postavlja nova domina i eventualno neki text 'X' ili 'O' cisto za prikaz table preko terminala gde se nakon toga tabla stampa.
- Takodje se stampaju svi moguci potezi trenutnog igraca u terminalu.
- Nakon toga se switchuje igrac i nastavlja racunar ukoliko je covek prvi odigrao potez. Onda kada igra racunar, na osnovu svih mogucih poteza odredjuje koje je njegovo najbolji potez, do odredjene dubine gde vrsi heuristiku i na osnovu nje odredjuje koji je najbolji potez.
- Ukoliko je tabla veca od 5x5 zbog UX je konfigurisan da vrsi odigravanje tacno odredjenih poteza iz pool-a. U prvih 4 poteza, te se zbog toga duze ceka na oidgravanje poteza racunara nakon 4og poteza racunara.