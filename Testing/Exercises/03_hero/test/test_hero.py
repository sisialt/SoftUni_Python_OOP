import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self) -> None:
        self.my_hero = Hero("UsernameHero", 1, 100.0, 10.0)

    def test_initialize_hero(self):
        self.assertEqual("UsernameHero", self.my_hero.username)
        self.assertEqual(1, self.my_hero.level)
        self.assertEqual(100.0, self.my_hero.health)
        self.assertEqual(10.0, self.my_hero.damage)

    def test_battle_with_enemy_username_equal_to_username_raises(self):
        my_enemy = Hero("UsernameHero", 1, 100.0, 10.0)
        with self.assertRaises(Exception) as ex:
            self.my_hero.battle(my_enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_no_health_raises(self):
        self.my_hero = Hero("UsernameHero", 1, 0.0, 10.0)
        my_enemy = Hero("Enemy", 1, 100.0, 10.0)
        with self.assertRaises(ValueError) as ex:
            self.my_hero.battle(my_enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_no_enemy_health_raises(self):
        my_enemy = Hero("Enemy", 1, 0.0, 10.0)
        with self.assertRaises(ValueError) as ex:
            self.my_hero.battle(my_enemy)

        self.assertEqual(f"You cannot fight {my_enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        my_hero = Hero("UsernameHero", 1, 10.0, 10.0)
        my_enemy = Hero("Enemy", 1, 10.0, 10.0)

        result = my_hero.battle(my_enemy)

        self.assertEqual("Draw", result)

    def test_battle_win(self):
        my_hero = Hero("UsernameHero", 1, 100.0, 10.0)
        my_enemy = Hero("Enemy", 1, 10.0, 10.0)

        result = my_hero.battle(my_enemy)

        self.assertEqual("You win", result)
        self.assertEqual(2, my_hero.level)
        expected_my_hero_health = 100.0 - my_enemy.damage * my_enemy.level + 5
        self.assertEqual(expected_my_hero_health, my_hero.health)
        self.assertEqual(15.0, my_hero.damage)

        self.assertEqual(1, my_enemy.level)
        expected_my_enemy_health = 10.0 - 10.0 * 1.0
        self.assertEqual(expected_my_enemy_health, my_enemy.health)
        self.assertEqual(10.0, my_enemy.damage)

    def test_battle_lose(self):
        my_hero = Hero("UsernameHero", 1, 10.0, 10.0)
        my_enemy = Hero("Enemy", 1, 100.0, 10.0)

        result = my_hero.battle(my_enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(1, my_hero.level)
        expected_my_hero_health = 10.0 - 10.0 * 1.0
        self.assertEqual(expected_my_hero_health, my_hero.health)
        self.assertEqual(10.0, my_hero.damage)

        self.assertEqual(2, my_enemy.level)
        expected_my_enemy_health = 100.0 - my_hero.damage * my_hero.level + 5
        self.assertEqual(expected_my_enemy_health, my_enemy.health)
        self.assertEqual(15.0, my_enemy.damage)

    def test_str(self):
        self.assertEqual(f"Hero UsernameHero: 1 lvl\n"
                         f"Health: 100.0\n"
                         f"Damage: 10.0\n", str(self.my_hero))


if __name__ == "__main__":
    unittest.main()
