import unittest
import python_plot as ply


class Test_lotka_volterra(unittest.TestCase):

    """
    Test class for testing functions in python_plot.py
    """

    def test_initial_cond_at_t15(self):
        rate = ply.lotka_volterra([0., 0.], 15)
        self.assertAlmostEqual(rate, [0., 0.])

    def test_solve_diff_with_zero_initial_cond(self):
        [prey, predator, t] = ply.solve_diff([0., 0.], 0, 2, 50)
        for i in range(0, 50):
            self.assertAlmostEqual(prey[i], 0.)
            self.assertAlmostEqual(predator[i], 0.)

if __name__ == '__main__':
    unittest.main()
