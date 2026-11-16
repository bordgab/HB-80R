# 3. Bemenetváltás (elektromos / akusztikus)

## Elv
Egy vezérlés két relét kapcsol egyszerre:

| Relé | Feladat | Típus (példa) |
|---|---|---|
| K1 | jelváltás a reverb előtti csomópontnál | DPDT jelrelé: Omron G6K-2 vagy Panasonic TQ2 |
| K2 | a HT-30 ág be/ki | 8 A-es DPDT teljesítményrelé: Finder 40.52 |

- **Nyugalmi állapot (relé elengedve) = elektromos mód.**
  - K1 a gyári előfokot köti a reverb csomópontra.
  - K2 bontja a magassugárzó-ágat.
  - Ha a vezérlés bármiért kiesik, a combó gyári állapotban szól.
- **Meghúzott relé = akusztikus mód.**
  - K1 az új előfok kimenetét köti a csomópontra.
  - K2 bekapcsolja a HT-30-at.

K1 két áramköre:
- **1. áramkör:** a jelváltás.
- **2. áramkör:** a nem használt forrást a földre köti egy 10 kΩ-os ellenálláson keresztül. Ez csökkenti az áthallást.

## Bekötés

```
Gyári előfok kimenet ──||──(csatoló, ha eddig is volt)──┐
                                                       K1/1 NC
Reverb + dry csomópont ───────────────────────── K1/1 COM
                                                       K1/1 NO
Új előfok (Rser 1 kΩ után) ────────────────────────────┘

Végfok + ── K2 COM ;  K2 NO ── PTC ── HT-30 keresztváltó
```

- **Ha a csomópontnak egyenfeszültségű előfeszítése van** (egyoldali tápú gyári áramkör), akkor a relét a csatolókondenzátor **jel felőli** oldalára tedd. A csomópont előfeszítése így nem szakad meg.
- **K1 helye:** a betáplálási pont közvetlen közelében legyen. A gyári panelről árnyékolt kábel menjen hozzá, az árnyékolás csak az előfok felőli végén legyen földelve.
- **K2 helye:** a hangszóró-vezetékek mellett, a jelvezetékektől távol.

## Vezérlés
- **Tekercsek:**
  - A relék tekercsfeszültsége egyezzen a rendelkezésre álló tápfeszültséggel. Pl. 12 V-os tekercs +15 V-ról soros ellenállással: R = (15 − 12) / Itekercs.
  - Mindkét tekercsen 1N4148 visszáramú dióda, záróirányban, párhuzamosan.
- **Kapcsolási lehetőségek**, egyenként vagy kombinálva:
  1. **Előlapi billenőkapcsoló:** zárja a tekercsek földágát.
  2. **Lábkapcsoló:** egy 6,3 mm-es mono jacken keresztül, párhuzamosan az előlapi kapcsolóval.
  3. **Automatikus:** az akusztikus bemenet kapcsolóérintkezős jackaljzat. Bedugott kábelnél záródik a kapcsolóérintkező, és meghúznak a relék.
- **Ha egy tranzisztorral kapcsolsz** (pl. BC337, 4,7 kΩ bázisellenállás): egy 100 µF és 10 kΩ-os RC-tag a bázison késleltetést ad. Így a váltás pillanatában nem pattog, mert a jel csak a csatolókondenzátorok feltöltődése után kapcsolódik.

## Pattogásmentesség
- Mindkét forrás kondenzátorral csatolva, levezető ellenállással a föld felé (Rbleed 100 kΩ az új előfok kimenetén).
- Ha mégis pattog: rövid, 100–200 ms-os némítás a váltás alatt, pl. egy J111 JFET-tel vagy egy harmadik relével a csomópont és a föld között.

## A betáplálási pont felkutatása
1. Keresd meg a reverb modult (rugós tank vagy digitális modul, pl. Belton) és a meghajtó fokozatát.
2. Kövesd visszafelé a jelet addig a pontig, ahol a jel két ágra válik: dry (közvetlen) ág és reverb meghajtás. **Ez a betáplálási pont.** Így a reverb mindkét bemeneten működik.
3. Jelgenerátorral (1 kHz, kb. 100 mV) és oszcilloszkóppal vagy multiméterrel ellenőrizd a gyári bemenetről, hogy jól azonosítottad-e a pontot.
4. Nézd meg, van-e a pont után presence- vagy hangláda-szimulációs szűrő. Ha van, az akusztikus hangot is színezi, és a presence/magas szabályzóval kell ellensúlyozni.
5. Ha a combónak van FX Return bemenete, és a reverb a hurok **után** van, a Return pont is szóba jöhet. Ez sok erősítőben fordítva van, ezért ellenőrizni kell.

## Biztonság
- Csak áramtalanítva, kihúzott hálózati kábellel dolgozz.
- A tápkondenzátorok kikapcsolás után is töltöttek lehetnek: süsd ki őket egy kb. 1 kΩ / 5 W-os ellenállással.
- Bekapcsolás előtt ellenőrizd, hogy a végfok kimenete és a föld között ne legyen zárlat.
