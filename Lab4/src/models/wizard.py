from src.models.character import Character


class Wizard(Character):
    def __init__(self, name, health=80, mana=100):
        super().__init__(name, health)
        self.mana = mana
        self.max_health = health

    def cast_heal_spell(self, wand, target):
        if self.mana < 20:
            return f"{self.name} no tiene suficiente maná para curar"

        self.mana -= 20
        return wand.heal(self, target)
