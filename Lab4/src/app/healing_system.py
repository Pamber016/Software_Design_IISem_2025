from src.app.i_healing_system import IHealingSystem


class HealingSystem(IHealingSystem):
    def can_heal(self, target):
        return target.is_alive and target.health < 100
    
    def calculate_heal_amount(self, target):
        base_heal = 25
        # Personajes con menos salud reciben más curación
        missing_health = 100 - target.health
        return min(base_heal, missing_health)