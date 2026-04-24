"""
Boeing 787-9 Wärmeverlust-Rechner
Einfache Version für den Physik-Unterricht
"""

import math

print("=" * 60)
print("BOEING 787-9 WÄRMEVERLUST-RECHNER")
print("=" * 60)

# -----------------------------------------------------------
# DATEN DES FLUGZEUGS (einfach eingegeben, nicht berechnet)
# -----------------------------------------------------------
print("\n--- Flugzeugdaten ---")

# Rumpf
laenge_rumpf = 62.8          # Meter
durchmesser_rumpf = 5.77      # Meter
flaeche_rumpf = math.pi * durchmesser_rumpf * laenge_rumpf
print(f"Rumpflänge: {laenge_rumpf} m")
print(f"Rumpfdurchmesser: {durchmesser_rumpf} m")
print(f"Rumpfoberfläche: {flaeche_rumpf:.0f} m²")

# Flügel (Ober- + Unterseite)
flaeche_fluegel = 620        # m², beide Seiten
print(f"Flügeloberfläche: {flaeche_fluegel} m²")

# Leitwerk (Höhen- + Seitenleitwerk)
flaeche_leitwerk = 200       # m²
print(f"Leitwerk-Oberfläche: {flaeche_leitwerk} m²")

# Passagiere
passagiere = 290
crew = 11
personen = passagiere + crew
print(f"Passagiere: {passagiere}")
print(f"Crew: {crew}")
print(f"Gesamt Personen: {personen}")

# -----------------------------------------------------------
# TEMPERATUREN
# -----------------------------------------------------------
print("\n--- Temperaturen ---")

temp_aussen = -56.5          # °C bei 11.000m Höhe (ISA-Standard)
temp_innen = 22.0            # °C Kabinentemperatur
temp_unterschied = temp_innen - temp_aussen

print(f"Außentemperatur: {temp_aussen} °C")
print(f"Innentemperatur: {temp_innen} °C")
print(f"Unterschied: {temp_unterschied} °C")

# -----------------------------------------------------------
# U-WERTE (vorgegebene Werte, nicht selbst ausgerechnet)
# -----------------------------------------------------------
print("\n--- U-Werte (Wärmedurchgangskoeffizienten) ---")
print("Das sagt, wie gut Wärme durch die Hülle geht.")
print("Je kleiner, desto besser die Isolierung.")

u_rumpf = 0.63               # W/(m²·K) - gut isoliert
u_fluegel = 2.0              # W/(m²·K) - schlechter isoliert
u_leitwerk = 2.0             # W/(m²·K) - schlechter isoliert

print(f"U-Wert Rumpf: {u_rumpf} W/(m²·K)")
print(f"U-Wert Flügel: {u_fluegel} W/(m²·K)")
print(f"U-Wert Leitwerk: {u_leitwerk} W/(m²·K)")

# -----------------------------------------------------------
# 1. WÄRMELEITUNG DURCH DIE HÜLLE
# -----------------------------------------------------------
print("\n" + "=" * 60)
print("1. WÄRMELEITUNG DURCH DIE HÜLLE")
print("=" * 60)
print("Wärme geht durch Rumpf, Flügel und Leitwerk nach draußen.")

# Formel: Q = U * A * ΔT
# Nur 40% der Flügel/Leitwerk-Fläche sind wirklich "innen" (Rest ist Struktur)

q_rumpf = u_rumpf * flaeche_rumpf * temp_unterschied
q_fluegel = u_fluegel * flaeche_fluegel * temp_unterschied * 0.4
q_leitwerk = u_leitwerk * flaeche_leitwerk * temp_unterschied * 0.4

q_leitung_gesamt = q_rumpf + q_fluegel + q_leitwerk

print(f"\nRumpf: {q_rumpf/1000:.1f} kW")
print(f"Flügel: {q_fluegel/1000:.1f} kW")
print(f"Leitwerk: {q_leitwerk/1000:.1f} kW")
print(f"\nGESAMT (Leitung): {q_leitung_gesamt/1000:.1f} kW")

# -----------------------------------------------------------
# 2. STRAHLUNGSVERLUSTE
# -----------------------------------------------------------
print("\n" + "=" * 60)
print("2. STRAHLUNGSVERLUSTE")
print("=" * 60)
print("Die warme Außenhaut strahlt Wärme ins Weltall ab.")

# Vereinfachte Berechnung
strahlungsfluss = 14.2       # W/m² (vorgegebener Wert)
q_strahlung_rumpf = strahlungsfluss * flaeche_rumpf
q_strahlung_fluegel = strahlungsfluss * flaeche_fluegel * 0.3
q_strahlung_gesamt = q_strahlung_rumpf + q_strahlung_fluegel

print(f"Strahlungsfluss: {strahlungsfluss} W/m²")
print(f"Rumpf: {q_strahlung_rumpf/1000:.1f} kW")
print(f"Flügel: {q_strahlung_fluegel/1000:.1f} kW")
print(f"\nGESAMT (Strahlung): {q_strahlung_gesamt/1000:.1f} kW")

# -----------------------------------------------------------
# 3. LUFTAUSTAUSCH (VENTILATION)
# -----------------------------------------------------------
print("\n" + "=" * 60)
print("3. LUFTAUSTAUSCH (FRISCHLUFT)")
print("=" * 60)
print("Kalte Luft von draußen muss aufgeheizt werden.")

# ACH = Air Changes per Hour = Luftwechsel pro Stunde
# Das sagt, wie oft die Kabinenluft komplett ausgetauscht wird
ach = 15                     # 15 Mal pro Stunde
print(f"Luftwechselrate (ACH): {ach} /h")
print("(= die Kabinenluft wird 15 Mal pro Stunde erneuert)")

# Kabinenvolumen
volumen_kabine = math.pi * (5.49/2)**2 * laenge_rumpf * 0.75
print(f"Kabinenvolumen: {volumen_kabine:.0f} m³")

# Massenstrom der Luft
luftdichte_aussen = 0.364    # kg/m³ bei 11.000m
volumenstrom = ach * volumen_kabine / 3600  # m³/s
massenstrom = volumenstrom * luftdichte_aussen

print(f"Volumenstrom: {volumenstrom:.2f} m³/s")
print(f"Massenstrom: {massenstrom:.2f} kg/s")

# Wärmeleistung für die Frischluft
cp_luft = 1005               # J/(kg·K) - spezifische Wärmekapazität
q_ventilation = massenstrom * cp_luft * temp_unterschied

print(f"\nGESAMT (Ventilation): {q_ventilation/1000:.1f} kW")

# -----------------------------------------------------------
# 4. GESAMTERGEBNIS
# -----------------------------------------------------------
print("\n" + "=" * 60)
print("4. GESAMTERGEBNIS")
print("=" * 60)

q_gesamt = q_leitung_gesamt + q_strahlung_gesamt + q_ventilation

print(f"\n{'Posten':<35} {'kW':>10}")
print("-" * 48)
print(f"{'Wärmeleitung durch Hülle':<35} {q_leitung_gesamt/1000:>9.1f}")
print(f"{'Strahlungsverluste':<35} {q_strahlung_gesamt/1000:>9.1f}")
print(f"{'Luftaustausch (Ventilation)':<35} {q_ventilation/1000:>9.1f}")
print("-" * 48)
print(f"{'BRUTTO-WÄRMEVERLUSTE':<35} {q_gesamt/1000:>9.1f}")

# -----------------------------------------------------------
# 5. INTERNE WÄRME (was man abziehen kann)
# -----------------------------------------------------------
print("\n" + "=" * 60)
print("5. INTERNE WÄRMEQUELLEN")
print("=" * 60)
print("Menschen und Geräte erzeugen auch Wärme.")

waerme_pro_person = 90       # W
q_personen = personen * waerme_pro_person
q_elektronik = 30000         # W (30 kW)

q_intern = q_personen + q_elektronik

print(f"Personen: {personen} × {waerme_pro_person} W = {q_personen/1000:.1f} kW")
print(f"Elektronik/Galleys: {q_elektronik/1000:.1f} kW")
print(f"\nInterne Wärme: {q_intern/1000:.1f} kW")

q_netto = q_gesamt - q_intern
print(f"\nNETTO-WÄRMEVERLUST: {q_netto/1000:.1f} kW")
print("(= das muss das Klimasystem wirklich nachheizen)")

# -----------------------------------------------------------
# 6. VERGLEICH MIT TRIEBWERK
# -----------------------------------------------------------
print("\n" + "=" * 60)
print("6. VERGLEICH")
print("=" * 60)

leistung_triebwerk = 2 * 70000  # 2 Triebwerke à 70 MW
print(f"Triebwerksleistung: {leistung_triebwerk/1000:.0f} kW")
print(f"Wärmeverluste: {q_gesamt/1000:.0f} kW")

anteil = (q_gesamt / leistung_triebwerk) * 100
print(f"\nAnteil: {anteil:.2f} %")
print("(Die Wärmeverluste sind fast nichts gegen die Triebwerksleistung)")

print("\n" + "=" * 60)
print("FERTIG")
print("=" * 60)