# Alkatrészlista

## Magassugárzó és keresztváltó
| Db | Jelölés | Érték / típus | Megjegyzés |
|---|---|---|---|
| 1 | — | Monacor HT-30 | 8 Ω, 98 dB, kivágás Ø59 mm |
| 1 | C1 | 2,7 µF MKP, legalább 250 V | pl. Monacor MKPA vagy Intertechnik MKT/MKP |
| 1 | L1 | 0,39 mH légmagos, legalább 0,8 mm-es huzal | egyenáramú ellenállás 0,3 Ω alatt |
| 1 | Rs | 2,2 Ω / 10 W | csak −3 dB-es padhoz |
| 1 | Rp | 18 Ω / 10 W | csak −3 dB-es padhoz |
| 1 | J-PAD | 3 tűs átkötő vagy kapcsoló | 0 / −3 dB |
| 1 | PTC | Ihold kb. 1,35 A, Itrip kb. 2,7 A, Vmax legalább 60 V | pl. Littelfuse RXEF-sorozat, a feszültségtűrést ellenőrizd az adatlapon |
| 1 | K2 | Finder 40.52, 8 A, tekercs a tápfeszültséghez | a magassugárzó ki/be kapcsolásához |
| 1 | — | csavaros sorkapocs, hangszóróvezeték (1,5 mm²) | |

## Előfok
| Db | Jelölés | Érték |
|---|---|---|
| 2 | U1, U2 | TL072 (vagy OPA2134), DIP8 foglalattal |
| 2 | R1, Rser | 1 kΩ |
| 1 | Rbias | 1 MΩ |
| 1 | Rbias alt. | 4,7 MΩ (J-IN átkötővel) |
| 2 | Rg, Rb3 | 4,7 kΩ |
| 1 | R5 | 15 kΩ |
| 1 | R6 | 27 kΩ |
| 3 | Rpg, Rb1, Rb2 | 10 kΩ |
| 1 | Rt3 | 3,3 kΩ |
| 1 | Rbleed | 100 kΩ |
| 2 | — | 47 Ω (tápszűrés) |
| 1 | C1 | 47 nF fólia |
| 2 | C3, C4 | 100 nF fólia |
| 2 | Cb1, Cb2 | 33 nF fólia |
| 3 | Ct1, Ct2, Cpg | 4,7 nF fólia |
| 1 | Cpf | 1,5 nF fólia |
| 1 | Cout | 2,2 µF fólia |
| 1 | Cg | 22 µF / 25 V elektrolit |
| 2 | Crf, Cf | 100 pF kerámia (C0G) |
| 1 | Cc | 47 pF kerámia (C0G) |
| 2 | — | 47 µF / 25 V elektrolit (tápszűrés) |
| 4 | — | 100 nF kerámia (tápszűrés, IC-nként 2) |
| 1 | P-GAIN | 47 kΩ fordított log (C) |
| 1 | P-PRES | 22 kΩ lineáris (B) |
| 2 | P-BASS, P-TREB | 100 kΩ lineáris (B) |
| 1 | P-VOL | 10 kΩ log (A) |
| 1 | S1 | 1P2T billenőkapcsoló (low-cut) |
| 1 | — | 6,3 mm-es kapcsolóérintkezős mono jackaljzat (akusztikus bemenet) |
| opc. | — | 78L15 + 79L15, ha a gyári táp ±18 V fölött van |

## Bemenetváltás
| Db | Jelölés | Érték |
|---|---|---|
| 1 | K1 | DPDT jelrelé, pl. Omron G6K-2 vagy Panasonic TQ2 |
| 2 | — | 1N4148 (visszáramú dióda) |
| 1 | — | billenőkapcsoló (Electric / Acoustic) |
| opc. | — | 6,3 mm-es jack lábkapcsolóhoz, BC337 + 4,7 kΩ + 100 µF + 10 kΩ késleltetéshez |
| 1 | — | 10 kΩ (áthallás elleni lezárás a K1 2. áramkörén) |
| — | — | árnyékolt kábel, perfboard vagy kis nyák, távtartók |
