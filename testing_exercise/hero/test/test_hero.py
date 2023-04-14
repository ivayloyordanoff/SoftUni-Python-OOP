import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_constructor(self):
        self.assertEqual(self.hero.username, "Hero")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_hero_with_yourself(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)
        self.assertEqual(str(context.exception), "You cannot fight yourself")

    def test_battle_hero_with_no_energy(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(str(context.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_with_no_energy(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(str(context.exception), "You cannot fight Enemy. He needs to rest")

    def test_battle_draw(self):
        self.hero.health = self.enemy.health
        self.hero.damage = self.enemy.damage
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.enemy.health, 0)
        self.assertEqual(result, "Draw")

    def test_battle_win(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 55)
        self.assertEqual(self.hero.damage, 105)
        self.assertEqual(result, "You win")

    def test_battle_lose(self):
        self.hero, self.enemy = self.enemy, self.hero
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.enemy.level, 2)
        self.assertEqual(self.enemy.health, 55)
        self.assertEqual(self.enemy.damage, 105)
        self.assertEqual(result, "You lose")

    def test_correct__str__(self):
        self.assertEqual(
            self.hero.__str__(),
            "Hero Hero: 1 lvl\n" +
            "Health: 100\n" +
            "Damage: 100\n"
        )


if __name__ == "__main__":
    unittest.main()
