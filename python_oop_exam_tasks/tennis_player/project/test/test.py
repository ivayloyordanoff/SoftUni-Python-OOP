from project.tennis_player import TennisPlayer
import unittest


class TestTennisPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Roger Federer", 41, 10000)

    def test_initialize(self):
        self.assertEqual(self.tennis_player.name, "Roger Federer")
        self.assertEqual(self.tennis_player.age, 41)
        self.assertEqual(self.tennis_player.points, 10000)
        self.assertEqual(self.tennis_player.wins, [])
        self.tennis_player.wins = ["Wimbledon"]
        self.assertEqual(self.tennis_player.wins, ["Wimbledon"])

    def test_set_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.tennis_player.name = "R"
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")
        with self.assertRaises(ValueError) as ex:
            self.tennis_player.name = "Ro"
            self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

    def test_set_name_correct(self):
        self.tennis_player.name = "Rafael Nadal"
        self.assertEqual(self.tennis_player.name, "Rafael Nadal")

    def test_set_age_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.tennis_player.age = 17
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

    def test_set_age_correct(self):
        self.tennis_player.age = 18
        self.assertEqual(self.tennis_player.age, 18)

    def test_add_new_win(self):
        self.tennis_player.add_new_win("Wimbledon")
        self.assertEqual(self.tennis_player.wins, ["Wimbledon"])

    def test_add_existing_win(self):
        self.tennis_player.add_new_win("Wimbledon")
        self.assertEqual(self.tennis_player.wins, ["Wimbledon"])
        result = self.tennis_player.add_new_win("Wimbledon")
        self.assertEqual(result, "Wimbledon has been already added to the list of wins!")

    def test_tennis_player_points_less_than_other_tennis_player_points(self):
        other_tennis_player = TennisPlayer("Rafael Nadal", 36, 11000)
        result = self.tennis_player.__lt__(other_tennis_player)
        self.assertEqual(result, 'Rafael Nadal is a top seeded player and he/she is better than Roger Federer')

    def test_tennis_player_points_greater_than_other_tennis_player_points(self):
        other_tennis_player = TennisPlayer("Rafael Nadal", 36, 9000)
        result = self.tennis_player.__lt__(other_tennis_player)
        self.assertEqual(result, 'Roger Federer is a better player than Rafael Nadal')

    def test_string_representation(self):
        self.tennis_player.add_new_win("Wimbledon")
        self.tennis_player.add_new_win("Australian Open")
        self.assertEqual(str(self.tennis_player), "Tennis Player: Roger Federer\n"
                                                  "Age: 41\n"
                                                  "Points: 10000.0\n"
                                                  "Tournaments won: Wimbledon, Australian Open")


if __name__ == "__main__":
    unittest.main()
