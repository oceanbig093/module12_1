import unittest
import runner



class TestRunner(unittest.TestCase):
    def test_walk(self):
        walker = runner.Runner('ходок')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        run = runner.Runner('бегун')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        challenger1 = runner.Runner('соп1')
        challenger2 = runner.Runner('соп2')
        for i in range(10):
            challenger2.run()
            challenger1.walk()
        self.assertNotEqual(challenger1.distance, challenger2.distance)


if __name__ == '__name__':
    unittest.main()
