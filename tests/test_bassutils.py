import unittest
import os
import sys

sys.path.insert(0, os.getcwd())

import bassutils.abc as calc
import bassutils.text as txt

class TestCalc(unittest.TestCase):
    """ All functions should start with `test_` """

    def test_txt(self):
        self.assertEqual(txt.func(), 'hahahaha')

    def test_text(self):
        self.assertEqual(txt.func(), 'hahahaha')

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
