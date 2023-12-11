#1
vezeteknev = input("Add meg a vezetékneved: ")
keresztnev = input("Add meg a keresztneved: ")

print(f"A te teljes neved: {vezeteknev} {keresztnev}")
#2
szam = int(input("Add meg a számot: "))

elozo_szam = szam - 1
kovetkezo_szam = szam + 1

print(f"A(z) {szam} szám előzője: {elozo_szam}")
print(f"A(z) {szam} szám rákövetkezője: {kovetkezo_szam}")
#3
szam1 = float(input("Add meg az első számot: "))
szam2 = float(input("Add meg a második számot: "))


osszeg = szam1 + szam2
kulonbseg = szam1 - szam2
szorzat = szam1 * szam2


if szam2 != 0:
    hanyados = szam1 / szam2
    print(f"Az osztás eredménye: {hanyados}")
else:
    print("Nullával nem lehet osztani!")


print(f"Az összeg: {osszeg}")
print(f"A különbség: {kulonbseg}")
print(f"A szorzat: {szorzat}")