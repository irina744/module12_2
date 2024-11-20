import runner
from runner import Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = runner.Runner('Усэйн', 10)
        self.andrey = runner.Runner('Андрей', 9)
        self.nick = runner.Runner('Ник', 3)





    def test_usain_vs_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results["Usain vs Nick"] = results
        last_runner = max(results.keys())
        self.assertTrue(last_runner == 2 and results[last_runner].name == "Ник")

    def test_andrey_vs_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results["Andrey vs Nick"] = results
        last_runner = max(results.keys())
        self.assertTrue(last_runner == 2 and results[last_runner].name == "Ник")

    def test_all_three(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.all_results["All Three"] = results
        last_runner = max(results.keys())
        self.assertTrue(last_runner == 3 and results[last_runner].name == "Ник")

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            formatted_result = {k: v.name for k, v in value.items()}
            print(formatted_result)


if __name__ == "__main__":
    unittest.main()
