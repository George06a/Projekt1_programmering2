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
            return True
        else:
            print(f"{self.namn} är för trött för att attackera!\n Stamina: {self.get_stamina()} \n")
            return False
    
    def superattack(self, motståndare):
        if self.get_stamina() >= 80:
            print(f"{self.namn} gör en SUPERATTACK på {motståndare.namn}!")
            motståndare.ta_skada(self.power * 3)
            self.ändra_stamina(-80)
            print(f"Stamina kvar: {self.get_stamina()}\n")
            return True
        else:
            print(f"{self.namn} har inte tillräckligt med stamina för superattack!\nFörsök Igen \n")
            return False

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
    
    def visa_stats(self):
        print(f"\n🔹 {self.namn}s stats:")
        print(f"Hälsa: {self.get_hälsa()}")
        if isinstance(self, Mage):
            print(f"Mana: {self.get_mana()}")
        else:
            print(f"Stamina: {self.get_stamina()}")
        print(f"Power: {self.power}\n")
    
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
            return True
        else:
            print(f"{self.namn} har inte tillräckligt med mana!\n")
            return False

    def få_mana(self):
        self.__mana += 5
        print(f"{self.namn} får tillbaks 5 mana. \n Mana nu: {self.get_mana()} \n")

    def superattack(self, motståndare):
        if self.__mana >= 80:
            print(f"{self.namn} gör en SUPERATTACK på {motståndare.namn}!")
            motståndare.ta_skada(self.power * 3)
            self.__mana -= 80
            print(f"Mana kvar: {self.get_mana()}\n")
            return True
        else:
            print(f"{self.namn} har inte tillräckligt med mana för superattack!\n Försök Igen!\n")
            return False
    
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

class Spelare:
    def __init__(self, karaktär):
        self.karaktär = karaktär

    def tur(self, motståndare):
        while True:
            val = input("1. Attack  2. Superattack  3. Blocka  4. Visa Stats: ")
            if val == "1":
                if self.karaktär.attack(motståndare.karaktär): break
            elif val == "2":
                if self.karaktär.superattack(motståndare.karaktär): break
            elif val == "3":
                self.karaktär.blocka(); break
            elif val == "4":
                self.karaktär.visa_stats()
            else:
                print("Ogiltigt val, försök igen!")

class Dator(Spelare):
    def tur(self, motståndare):
        while True:
            val = random.choice([1, 2, 3])
            if val == 1 and self.karaktär.attack(motståndare.karaktär): break
            elif val == 2 and self.karaktär.superattack(motståndare.karaktär): break
            elif val == 3:
                self.karaktär.blocka(); break

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



class Spel:
    def __init__(self, spelare1, spelare2):
        self.spelare1 = spelare1
        self.spelare2 = spelare2
        self.runda = 1

    def start(self):
        print(f"\n⚔️ Striden börjar mellan {self.spelare1.karaktär.namn} och {self.spelare2.karaktär.namn}! ⚔️\n")
        while self.spelare1.karaktär.lever() and self.spelare2.karaktär.lever():
            print(f"--- Runda {self.runda} ---")

            print(f"\n{self.spelare1.karaktär.namn}s tur:")
            self.spelare1.ta_tur(self.spelare2)

            if not self.spelare2.karaktär.lever():
                print(f"\n💀 {self.spelare2.karaktär.namn} besegrades! {self.spelare1.karaktär.namn} vann! 💪")
                break

            print(f"\n{self.spelare2.karaktär.namn}s tur:")
            self.spelare2.ta_tur(self.spelare1)

            if not self.spelare1.karaktär.lever():
                print(f"\n💀 {self.spelare1.karaktär.namn} besegrades! {self.spelare2.karaktär.namn} vann! 💪")
                break

            # Mage får tillbaka mana
            if isinstance(self.spelare1.karaktär, Mage):
                self.spelare1.karaktär.få_mana()
            if isinstance(self.spelare2.karaktär, Mage):
                self.spelare2.karaktär.få_mana()

            self.runda += 1


def main():
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
    
    spel = Spel(spelare1,spelare2)
    spel.start()

main()