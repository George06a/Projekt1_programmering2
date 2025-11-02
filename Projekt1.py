#Klassbaserat spel

#Superklassen
class Karaktärer:
    def __init__(self,namn,hälsa,power):
        self.namn = namn
        self.hälsa = hälsa
        self.skada = power
    
    def attack(self, motståndare):
        print(f"{self.namn} attackerar {motståndare.namn}")
        motståndare.Ta_Skada(self.power)
    
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
    def __init__(self,namn,hälsa,power):
        super().__init__(namn,hälsa,power)

#Karaktär 2 
class Assasin(Karaktärer):
    def __init__(self,namn,hälsa,power):
        super().__init__(namn,hälsa,power)

#Karaktär 3
class Shieldbearer(Karaktärer):
    def __init__(self,namn,hälsa,power):
        super().__init__(namn,hälsa,power)

#Karaktär 4 
class Ranger(Karaktärer):
    def __init__(self,namn,hälsa,power):
        super().__init__(namn,hälsa,power)