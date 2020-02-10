import unittest
import fuzzmatch
import sys

word1 = "HOL"
word2 = "hol"
class TestLeveshtein(unittest.TestCase):
    def test_case(self):
        self.assertEqual(
                fuzzmatch.levenshtein(word1,word1,len(word1),len(word1)).all(),
                fuzzmatch.levenshtein(word2,word2,len(word2),len(word2)).all()
                )


if __name__ == '__main__':
    unittest.main()
