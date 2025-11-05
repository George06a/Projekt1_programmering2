#Klassbaserat spel

#Superklassen
class Karaktärer:
    def __init__(self,namn,hälsa,power,stamina):
        self.namn = namn
        self.hälsa = hälsa
        self.power = power
        self.stamina = stamina
    
    def attack(self, motståndare):
        if self.stamina>=10:
            print(f"{self.namn} attackerar {motståndare.namn}")
            motståndare.ta_skada(self.power)
            self.stamina -= 10
            print(f"Stamina Kvar: {self.stamina}\n")
        else:
            print(f"{self.namn} är för trött för att attackera!\n Stamina: {self.stamina} \n")
    
    def superattack(self, motståndare):
        if self.stamina >= 80:
            print(f"{self.namn} gör en SUPERATTACK på {motståndare.namn}!")
            motståndare.ta_skada(self.power * 3)
            self.stamina -= 80
            print(f"Stamina kvar: {self.stamina}\n")
        else:
            print(f"{self.namn} har inte tillräckligt med stamina för superattack!\n")

    def blocka(self):
        self.stamina += 25
        print(f"{self.namn} blockerar och återfår 25 stamina!\n Stamina nu: {self.stamina}\n")
    
    # Vad händer efter karaktären tagit skada.
    def ta_skada(self, skada):
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
        if self.mana>=10:
            print(f"{self.namn} Attackerar {motståndare.namn}")
            motståndare.ta_skada(self.power)
            self.mana-=10
        else:
            print(f"{self.namn} har inte tillräckligt med mana!\n")

    def få_mana(self):
        self.mana += 5
        print(f"{self.namn} får tillbaks 5 mana. \n Mana nu: {self.mana} \n")

    def superattack(self, motståndare):
        if self.mana >= 80:
            print(f"{self.namn} gör en SUPERATTACK på {motståndare.namn}!")
            motståndare.ta_skada(self.power * 3)
            self.mana -= 80
            print(f"Mana kvar: {self.mana}\n")
        else:
            print(f"{self.namn} har inte tillräckligt med mana för superattack!\n")
    
    def blocka(self):
        self.mana += 15
        print(f"{self.namn} blockerar/dodgar och återfår 15 mana! Mana nu: {self.mana}\n")

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