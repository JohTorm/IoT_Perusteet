oviKiinni = False
oviLukittu = False
oviTila = ""

if oviKiinni == False and oviLukittu == False:
    oviTila = "Auki ja Avoinna"
elif oviKiinni == True and oviLukittu == False:
    oviTila = "Kiinni ja Avoinna"
elif oviKiinni == True and oviLukittu == True:
    oviTila = "Kiinni ja Lukittu"
    
print("ovi on " + oviTila)
userInput = int(input("Mitäs tehdään? sulje ovi = 1, sulje ja lukitse = 2 " ))
if userInput == 1:
    oviTila = "Kiinni ja Avoinna"
    print("ovi on " + oviTila)
    