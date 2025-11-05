#Klassbaserat spel

#Superklassen
class Karaktärer:
    def __init__(self,namn,hälsa,power,stamina):
        self.namn = namn
        self.hälsa = hälsa
        self.skada = power
        self.stamina = stamina
    
    def attack(self, motståndare):
        if self.stamina>0:
            print(f"{self.namn} attackerar {motståndare.namn}")
            motståndare.Ta_Skada(self.power)
            self.stamina -= 10
            print(f"Stamina Kvar: {self.stamina}\n")
        else:
            print(f"{self.namn} är för trött för att attackera!\n Stamina: {self.stamina} \n")
    
    # Vad händer efter karaktären tagit skada.
    def Ta_Skada(self, skada):
        self.hälsa -= skada
        if self.hälsa < 0:
            self.hälsa = 0
        print(f"{self.namn} tar {skada} skada.\n Hälsa kvar: {self.hälsa}\n")

    #Kontrollerar om karaktären fortfarande är i liv.
    def lever(self):
        return self.hälsa > 0 
    
#Karaktär 1
class Mage(Karaktärer):
    def __init__(self,namn,hälsa,power,mana):
        super().__init__(namn,hälsa,power,stamina=0)
        self.mana = mana

    def attack(self, motståndare):
        print(f"{self.namn} Attackerar {motståndare.namn}")
        motståndare.Ta_Skada(self.power)

    def få_mana(self):
        self.mana += 5
        print(f"{self.namn} får tillbaks 5 mana. \n Mana nu: {self.mana} \n")

#Karaktär 2 
class Assasin(Karaktärer):
    def __init__(self,namn,hälsa,power,stamina):
        super().__init__(namn,hälsa,power,stamina)

#Karaktär 3
class Shieldbearer(Karaktärer):
    def __init__(self,namn,hälsa,power,stamina):
        super().__init__(namn,hälsa,power,stamina)

#Karaktär 4 
class Ranger(Karaktärer):
    def __init__(self,namn,hälsa,power,stamina):
        super().__init__(namn,hälsa,power,stamina)