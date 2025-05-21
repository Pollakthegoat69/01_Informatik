from temperatur import celcius_to_fahrenheit, celcius_to_kelvin

celcius = float (input("Gben sie die aktuelle Temperratur ein:"))
fahrenheit = celcius_to_fahrenheit(celcius)
kelvin = celcius_to_kelvin(celcius)

print(f"Die Temperatur in Fahrenheit ist {fahrenheit}, die Temperatur in Kelvin ist {kelvin}")



