# Prace s cizim kodem
- Vysledek je b-ta mocnina a = a^b
- Promenna a je zaklad, promenna b je exponent
- Funkcnost - porovnaval jsem vysledky s funkci math.pow a nenasel jsem zadnou neshodu

### Doporuceni:
- pokud uzivatel nezada hodnoty, ktere lze parsovat do typu int, tak program spadne na ValueError (myslim)
- Navrhnul bych rekurzivni input funkci ktere bude vracet sama sebe, dokud budeme mit ValueError
- Zaroven aby cilovy uzivatel nebyl zmaten, byl pridal texty do input funkci

# Teoreticke otazky
### Datove typy:
  - str - Pro textove hodnoty
  - int - celociselne hodnoty
  - float - ciselne hodnoty s desetinnou carkou
  - tuple - podobny jako list, ale pouziva se k shromazdeni spolu souvisejicich hodnot, vetsinou maji fixni delku
  - dictionary - neco ve stylu hashmap v python provedeni, ukladani key-value paru a hledani 0(1)
  - list - shluk idealne hodnot stejneho typu ( i kdyz neni potreba ), hledani O(n)
  - Prevedeni textoveho vstupu na desetinne cislo
  - float(input("Zadejte cislo s desetinnou carkou"))

### Pozadavky
  - Pro stejny vstup musi vzdy vratit stejny vystup
  - Musi mit jenom jeden zacatek
  - Srozumitelny, jasne zadani

### Vyvojovy diagram
  - odkaz https://miro.com/app/board/uXjVNPNj-28=/?share_link_id=402293758944
  - nebo obrazek diagram.jpg
