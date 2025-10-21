import unittest
from unittest.mock import MagicMock
from src.app.combat_system import CombatSystem
from src.models.character import Character
from src.models.sword import Sword
from src.app.healing_system import HealingSystem

class TestDependencyInjection(unittest.TestCase):

    def test_combat_system_uses_injected_calculator(self):
        """Test que CombatSystem usa la calculadora inyectada"""
        mock_calculator = MagicMock()
        mock_calculator.check_critical_hit.return_value = False
        
        combat = CombatSystem(mock_calculator)
        hero = Character("Hero")
        enemy = Character("Enemy")
        
        # Necesitamos un arma real para este test
        sword = Sword()
        
        combat.perform_attack(hero, sword, enemy)
        
        # Verificamos que se llamó a la dependencia inyectada
        mock_calculator.check_critical_hit.assert_called_once()

    def test_critical_hit_adds_extra_damage(self):
        """Test que el golpe crítico añade daño extra"""
        mock_calculator = MagicMock()
        mock_calculator.check_critical_hit.return_value = True
        
        combat = CombatSystem(mock_calculator)
        hero = Character("Hero")
        enemy = Character("Enemy")
        sword = Sword()
        
        combat.perform_attack(hero, sword, enemy)
        
        # 15 de daño base + 10 de crítico = 25
        self.assertEqual(enemy.health, 75)

    def test_healing_system_dependency_injection(self):
        """Test de inyección de dependencias con sistema de curación"""
        mock_healing_system = MagicMock(spec=HealingSystem)
        mock_healing_system.can_heal.return_value = True
        mock_healing_system.calculate_heal_amount.return_value = 30

        wizard = Character("Mage")
        wounded = Character("Wounded Ally")
        wounded.take_damage(50)

        # Sistema inyectado de curación
        if mock_healing_system.can_heal(wounded):
            heal_amount = mock_healing_system.calculate_heal_amount(
                wizard, wounded)
            wounded.heal(heal_amount)

        self.assertEqual(wounded.health, 80)  # 50 + 30
        mock_healing_system.can_heal.assert_called_once_with(wounded)
        mock_healing_system.calculate_heal_amount.assert_called_once_with(
            wizard, wounded)