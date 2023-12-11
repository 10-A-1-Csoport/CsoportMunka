szam1 = input("Adj egy számot: ")
szam1 = int(szam1)
szam2 = input("Adj egy másik számot: ")
szam2 = int(szam2)

print("Az összege:", szam1 + szam2)
print("A különbsége:", szam1 - szam2)
print("A szorzata:", szam1 * szam2)

if szam2 != 0:
    print("A hányadosuk:", szam1 / szam2)
else:
    print("A hányadosukat nem értelmezzük, mert a második szám nulla.")