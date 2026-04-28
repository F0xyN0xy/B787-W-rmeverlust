# Boeing 787-9 Wärmeverlust-Rechner

Ein einfaches Python-Programm, das berechnet, wie viel Wärme ein Boeing 787-9 Dreamliner im Reiseflug verliert.

## Was macht das Programm?

Es rechnet aus, wie viel Heizleistung das Flugzeug braucht, damit es in 11.000 Metern Höhe (wo es −56,5 °C ist) trotzdem 22 °C warm in der Kabine ist.

## Wie startet man es?

1. Python installieren (python.org)
2. Die Datei `b787_waermeverlust.py` speichern
3. Im Terminal / Command Prompt eingeben:
   ```
   python b787_waermeverlust.py
   ```

## Was bedeuten die Abkürzungen?

| Abkürzung | Bedeutung | Erklärung |
|:---|:---|:---|
| **U-Wert** | Wärmedurchgangskoeffizient | Sagt, wie gut Wärme durch eine Wand geht. Klein = gut isoliert. |
| **ACH** | Air Changes per Hour | Wie oft die Luft in der Kabine pro Stunde komplett ausgetauscht wird. |
| **Q_Leit** | Wärmeleitung | Wärme, die einfach durch den Rumpf, Flügel und Leitwerk nach draußen geht. |
| **Q_Strahl** | Strahlung | Wärme, die die warme Außenhaut als Infrarot-Strahlung ins Weltall abgibt. |
| **Q_Vent** | Ventilation | Kalte Außenluft wird reingepumpt und muss aufgeheizt werden. |
| **kW** | Kilowatt | Einheit für Leistung. 1 kW = 1000 Watt. |
| **ISA** | International Standard Atmosphere | Ein Standard-Modell für Temperatur und Druck in der Atmosphäre. |
| **CFRP** | Carbonfaser-Verbund | Das Material, aus dem der Rumpf der 787 besteht. |

## Ergebnis

Das Programm gibt am Ende drei Hauptwerte aus:

1. **Wärmeleitung durch Hülle** (~98 kW) — Wärme geht durch die Wände
2. **Strahlungsverluste** (~19 kW) — Wärme strahlt weg
3. **Luftaustausch** (~133 kW) — Kalte Frischluft muss erwärmt werden

**Gesamt:** ca. **250 kW** Brutto-Verluste

Abzüglich der Wärme von Passagieren und Elektronik bleiben ca. **190 kW** Netto-Heizlast übrig.

## Vergleich

Die beiden Triebwerke produzieren zusammen ca. **140.000 kW** Leistung. Die Heizleistung von 250 kW ist also nur **0,18 %** davon — fast nichts.

## Datenquellen

- Boeing 787-9 Technische Daten (Länge, Durchmesser, Flügelfläche)
- ISA-Atmosphäre (Temperatur in 11.000 m: −56,5 °C)
- Typische U-Werte für Verkehrsflugzeuge
- Luftwechselrate für Flugzeugkabinen

---


# Quellen

-[Wikipedia](https://en.wikipedia.org/wiki/Boeing_787_Dreamliner)

-[Nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7152029/?sharetype=link)

-[ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0360132317304274?sharetype=link)

-[Boeing](https://www.boeing.com/commercial/787/by-design?sharetype=link)