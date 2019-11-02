#### Problem:

Given a number n, generate all possible combinations of valid parenthesis. 
For ex, if n = 3, you should return `"((()))", "(()())", "(())()", "()(())", "()()()"`

#### Solution:

We start with an empty string and we can add a opening `(` brackets if it does not exceed `n` and we can add a closing bracket if number of opening brackets is less than closing brackets. Thus when the string becomes of length `2n`, the string is a valid string of parenthesis.

#### Requirements:

- You need `Python 3` to run this program

#### Usage:

`python parenthesis.py`

#### Test:

`python -m unittest parenthesis.py`

