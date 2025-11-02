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
    
    def Ta_Skada(self, skada):
        self.hälsa -= skada
        if self.hälsa < 0:
            self.hälsa = 0
        print(f"{self.namn} tar {skada} skada.\n Hälsa kvar: {self.hälsa}")