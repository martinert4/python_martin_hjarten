#	Läs in datan: Spara i en struktur så man vet värden som hör till Pichu respektive Pikachu.

#skapa funktion för att läsa in filerna 

def las_in_pokemon(filnamn):
    temp_lista = []  # En tom lista som fylls på inuti funktionen
    
    with open(filnamn, "r") as fil:
        for rad in fil:
            rad = rad.strip()
            
            if "width" in rad:
                continue
                
            if rad:
                steg_1 = rad.replace("(", "").replace(")", "")
                delar = steg_1.split(",")
                
                bredd = float(delar[0])
                höjd = float(delar[1])
                
                temp_lista.append([bredd, höjd])
                
    return temp_lista  



# läs in båda filerna
pichu_lista = las_in_pokemon("data/pichu.txt")
pikachu_lista = las_in_pokemon("data/pikachu.txt")







# Skapa listor för x och y för alla punkter

# Skapa tomma listor för x och y för Pichu
pichu_x = []
pichu_y = []

for p in pichu_lista:
    pichu_x.append(p[0]) # index 0 är bredd (X)
    pichu_y.append(p[1]) # index 1 är höjd (Y)



# Skapa tomma listor för x och y för pikachu
pikachu_x = []
pikachu_y = []

for p in pikachu_lista:
    pikachu_x.append(p[0]) # index 0 är bredd (X)
    pikachu_y.append(p[1]) # index 1 är höjd (Y)




# Hårdkodade testpunkter
testpunkter_lista = [[25, 35], [15,14], [26,30], [22,45]]






# Skapa tomma listor för x och y för testpunkter
testpunkt_x = []
testpunkt_y = []

# Loopa igenom 
for p in testpunkter_lista:
    testpunkt_x.append(p[0]) # index 0 är bredd (X)
    testpunkt_y.append(p[1]) # index 1 är höjd (Y)







# Beräkna avstånd från respektive testpunkt

import math


# funktion för beräkna avstånd mellan två punkter
def avstånd(x1,y1,x2,y2):
    
    

    avstånd_beräkning = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return avstånd_beräkning 



# funktion för beräkna avstånd mellan testpunkt och punkt från lista
def hämta_kortaste_avstånd(en_testpunkt, pokemon_lista):
    resultat_lista = []
    
    # Vi loopar igenom listan 
    for i in range(len(pokemon_lista)):
        # Vi använder parametrarna istället för hårdkodade namn!
        resultat_lista.append(avstånd(*en_testpunkt, *pokemon_lista[i]))
        
    # Hitta det minsta talet
    minsta_avståndet = min(resultat_lista)
    
   
    return minsta_avståndet




# Nedan kommer beräkningarna 


for k in range(4):

    test_punkt = testpunkter_lista[k]

    # funktionen för Pichu
    avstånd_pichu = hämta_kortaste_avstånd(test_punkt, pichu_lista)

    # funktion för Pikachu
    avstånd_pikachu = hämta_kortaste_avstånd(test_punkt, pikachu_lista)


    # if-sats för att gissa
    if avstånd_pichu < avstånd_pikachu:
        print(f"Kortaste avståndet ({round(avstånd_pichu,2)} cm) är till en Pichu.  Testpunkten {test_punkt} bedöms därför vara en Pichu")
    else:
        print(f"Kortaste avståndet ({round(avstånd_pikachu,2)} cm) är till en Pikachu.  Testpunkten {test_punkt} bedöms därför vara en Pikachu")






#Visualisering: Plotta punkter i ett koordinatsystem. Ge Pichu-punkterna blå färg och Pikachu  röd färg.

import matplotlib.pyplot as plt

# Skapa själva fönstret
plt.figure(figsize=(8, 6))

# Pichu som BLÅ punkter 
plt.scatter(pichu_x, pichu_y, color="blue", label="Pichu", alpha=0.7)

# Pikachu som RÖDA punkter 
plt.scatter(pikachu_x, pikachu_y, color="red", label="Pikachu", alpha=0.7)

# testpunkter som gröna stjärnor 
plt.scatter(testpunkt_x, testpunkt_y, color="green", marker="*", s=150, label="Okänd (Testpunkt)")



# rubriker på axlarna och diagrammet
plt.xlabel("Bredd (cm)", fontsize=12)
plt.ylabel("Höjd (cm)", fontsize=12)
plt.title("Visualisering av Pichu, Pikachu och Testpunkter", fontsize=14, fontweight="bold")

# färgförklaring
plt.legend()

# rutnät så det blir lättare att läsa av koordinater
plt.grid(True, linestyle="--", alpha=0.5)

# Visa diagrammet på skärmen!
plt.show()





