Domáca úloha 1
==============

Domácu úlohu odovzdávajte do Štvrtku 27.3. 9:55 (t.j. najneskôr
na začiatku prednášky).

Úlohu odovzdávajte buď fyzicky na papier formátu A4 (čitateľne označenom a
podpísanom) na prednáške alebo na cvičeniach, alebo elektronicky vo formáte PDF
(ako súbor `du01.pdf`) alebo ako obyčjaný textový súbor (`du01.txt`)
do vetvy `du01`.  Môžete odovzdať aj oskenované/odfotené
papierové verzie ako súbor `du01.jpg` alebo `du01.png`, ak sú dostatočne čitateľné
(dostatočné rozlíšenie, kontrast, v oskenovanej verzii sa škaredé písmo trochu
ťažšie lúšti,...). Nezabudnite vyrobiť pull request.

Bohužiaľ cez webové rozhranie sa na github dajú súbory len priamo písať alebo
copy-paste-ovať, binárne súbory treba nahrať pomocou
GIT-u ([msysgit](http://msysgit.github.io/) alebo čistý [git](http://git-scm.com/downloads))
alebo [github programu pre windows](http://windows.github.com/)
respektíve pre [Mac](http://mac.github.com/).

Github pre windows/mac je vcelku jednoduchý: stačí nainštalovať, zadať meno a heslo,
naklonovať svoj repozitár, prepnúť správnu vetvu, nahrať do správnych adresárov súbory,
commit-núť a nahrať na server (v tomto programe to volaju "sync/synchronize branch").
Samozrejme potom treba ešte (cez webová rozhranie) vyrobiť pull request.

## 1.1 (1b)

[Shefferova spojka (NAND)](http://en.wikipedia.org/wiki/Sheffer_stroke)
, značka: `↑`, je binárna logická spojka s nasledovným významom:
* `A ↑ B` je pravdivé vtt keď aspoň jedno z `A`  alebo `B` je nepravdivé.

Vybudujte teóriu výrokovel logiky používajúcej **iba** túto spojku: zadefinujte pojem
formuly, vytvárajúcej postupnosti a stromu pre formulu, boolovského ohodnotenia.

## 1.2 (1b)

Hovríme, že binárna logická spojka <code>&loz;</code> je **definovateľná** zo spojok
<code>&alpha;</code>, <code>&beta;</code>... ak existuje formula, obsahujúca iba
spojky <code>&alpha;</code>, <code>&beta;</code>,... a premenné `a` a `b`, ekvivalentná
formule <code>(a &loz; b)</code>.

Hovríme, že unárna logická spojka <code>&loz;</code> je **definovateľná** zo spojok
<code>&alpha;</code>, <code>&beta;</code>... ak existuje formula, obsahujúca iba
spojky <code>&alpha;</code>, <code>&beta;</code>,... a premennú `a`, ekvivalentná
formule <code>&loz; a</code>.

Napríklad <code>&rarr;</code> je definovateľná z <code>&not;</code> a <code>&or;</code> pretože
<code>(a&rarr;b)</code> je  ekvivalentná s <code>(&not;a&or;b)</code> (samozrejme ekvivalenciu
tých dvoch formúl by bolo treba ešte dokázať).

Dokážte, že
  * `↑` je definovateľná zo spojok <code>&not;</code>, <code>&and;</code> a <code>&or;</code>;
  * <code>&not;</code>, <code>&and;</code>, <code>&or;</code>, <code>&rarr;</code> sú definovateľné
    z `↑`.

## 1.3 (1b)

Uvažujme naslednovnú definíciu:

Formula `X` je symetrická v `a` a `b`, kde `a` a `b` sú premenné,  vtt keď pre každé boolovské ohodnotenie `v` platí:
nech `v'` je boolovské ohodnotenie také, že
    * `v'(a) = v(b)`;
    * `v'(b) = v(a)`;
    * `v'(x) = v(x)` pre ostatné premenné rôzne od `a` a `b`,
potom `v(X) = v'(X)`.

Dokážte,  že:
* ak `X` neobsahuje ani `a` ani `b`, tak je symetrická v `a` a `b`
* ak `X` je symetrická v `a` a `b`, tak je symetrická v `b` a `a`
* ak `X` nie je symetrická v `a` a `b`, tak `X` nie je tautológia

