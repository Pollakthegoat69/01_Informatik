def eingabe_der_werte():
    print("gib die Raummaße ein")
    Länge = int(input ("Länge in mm: "))
    Breite = int(input ("Breite in mm: "))
    Höhe = int(input ("Höhe in mm: "))
    Temp_außen = int(input ("Außentemperatur in °C: "))
    Temp_innen = int(input ("Innentemperatur in °C: "))

    volumen = Länge * Breite * Höhe
    dT = Temp_innen - Temp_außen

volumen, dT = eingabe_der_werte()
if dT < 0:
    print(f"Die Innentemperatur ist niedriger als {dT} < 0")

Heizlast= volumen * dT * 0.024
print("Die Heizlast beträgt: {Heizlast}kW")
