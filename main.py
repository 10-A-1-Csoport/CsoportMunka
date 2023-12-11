vezeteknev = input("Add meg a vezetéknevedet: ")
keresztnev = input("Add meg a keresztnevedet: ")

print(f"{vezeteknev} {keresztnev} üdvözöllek.")

szam = input("Adj meg egy számot: ")
szamAtvezetes = int(szam)
szamElozo = szamAtvezetes - 1
SzamUtana = szamAtvezetes + 1
print(f"Előtte lévő szám: {szamElozo}, következő szám: {SzamUtana}")

elsoSzam = input("Adj meg egy számot: ")
masodikSzam = input("Adj meg egy második számot: ")

elsoSzamAtvezetes = int(elsoSzam)
masodikSzamAtvezetes = int(masodikSzam)

szamOsszege = elsoSzamAtvezetes + masodikSzamAtvezetes
szamKulonbseg = elsoSzamAtvezetes - masodikSzamAtvezetes
szamSzorzata = elsoSzamAtvezetes * masodikSzamAtvezetes
szamHanyadosa = elsoSzamAtvezetes / masodikSzamAtvezetes

print(f"A két szám összege: {szamOsszege}")
print(f"A két szám különbsége: {szamKulonbseg}")
print(f"A két szám szorzata: {szamSzorzata}")
print(f"A két szám különbsége: {szamKulonbseg}")

aValtozo = input("Add meg az első változó értékét: ")
bValtozo = input("Add meg a második változó értékét: ")