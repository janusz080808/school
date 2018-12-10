print("program obliczajacy wynik dzielenia")
dzielna = float(input("podaj dzielna")) 
dzielnik = float(input("podaj dzielnik"))
dana = 0
while dzielnik == dana:
    print("nie mozna dzielic przez", dana,".")
    dzielnik = float(input("podaj dzielnik jeszcze raz:" ))
wynik = (dzielna/dzielnik,)
reszta = (dzielna % dzielnik)
reszta1 = (dzielna - reszta) / dzielnik
print("wynik to:", wynik, "a wynik z reszta to", reszta1, "i", reszta)
   
