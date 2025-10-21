import unittest
from src.models.character import Character
from src.models.magic_wand import MagicWand
from src.models.wizard import Wizard


class TestMagicSystem(unittest.TestCase):

    def test_magic_wand_heal_increases_health(self):
        """Test que la varita mágica cura a un personaje herido"""
        wizard = Character("Gandalf")
        warrior = Character("Frodo")
        warrior.take_damage(30)  # 100 - 30 = 70

        wand = MagicWand()
        result = wand.heal(wizard, warrior)

        self.assertEqual(warrior.health, 90)  # 70 + 20
        self.assertIn("cura", result)
        self.assertIn("varita mágica", result)

    def test_cannot_heal_dead_character(self):
        """Test que no se puede curar a un personaje muerto"""
        wizard = Character("Gandalf")
        dead_warrior = Character("Boromir")
        dead_warrior.take_damage(100)  # Muere

        wand = MagicWand()
        result = wand.heal(wizard, dead_warrior)

        self.assertFalse(dead_warrior.is_alive)
        self.assertIn("No se puede curar", result)
        self.assertEqual(dead_warrior.health, 0)

    def test_wizard_mana_consumption(self):
        """Test que el mago gasta maná al curar"""
        wizard = Wizard("Gandalf")
        wounded_ally = Character("Frodo")
        wounded_ally.take_damage(40)

        wand = MagicWand()
        initial_mana = wizard.mana

        result = wizard.cast_heal_spell(wand, wounded_ally)

        self.assertEqual(wizard.mana, initial_mana - 20)
        self.assertIn("cura", result)

    def test_magic_wand_also_attacks(self):
        """Test que la varita también puede atacar (implementa Weapon)"""
        wizard = Character("Gandalf")
        enemy = Character("Saruman")
        wand = MagicWand()

        result = wand.attack(wizard, enemy)

        self.assertEqual(enemy.health, 92)  # 100 - 8
        self.assertIn("hechizo ofensivo", result)