Cvičenie 5
==========

**Riešenie odovzdávajte podľa
[pokynov na konci tohoto zadania](#technické-detaily-riešenia)
do Nedele 30.3.  23:59:59.**

Súbory potrebné pre toto cvičenie si môžete stiahnúť ako jeden zip
[`cv05.zip`](https://github.com/FMFI-UK-1-AIN-411-2014/udvl/archive/cv05.zip).

CNF (4b)
--------
Triedy, ktoré sme vyrobili v cvičení 3, nie sú z viacerých dôvodov
veľmi vhodné na reprezentáciu formúl v CNF:
- kedykoľvek by sme očakávali formulu v CNF tvare,  museli by sme vždy
  kontrolovať, či naozaj má správny tvar
- je trošku neefektívna ( `Negation(Variable("x"))`) a ťažkopádnejšia
  na použite (musíme ziťovať akého typu je podformula v Disjunction atď)
- chceme pridať niekoľko metód, ktoré majú zmysel len pre CNF formulu

Najefektívnejší (čo sa veľkosti a rýchlosti kódu týka) spôsob by bol
reprezentovať CNF formulu jednoducho ako pole (list) kláuz, pričom každá
klauza by bola pole dvojíc: meno a boolovský flag hovoriaci, či je negovaná.
Operácie s nimi by ale potom nemohli byť implementované ako ich metódy. Aby
sme dosiahli obidve výhody, spravíme to tak, že prvé dve triedy oddedíme od
poľa (list-u) a pridámu im navyše potrebné metódy.

Implementujte triedy `Cnf`, `CnfClause` a `CnfLit` s nasledovnými metódami:

```
class VariableMap:
    constructor(Array of String variables)
    VariableMap addVar(String var) // vrati referenciu na seba, aby sa dala 'chainovat'
    int get(String var) // vrati cislo priradene var
    int operator[](String var)  // vrati cislo priradene var,
                                //tj  map['a'] == 10,  __getitem__ v pythone
    String toString() // vrati nejaku textovu reprezentaciu mapy

    Array of String keys() // zoznam premennych v mape
    Map<int,String) reverse()

    writeToFile(OutputFile outFile)
    static VariableMap readFromFile(InputFile inFile)

class CnfLit:
    String name
    bool neg

    constructor(String name) // vyrobi kladny (nenegovany) literal
    static CnfLit Not(String name) // vyrobi CnfLit s neg==true
    CnfLit operator-() // vrati novu CnfLit, ktora je negaciou tejto

    String toString()
    bool eval(Interpretation i)

    extendVarMap(VariableMap map)
    writeToFile(OutputFile outFile, VariableMap varMap)

class CnfClause(Array of CnfLit):
    constructor(Array of CnfLit vars)

    String toString()
    bool eval(Interpretation i)

    extendVarMap(VariableMap map)

    writeToFile(OutputFile outFile, VariableMap varMap)
    static CnfClause readFromFile(InputFile inFile, VariableMap varMap)

class Cnf(Array of CnfClause):
    constructor(Array of CnfClause clauses)

    String toString()
    bool eval(Interpretation i)

    extendVarMap(VariableMap map)

    writeToFile(OutputFile outFile, VariableMap varMap)
    static Cnf readFromFile(InputFile inFile, VariableMap varMap)
```

Podrobnejší popis v c++ formáte si môžete pozrieť v súbore [`cnf.h`](cnf.h).

Metódy `toString` a `eval` majú fungovať podobne ako v cvičení 3 na obyčajných
formulách. Formát `toString` je nasledovný:
- `CnfLit`:  meno premennej ak nie je negovaná, "-" a meno premennej, ak je
  negovaná,
- `CnfClause`: reprezentácie jednotlivých premenných oddelené
  medzerami,
- `Cnf`: reprezentácie jednotlivých klauz s "\n" za každou klauzou (aj poslednou).

Trieda `VariableMap` slúži na reprezentáciu mapovania mien premenných na
čísla.  Metóda `addVar` pridá novú premennú (ak sa zavolá s premennou, ktorá
už v mape je, nič sa nestane) a vráti referenciu na seba, aby sa dala
používať štýlom `varMap = VariableMap().addVar('a').addVar('b')`.

K číslam premenných sa pristupuje pomocou operátora `[]` podobne ako v
skutočnej mape / slovníku (t.j. `numeric = varMap['a']`). Metóda `toString`
vráti nejakú textovú reprezentáciu. Nezáleží na presnom formáte, je to
hlavne pre debugovacie účely, jediná podmienka je, že pre rôzne mapovania
vráti rôzne reťazce.

Metóda `reverse` vráti (ako obyčajnú mapu / slovník z čísel na reťazce)
opačné mapovanie (potrebné napríklad pri načítavaní CNF).

Metódy `writeToFile` a `readFromFile` zapíšu mapdu do / načítajú ju zo
súboru. Formát nie je špecifikovaný, dôležité je, aby sme po zapísaní a
následnom načítaní dostali rovnakú mapu.

Pre Cnf triedy zapíše `writeToFile` celú CNF formulu (alebo iba príslušnú
klauzu alebo premennú) do súboru `outFile` v DIMACS formáte, pričom premenné
zakóduje pomoc `varMap`. Každá klauza by sa mala zapísať na jeden samostatný
riadok.

Metóda `readFromFile` načíta CNF formulu (alebo iba jednu klauzu v prípade
CnfClause, vhodné napríklad pri čítaní riešenia zo SAT solvera) zo súboru
inFile. Môžete predpokladať, že každá klauza je na jednom samostatnom
riadku. Premenné sa dekódujú pomocou varMap (pozor, je to map z mien na
čísla, tj opačným smerom). Ak sa nedá načítať korektná formula / klauza,
funkcia by mala vyhodiť výnimku (`IOError` v pythone, podľa uváženia v
iných jazykoch).

Metóda `extendVarMap` rozšíri vstupnú mapu startMap o všetky potrebné
premenné, ktoré sa vyskytujú vo formuly (klauze) a ešte ich neobsahuje.

## Technické detaily riešenia

Riešenie odovzdajte do vetvy `cv05` v adresári `cv05`.  Odovzdávajte súbor
`cnf.h`/`cnf.cpp`, `cnf.py`, alebo `Cnf.java`.

Odovzdávanie riešení v iných jazykoch konzultujte s cvičiacimi.

### Python
Program [`cv05test.py`](cv05test.py) musí korektne zbehnúť s vašou knižnicou
(súborom `cnf.py`, ktorý odovzdáte).

`Cnf` a `CnfClause` majú byť oddedené od vstavanej triedy `list`, čím
získajú všetky jej metódy a vlastnosti (indexovanie cez `[]`,
`appednd`,...). `list` má konštruktor s jedným argumentom: zoznamom, ktorého
prvky sa stanú jeho počiatočným obsahom.

`CnfLit` musí implementovať unárny operátor `-` (metódu `__neg__`), ktorý
vráti negovaný `CnfLit`.

`VariableMap` musí implementovať operátor `[]`(metódu `__getitem__`) na
prístup k číslam premenných.`

`InputFile` a `OutFile` budú [objekty typu File](http://docs.python.org/2/library/stdtypes.html#file-objects)
([python 3](http://docs.python.org/3/library/io.html#module-io)), to
znamená, že na nich môžete volať metódy `write`, `readline` (prípadne `for
line in inFile`)

`Interpretation` bude podobne ako v cvičení 3 slovník z reťazcov na bool:
`{ 'a': True, 'b': False }`.



### C++
Súbor `cnf.h` obsahuje deklarácie tried, ktoré máte implementovať v súbore
`cnf.cpp`. Možete si do neho doplniť ďalšie deklarácie (premenné, pomocné
funkcie), ale test musí ísť stále skompilovať a spustiť.

Odovzdajte súbor `cnf.cpp` obsahujúci implementáciu, prípadne aj `cnf.h` ak
ste ho menili.

Program [`cv05test.cpp`](cv05test.cpp) musí byť skompilovateľný keď k nemu
priložíte vašu knižnicu (súbory `cnf.h`/`cnf.cpp`, ktoré odovzdáte).

POZOR: cv05test.cpp netestuje všetku funkcionalitu! bohužiaľ
sa nám z časových dôvodov neoplatilo ich vyrábať.

`Cnf` a `CnfClause` majú spĺňať podmienky pre
[`ReversibleContainer`](http://en.cppreference.com/w/cpp/concept/ReversibleContainer)
s
[`RandomAccessIterator`-om](http://en.cppreference.com/w/cpp/concept/RandomAccessIterator).
Túto magickú podmienku najjednoduchšie splníte tak, že vaše triedy oddedíte
od `std::vector<CnfClause>` a `std::vector<CnfLit>`.

`CnfLit` musí implementovať unárny `CnfLit CnfLit::operator-()`.

`VariableMap` musí implementovať `int VariableMap::operator[](std::string)`
(plus ostatné metódy).

`InputFile` a `OutFile` budú (referncie na) `std::istream` a `std::ostream`

`Interpretation` bude rovnaká ako v cvičení 3:
```c++
typedef std::map<std::string, bool> Interpretation;
```

### Java
Odovzdávajte súbor `Cnf.java`, ktorý obsahuje potrebné triedy (bohužiaľ testy
sa nám z časových dôvodov neoplatilo vyrábať).

Triedy emulujúce zoznamy musia implementovať interface `Iterable<E>` a
`List<E>`. Najjednoduchší spôsob ako to dosiahnuť je oddediť vašu triedu od
[`AbstractList<E>`](http://docs.oracle.com/javase/7/docs/api/java/util/AbstractList.html)
a implementovať metódy `get(int)`, `size()`, `set(int, E)`, `add(int, E)` a
`remove(int)`. Triedy samozrejme majú mať konštruktor, ktorý akceptuje pole
podelementov.
