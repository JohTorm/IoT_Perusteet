oviKiinni = True
oviLukittu = True
oviTila = ""

if oviKiinni == False and oviLukittu == False:
    oviTila = "Auki ja Avoinna"
elif oviKiinni == True and oviLukittu == False:
    oviTila = "Kiinni ja Avoinna"
elif oviKiinni == True and oviLukittu == True:
    oviTila = "Kiinni ja Lukittu"
    
print("ovi on " + oviTila)
if oviKiinni == True and oviLukittu == True:
    userInput = int(input("Mitäs tehdään? Avaa lukko ja ovi = 1, avaa vain lukko = 2"))
    if userInput == 1:
        oviTila = "Auki ja Avoinna"   
        oviKiinni = False
        oviLukittu = False
        print("ovi on " + oviTila)
    elif userInput == 2:
        oviTila = "Kiinni ja Avoinna"   
        oviKiinni = True
        oviLukittu = False
        print("ovi on " + oviTila)
    
if oviKiinni == False and oviLukittu == False:
    userInput = int(input("Ovi on auki, mitäs tehdään? Sulje ovi = 1, sulje ja lukitse = 2"))
    if userInput == 1:
        oviTila = "Kiinni ja Avoinna"   
        oviKiinni = True
        oviLukittu = False
        print("ovi on " + oviTila)
    elif userInput == 2:
        oviTila = "Kiinni ja lukittu"   
        oviKiinni = True
        oviLukittu = True
        print("ovi on " + oviTila)
        
if oviKiinni == True and oviLukittu == False:
    oviTila = "Kiinni ja Avoinna"
    userInput = int(input("Mitäs tehdään? Avaa ovi = 1, lukitse ovi = 2"))
    if userInput == 1:
        oviTila = "Auki ja Avoinna"   
        oviKiinni = False
        oviLukittu = False
        print("ovi on " + oviTila)
    elif userInput == 2:
        oviTila = "Kiinni ja Lukittu"   
        oviKiinni = True
        oviLukittu = True
        print("ovi on " + oviTila)