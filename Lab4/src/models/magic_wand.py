from src.models.weapon import Weapon


class MagicWand(Weapon):
    def __init__(self, spell_power=20):
        self.spell_power = spell_power

    def attack(self, attacker, target):
        # Daño mágico fijo
        damage = 8
        target.take_damage(damage)
        return f"{attacker.name} lanza hechizo ofensivo a {target.name} causando {damage} de daño mágico"

    def heal(self, caster, target):
        # Nueva funcionalidad: curar aliados
        if not target.is_alive:
            return f"No se puede curar a {target.name} porque está muerto"

        heal_amount = self.spell_power
        target.heal(heal_amount)

        return f"{caster.name} cura a {target.name} con varita mágica (+{heal_amount} salud)"
