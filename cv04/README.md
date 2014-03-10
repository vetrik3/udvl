Cvičenie 4
==========

**Riešenie odovzdávajte podľa
[pokynov na konci tohoto zadania](#technické-detaily-riešenia)
do Nedele 23.3.  23:59:59.**

## Sudoku (4b)

Implementujte triedu `SudokuSolver` ktorá pomocou SAT solvera rieši sudoku.

Trieda musí mať metódu `solve`, ktorá ako jediný parameter dostane vstupné sudoku:
dvojrozmerné pole 9x9 čísel od 0 až 9, kde 0 znamená prázdne políčko. Metóda vráti ako výsledok
dvojrozmerné pole 9x9 čísel od 1 po 9 reprezentujúce (jedno možné) riešenie vstupného sudoku.

Ak zadanie sudoku nemá riešenie, metóda `solve` vráti dvojrozmerné pole obsahujúce samé nuly.

Sudoku:

* štvorcová hracia plocha rozmerov 9x9 rozdelená na 9 podoblastí rozmerov 3x3
* cieľom je do každého políčka vpísať jednu z číslic 1 až 9

pričom musíme rešpektovať obmedzenia:

* v stĺpci sa nesmú číslice opakovať
* v riadku sa nesmú číslice opakovať
* v každej podoblasti 3x3 sa nesmú číslice opakovať

*Pomôcka*: Pomocou výrokovologickej premennej <code>s\_i\_j\_n</code> (<code>0
&le; i,j &le; 8</code>, <code>1 &le; n &le; 9</code>) môžeme zakódovať, že na
súradniciach <code>[i,j]</code> je vpísané číslo <code>n</code>.

*Pomôcka 2*: Samozrejme potrebuje zakódovať, že na každej pozícii má byť práve
jedno číslo (t.j. že tam bude aspoň jedno a že tam nebudú dve rôzne).

*Pomôcka 3*: Podmienky nedovoľujúce opakovanie číslic môžeme zapísať vo forme
implikácií: <code>s\_i\_j\_n -> -s\_k\_l\_n</code> pre vhodné indexy
<code>i,j,k,l</code>.  (spomeňte si, ako sme riešili problém N-dám)


*Pomôcka 4*: Pre SAT solver musíme výrokovologické premenné <code>s\_i\_j\_n</code>
zakódovať na čísla (od 1). <code>s\_i\_j\_n</code> môžeme zakódovať ako číslo
<code>9 * 9 * i + 9 * j + n</code>, kde <code>0 &le; i,j &le; 8</code> a
<code>1 &le; n &le; 9</code>.

*Pomôcka 5*: Opačná transformácia, teda SAT solver nám dá číslo <code>x</code>
a chceme vedieť pre aké <code>i, j, n</code> platí <code>x = s\_i\_j\_n</code>
(napríklad 728 je kód pre <code>s\_8\_8\_8</code>): keby sme nemali <code>n</code>
od 1, ale od 0 (teda rovnako ako súradnice), bolo by to vlastne to isté ako
zistiť cifry čísla <code>x</code> v deviatkovej sústave. Keďže <n> je od 1, ale
je na mieste 'jednotiek' (tj <code>n * 9<sup>0</sup></code>), stačí nám pred
celou operáciou od neho odčítať jedna (a potom zase pripočítať 1 k n).



## Technické detaily riešenia

Riešenie odovzdajte do vetvy `cv04` v adresári `cv04`.

Všetky ukážkové a testovacie súbory k tomuto cvičeniu si môžete stiahnuť
ako jeden zip súbor
[cv04.zip](https://github.com/FMFI-UK-1-AIN-411-2014/udvl/archive/cv04.zip).

V priečinku [examples/sat](../examples/sat) môžete nájsť knižnicu s dvoma
pomocnými triedami `DimacsWriter` a `SatSolver`, ktoré vám môžu uľahčiť prácu
so SAT solverom. Príklad ich použitia (a čiastočne aj vzorové riešenie cvičenia
2) možete nájsť v priečinku [examples/nqueens](../examples/nqueens/).

### Python
Odovzdajte súbor `sudoku.py` v ktorom je implementovaná trieda `SudokuSolver`
obsahujúca metódu `solve`. Metóda `solve` má jediný argument: dvojrozmernú
maticu čísel (zoznam zoznamov čísel) a vracia rovnako dvojrozmernú maticu
čísel.

Program [`cv04test.py`](cv04test.py) musí korektne zbehnúť s vašou knižnicou
(súborom `formula.py`, ktorý odovzdáte).

Ak chcete použiť knižnicu z [examples/sat](../examples/sat), nemusíte si ju
kopírovať do aktuálne adresára, stačí ak na začiatok svojej knižnice pridáte
```python
import sys
sys.path[0:0] = [os.path.join(sys.path[0], '../examples/sat')]
```

### C++
Odovzdajte súbory `sudoku.h` a `sudoku.cpp` obsahujúce triedu `SudokuSolver`
ktorá implementuje interface `AbstractSudokuSolver` z `AbstractSudokuSolver.h`.

Program [`cv04test.cpp`](cv04test.cpp) musí byť skompilovateľný keď k nemu
priložíte vašu knižnicu (súbory `sudoku.h`/`sudoku.cpp`, ktoré odovzdáte).

###Java:
Odovzdajte súbory `SudokuSolver.java` obsahujúce triedu `SudokuSolver` ktorá
implementuje interface `AbstractSudokuSolver` z `AbstractSudokuSolver.java`.

Program [`Cv04Test.java`](Cv04Test.java) musí byť skompilovateľný, keď sa k
nemu priloží vaša knižnica.
