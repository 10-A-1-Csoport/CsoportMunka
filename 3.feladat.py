szam1 = input("Adj meg egy számot: ")
szam1 = int(szam1)
szam2 = input("Adj meg egy másik számot: ")
szam2 = int(szam2)

print("Az összegük:", szam1 + szam2)
print("A különbségük:", szam1 - szam2)
print("A szorzatuk:", szam1 * szam2)

if szam2 != 0:
    print("A hányadosuk:", szam1 / szam2)
else:
    print("A hányadosukat nem értelmezzük, mert a második szám nulla.")
