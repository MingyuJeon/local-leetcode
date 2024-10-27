# 1249. Minimum Remove to Make Valid Parentheses

import unittest
from sol import Solution

class TestMinimumRemoveToMakeValid(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        self.assertEqual(self.solution.minRemoveToMakeValid("lee(t(c)o)de)"), "lee(t(c)o)de")

    def test_case2(self):
        self.assertEqual(self.solution.minRemoveToMakeValid("a)b(c)d"), "ab(c)d")

    def test_case3(self):
        self.assertEqual(self.solution.minRemoveToMakeValid("))(("), "")

    def test_case4(self):
        self.assertEqual(self.solution.minRemoveToMakeValid("(a(b)c(d)e)"), "(a(b)c(d)e)")

    def test_case5(self):
        self.assertEqual(self.solution.minRemoveToMakeValid("((a)b(c))"), "((a)b(c))")

    def test_case6(self):
        self.assertEqual(self.solution.minRemoveToMakeValid("))(("), "")

if __name__ == '__main__':
    unittest.main()