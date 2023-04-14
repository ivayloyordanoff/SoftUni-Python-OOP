from project.movie import Movie

import unittest


class TestMovie(unittest.TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Pulp Fiction", 1994, 8.8)

    def test_initialize(self):
        self.assertEqual(self.movie.name, "Pulp Fiction")
        self.assertEqual(self.movie.year, 1994)
        self.assertEqual(self.movie.rating, 8.8)
        self.assertEqual(self.movie.actors, [])

    def test_set_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""
        self.assertEqual(str(ex.exception), "Name cannot be an empty string!")

    def test_set_name_correctly(self):
        self.movie.name = "Troy"
        self.assertEqual(self.movie.name, "Troy")

    def test_set_year_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1886
        self.assertEqual(str(ex.exception), "Year is not valid!")

    def test_add_actor_correctly(self):
        self.movie.add_actor("John Travolta")
        self.assertEqual(self.movie.actors, ["John Travolta"])

    def test_add_actor_already_added(self):
        self.movie.add_actor("John Travolta")
        result = self.movie.add_actor("John Travolta")
        self.assertEqual(result, "John Travolta is already added in the list of actors!")

    def test_rating_greater_than_other(self):
        other = Movie("Troy", 2004, 7.3)
        result = self.movie.__gt__(other)
        self.assertEqual(result, '"Pulp Fiction" is better than "Troy"')

    def test_other_rating_is_greater(self):
        other = Movie("The Godfather", 1972, 9.2)
        result = self.movie.__gt__(other)
        self.assertEqual(result, '"The Godfather" is better than "Pulp Fiction"')

    def test_represent(self):
        self.movie.add_actor("John Travolta")
        result = repr(self.movie)
        self.assertEqual(result, "Name: Pulp Fiction\n"
                                 "Year of Release: 1994\n"
                                 "Rating: 8.80\n"
                                 "Cast: John Travolta")


if __name__ == '__main__':
    unittest.main()
