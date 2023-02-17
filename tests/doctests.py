import unittest

class pypp_doctests(unittest.TestCase):
    def runTest(self):
        import doctest, pypp.preprocessor, pypp.evaluator
        failurecount, testcount = doctest.testmod(pypp.evaluator)
        self.assertGreater(testcount, 0)
        self.assertEqual(failurecount, 0)
        failurecount, testcount = doctest.testmod(pypp.preprocessor)
        #self.assertGreater(testcount, 0)
        self.assertEqual(failurecount, 0)

