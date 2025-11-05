#Klassbaserat spel

#Superklassen
class Karaktärer:
    def __init__(self,namn,hälsa,power,stamina):
        self.namn = namn
        self.__hälsa = hälsa
        self.power = power
        self.__stamina = stamina

    def get_hälsa(self):
        return self.__hälsa
    
    def get_stamina(self):
        return self.__stamina

    def attack(self, motståndare):
        if self.get_stamina()>=10:
            print(f"{self.namn} attackerar {motståndare.namn}")
            motståndare.ta_skada(self.power)
            self.ändra_stamina(-10)
            print(f"Stamina Kvar: {self.get_stamina()}\n")
        else:
            print(f"{self.namn} är för trött för att attackera!\n Stamina: {self.get_stamina()} \n")
    
    def superattack(self, motståndare):
        if self.get_stamina() >= 80:
            print(f"{self.namn} gör en SUPERATTACK på {motståndare.namn}!")
            motståndare.ta_skada(self.power * 3)
            self.ändra_stamina(-80)
            print(f"Stamina kvar: {self.get_stamina()}\n")
        else:
            print(f"{self.namn} har inte tillräckligt med stamina för superattack!\n")

    def blocka(self):
        self.ändra_stamina(25)
        print(f"{self.namn} blockerar och återfår 25 stamina!\n Stamina nu: {self.get_stamina()}\n")
    
    # Vad händer efter karaktären tagit skada.
    def ta_skada(self, skada):
        self.__hälsa -= skada
        if self.__hälsa < 0:
            self.__hälsa = 0
        print(f"{self.namn} tar {skada} skada.\n Hälsa kvar: {self.get_hälsa()}\n")

    def ändra_stamina(self, värde):  # Ändrat: ny metod för inkapsling
        self.__stamina += värde
        if self.__stamina < 0:
            self.__stamina = 0

    #Kontrollerar om karaktären fortfarande är i liv.
    def lever(self):
        return self.__hälsa > 0 
    
#Karaktär 1
class Mage(Karaktärer):
    def __init__(self,namn,hälsa,power,mana):
        super().__init__(namn,hälsa,power,stamina=0)
        self.__mana = mana

    def get_mana(self):
        return self.__mana

    def attack(self, motståndare):
        if self.__mana>=10:
            print(f"{self.namn} Attackerar {motståndare.namn}")
            motståndare.ta_skada(self.power)
            self.__mana-=10
        else:
            print(f"{self.namn} har inte tillräckligt med mana!\n")

    def få_mana(self):
        self.__mana += 5
        print(f"{self.namn} får tillbaks 5 mana. \n Mana nu: {self.get_mana()} \n")

    def superattack(self, motståndare):
        if self.__mana >= 80:
            print(f"{self.namn} gör en SUPERATTACK på {motståndare.namn}!")
            motståndare.ta_skada(self.power * 3)
            self.__mana -= 80
            print(f"Mana kvar: {self.get_mana()}\n")
        else:
            print(f"{self.namn} har inte tillräckligt med mana för superattack!\n")
    
    def blocka(self):
        self.__mana += 15
        print(f"{self.namn} blockerar/dodgar och återfår 15 mana! \n Mana nu: {self.get_mana()}\n")

#Karaktär 2 
class Assasin(Karaktärer):
    def __init__(self,namn,hälsa,power,stamina):
        super().__init__(namn,hälsa,power,stamina)

#Karaktär 3
class Shieldbearer(Karaktärer):
    def __init__(self,namn,hälsa,power,stamina):
        super().__init__(namn,hälsa,power,stamina)

#Karaktär 4 
class Gambler(Karaktärer):
    def __init__(self,namn,hälsa,power,stamina):
        super().__init__(namn,hälsa,power,stamina)


import random

def dator_tur(dator, motståndare):
    """Datorn väljer slumpmässigt attack, superattack eller blocka"""
    val = random.choice([1,2,3])
    if val == 1:
        dator.attack(motståndare)
    elif val == 2:
        dator.superattack(motståndare)
    elif val == 3:
        dator.blocka()

def välj_karaktär(spelarnamn):
    while True:
        print(f"\n{spelarnamn}, välj din karaktär:")
        print("1. Mage\n2. Assasin\n3. Shieldbearer\n4. Gambler")
        val = input("Val: ")

        if val == "1":
            return Mage(spelarnamn, 100, 15, mana=75)
        elif val == "2":
            return Assasin(spelarnamn, 110, 20, 100)
        elif val == "3":
            return Shieldbearer(spelarnamn, 150, 10, 120)
        elif val == "4":
            # ger random hälsa, power och stamina för Gambler
            hälsa = random.randint(100, 150)     # mellan 100 och 150
            power = random.randint(10, 20)       # mellan 10 och 20
            stamina = random.randint(50, 100)    # mellan 50 och 120
            print(f"{spelarnamn} Har valt Gambler och får Hälsa:{hälsa}, Skada:{power}, Stamina:{stamina}\n")
            return Gambler(spelarnamn, hälsa, power, stamina)
        else:
            print("Fel val! Vänligen försök igen.\n")



def Spel(spelare1, spelare2):
    print(f"\n⚔️ Striden börjar mellan {spelare1.namn} och {spelare2.namn}! ⚔️\n")
    runda = 1
    while spelare1.lever() and spelare2.lever():
        print(f"--- Runda {runda} ---")

        # Spelare 1:s tur
        print(f"\n{spelare1.namn}s tur:")
        while True:
            val = input("1. Attack  2. Superattack  3. Blocka: ")
            if val == "1":
                spelare1.attack(spelare2)
                break
            elif val == "2":
                spelare1.superattack(spelare2)
                break
            elif val == "3":
                spelare1.blocka()
                break
            else:
                print("Ogiltigt val, du missade din tur!")
                continue

        if not spelare2.lever():
            print(f"\n💀 {spelare2.namn} besegrades! {spelare1.namn} vann! 💪")
            break

        # Spelare 2:s tur
        print(f"\n{spelare2.namn}s tur:")
        if spelare2.namn == "Datorn":
            dator_tur(spelare2,spelare1)
        else:
            while True:
                val = input("1. Attack  2. Superattack  3. Blocka: ")
                if val == "1":
                    spelare2.attack(spelare1)
                    break
                elif val == "2":
                    spelare2.superattack(spelare1)
                    break
                elif val == "3":
                    spelare2.blocka()
                    break
                else:
                    print("Ogiltigt val, Testa Igen!")
                    continue

        if not spelare1.lever():
            print(f"\n💀 {spelare1.namn} besegrades! {spelare2.namn} vann! 💪")
            break

        # Mage får tillbaka mana varje runda
        if isinstance(spelare1, Mage):
            spelare1.få_mana()
        if isinstance(spelare2, Mage):
            spelare2.få_mana()

        runda += 1


if __name__ == "__main__":
    print("Välkommen till STRIDSSPELET!\n")
    print("1. Spela 1v1\n2. Spela mot datorn")
    läge = input("Välj läge: ")

    if läge == "1":
        namn1 = input("Spelare 1 namn: ")
        namn2 = input("Spelare 2 namn: ")
        spelare1 = välj_karaktär(namn1)
        spelare2 = välj_karaktär(namn2)
        Spel(spelare1, spelare2)

    elif läge == "2":
        namn1 = input("Ditt namn: ")
        spelare1 = välj_karaktär(namn1)
        dator = random.choice([
            Mage("Datorn", 100, 15, mana=50),
            Assasin("Datorn", 110, 20, 100),
            Shieldbearer("Datorn", 150, 10, 120),
            Gambler("Datorn", 120, 12, 100)
        ])
        print(f"\nDu möter {dator.namn} som är en {dator.__class__.__name__}!\n")
        Spel(spelare1, dator)

    else:
        print("Ogiltigt val, spelet avslutas.")
