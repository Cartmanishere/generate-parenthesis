import unittest
import sys

class Solution:
    def generate_parenthesis(self, num):
        """
        Returns a list of valid parenthesis strings of input length
        :param num: length of each string
        :return arr: resultant array of strings
        """
        if num <= 0:
            return []

        self.ans = []
        self.N = num
        self.parenthesis()
        return self.ans

    def parenthesis(self, s='', left=0, right=0):
        if len(s) == 2 * self.N:
            self.ans.append(s)
            return
        if left < self.N:
            self.parenthesis(s + '(', left + 1, right)
        if right < left:
            self.parenthesis(s + ')', left, right + 1)


class TestCases(unittest.TestCase):

    def test_generateParenthesis(self):
        s = Solution()
        self.assertListEqual(s.generate_parenthesis(0), [])
        self.assertListEqual(s.generate_parenthesis(1), ['()'])
        self.assertListEqual(s.generate_parenthesis(2), ['(())', '()()'])
        self.assertListEqual(s.generate_parenthesis(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])


if __name__ == "__main__":
    s = Solution()

    while True:
        try:
            n = input('Enter n (^C to exit): ')
            if not n.isdigit():
                raise ValueError('n must be a valid non-negative number')
            n = int(n)

            print(s.generate_parenthesis(n))
        except KeyboardInterrupt as e:
            sys.exit(0)
