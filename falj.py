"""
Beolvassa a fájl szavait egy listába. Ügyelj arra, hogy ne legyen sorvége jel
a szavak végén! Legyen ez a betoltes() nevű függvény, amelynek paramétere a
fájlnév, visszatérési értéke a szavak listája! Ellenőrizd a szavak számát,
és magukat a szavakat is a beolvasás után!
"""
import sys

def betoltes(faljnev):
    lista = []
    try:
        with open(faljnev, "rt", encoding="UTF-8") as f:
            for sor in f:
                sor = sor.rstrip("\n")
                lista.append(sor)
                
        return lista
    except:
        sys.stderr.write("Nincs ilyen fálj komámuram, nyaljalak meg!\n")
        return []
        
            
#print(betoltes("szavak_50.txt"))
#tomb = betoltes("szavak_50.txt")
#print(len(tomb))


#Rendezd sorba a listát a beépített rendező függvénnyel, sorted() vagy.sort().

#tomb.sort()
#print(tomb)

"""
Írd ki egy másik fájlba csak a k betűvel kezdődő szavakat!
Legyen ennek a neve szavak_kbetus.txt, és legyen ugyanolyan a formátuma,
soronként egy darab szó! Ellenőrizd a keletkező fájlt, pl. jegyzettömbbel!
A fájlba írást végezze a mentes() nevű függvény, amelynek paraméterben
lehet megadni a fájlnevet és a mentendő listát!
"""

def mentes(falj, bemenet):
    if isinstance(bemenet, list) and len(bemenet) > 0:
        with open(falj,"wt", encoding="UTF-8") as f:
            for sor in bemenet:
                if sor[0].lower() == "k":
                    print(sor,file=f)
    else:
        sys.stderr.write("Valami nem jó Gec\n")
    
#mentes("szavak_kbetus.txt", tomb)
                
    
    
"""
Írj függvényt, amely paraméterként a fájl nevét kapja,
és visszaad egy listát, amelyik a megállók neveit tartalmazza!
"""
    

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
        
    
        
#x = beolvaso("m1.txt")


"""
Írj függvényt, amelyik paraméterként két fájl nevét kapja,
és meghatározza, hogy át lehet-e szállni az egyik metróvonalról
a másikra! Ha igen, térjen vissza a megálló nevével, ha nem, akkor
None értékkel!
"""
        
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
        

#x = atszallas("m1.txt","m2.txt")
"""
if isinstance(x, set):
    for xd in x:
        print(xd, end=" ")
        
    print()
"""    

def main():
    if len(sys.argv) == 3:
        f1 = sys.argv[1]
        f2 = sys.argv[2]
        be_f1 = beolvaso(f1)
        be_f2 = beolvaso(f2)
        print("A m1.txt megállói:")
        print("___________________________________________________\n")
        for sor in be_f1:
            print(sor.megallo)
        
        print("A m2.txt megállói:")
        print("___________________________________________________\n")
        
        for sor in be_f2:
            print(sor.megallo)
            
        x = atszallas(f1,f2)
        
        print("\nKözös megálló:")
        print("___________________________________________________\n")
        if isinstance(x, set):
            for xd in x:
                print(xd)
                
            print()
    else:
        sys.stderr.write("Használat: python3 falj.py m1.txt m2.txt\nElöször a fálj név utána spacek mentén két db szöveges fájln")
        sys.exit(1)
    
    
     






main()
            
