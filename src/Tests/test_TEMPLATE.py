# TEST: MODULE.PY

import module.py
import unittest


class Test(unittest.TestCase):
    def moduleMethod(self):
        pass

    def moduleFunction(self):
        pass

    def moduleMethod2(self):
        pass

    def moduleFunction2(self):
        pass


#################################FOR TEST RUNNER###############################

if __name__ == "__main__":
    unittest.main()