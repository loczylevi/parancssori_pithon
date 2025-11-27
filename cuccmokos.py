


import sys

class Megallok:
    def __init__(self,megallo):
        self.megallo = megallo
        
        
def beolvaso(fajl):
    lista = []
    try:
        with open(fajl,"rt", encoding="UTF-8") as f:
            for sor in f:
                s = sor.rstrip("\n")
                lista.append(Megallok(s))
        return lista   
    except:
        sys.stderr.write('Nem letezik a fájl tesó :(\n')
        return []
        
def atszallas(egyik,masik):
    try:
        egy = {s.megallo for s in beolvaso(egyik)}
        ketto = {s.megallo for s in beolvaso(masik)}
        x = (egy & ketto)
        if len(x)>0:
            return x
        else:
            return None
        
    except:
        sys.stderr.write("Valami nem jó gec11\n")
        return []
        
"""
Alakítsd át a programot egy teljes parancssori alkalmazássá,
amelynek két paramétere van ami a metrómegállók neveit tartalmazza!
Ehhez szükséged lesz a parancssori paraméterek kezelésére.
"""
import sys

def main():
    # Ellenőrizzük, hogy pontosan 2 paraméter van-e
    if len(sys.argv) == 3:
        f1 = sys.argv[1]  # 1. fájl neve
        f2 = sys.argv[2]  # 2. fájl neve

        # Fájlok beolvasása
        be_f1 = beolvaso(f1)
        be_f2 = beolvaso(f2)

        # Kiírjuk az első fájl megállóit
        print(f"A {f1} megállói:")
        print("___________________________________________________\n")
        for sor in be_f1:
            print(sor.megallo)

        # Kiírjuk a második fájl megállóit
        print(f"A {f2} megállói:")
        print("___________________________________________________\n")
        for sor in be_f2:
            print(sor.megallo)

        # Megkeressük a közös megállókat
        x = atszallas(f1,f2)
        print("\nKözös megálló:")
        print("___________________________________________________\n")
        if isinstance(x, set):
            for xd in x:
                print(xd)
            print()
    else:
        # Hibakezelés: nem megfelelő paraméterszám
        sys.stderr.write(
            "Használat: python3 cuccmokos.py m1.txt m2.txt\n"
            "Először a fájl neve, utána space-el elválasztva két db szöveges fájl\n"
        )
        sys.exit(1)

main()

            

