# HB-80R akusztikus átalakítás

Tervdokumentáció egy **Harley Benton HB-80R** gitárkombó átalakításához, hogy elektroakusztikus gitárral is jó hangot adjon:

- **Monacor HT-30** magassugárzó a Celestion Seventy 80 mellé, másodrendű keresztváltóval, átkötős paddel és PTC-s védelemmel;
- **2 × TL072** akusztikus előfok: nagy impedanciájú buffer, 80 Hz-es low-cut, presence, Baxandall basszus/magas. A gyári előfokot kikerülve a reverb elé csatlakozik;
- **Relés bemenetváltás**: egy kapcsoló választ a gyári és az akusztikus előfok között, és ugyanez kapcsolja ki-be a magassugárzót.

```
Elektromos ─ gyári előfok ──┐
                            K1 ─ reverb/dry ─ végfok ─┬─ Seventy 80
Akusztikus ─ TL072 előfok ──┘                         └─ K2 ─ PTC ─ felüláteresztő ─ pad ─ HT-30
```

## Dokumentáció
1. [Magassugárzó és keresztváltó](docs/01-magassugarzo-keresztvalto.md)
2. [Akusztikus előfok](docs/02-eloerosito.md)
3. [Bemenetváltás](docs/03-bemenetvaltas.md)
4. [Alkatrészlista](docs/bom.md)

## Szimuláció
A `sim/` mappában ngspice netlisták vannak (`crossover.cir`, `preamp.cir`). A `plot.py` több potméter-állással lefuttatja őket, és a `docs/img/` mappába rajzolja a görbéket.

```bash
sudo apt install ngspice          # vagy: brew install ngspice
pip install numpy matplotlib
python3 sim/plot.py
```

A hangszórómodellek becsült paraméterekkel dolgoznak. A görbék a tervezést segítik, a végleges hangolást (polaritás, pad, presence) hallásra vagy méréssel kell elvégezni.

## Biztonság
A combóban hálózati feszültség és nagy töltésű kondenzátorok vannak. Csak áramtalanítva dolgozz, és bekapcsolás előtt süsd ki a tápkondenzátorokat. Az átalakítás a garanciát megszünteti.
