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

        self.assertEqual(0, my_hero.health)
        self.assertEqual(0, my_enemy.health)
        self.assertEqual("Draw", result)

    def test_battle_win(self):
        # goes in setUp
        my_hero = Hero("UsernameHero", 1, 100.0, 10.0)
        my_enemy = Hero("Enemy", 1, 10.0, 10.0)

        result = my_hero.battle(my_enemy)

        # result = self.hero.battle(self.enemy)
        #
        # self.assertEqual(2, self.hero.level)
        # self.assertEqual(95, self.hero.health)
        # self.assertEqual(15, self.hero.damage)
        # self.assertEqual("You win", result)

        self.assertEqual("You win", result)
        self.assertEqual(2, my_hero.level)
        self.assertEqual(95, my_hero.health)
        self.assertEqual(15.0, my_hero.damage)

# no need to test
        self.assertEqual(1, my_enemy.level)
        self.assertEqual(0, my_enemy.health)
        self.assertEqual(10.0, my_enemy.damage)

    def test_battle_lose(self):
        my_hero = Hero("UsernameHero", 1, 10.0, 10.0)
        my_enemy = Hero("Enemy", 1, 100.0, 10.0)

        result = my_hero.battle(my_enemy)

        # result = self.enemy.battle(self.hero)
        #
        # self.assertEqual(2, self.hero.level)
        # self.assertEqual(55, self.hero.health)
        # self.assertEqual(105, self.hero.damage)
        # self.assertEqual("You lose", result)

        self.assertEqual("You lose", result)
        self.assertEqual(1, my_hero.level)
        self.assertEqual(0, my_hero.health)
        self.assertEqual(10.0, my_hero.damage)

        self.assertEqual(2, my_enemy.level)
        self.assertEqual(95, my_enemy.health)
        self.assertEqual(15.0, my_enemy.damage)

    def test_str(self):
        self.assertEqual(f"Hero UsernameHero: 1 lvl\n"
                         f"Health: 100.0\n"
                         f"Damage: 10.0\n", str(self.my_hero))


if __name__ == "__main__":
    unittest.main()
