class GameCharacter:
    def walk(self):
        print("Character is walking forward...")

    def run(self):
        print("Character is running!")

class Wizard(GameCharacter):
  
    def cast_spell(self):
        print("FIREBALL! 🔥")

class Knight(GameCharacter):

    def swing_sword(self):
        print("SLASH! ⚔️")

class Archer(GameCharacter):

    def shoot_arrow(self):
        print("SHOOO...! --)♦")


player1 = Wizard()
player2 = Knight()
player3 = Archer()


player1.walk()       


player1.cast_spell() 

player2.swing_sword() 

player3.shoot_arrow() 

player3.run() 