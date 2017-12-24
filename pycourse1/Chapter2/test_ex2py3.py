# test_ex2py3.py 

import unittest
from ex2py3 import nameResponse

class PrimesTestCase(unittest.TestCase):
	"""Tests for 'ex2py3.py'."""

	def test_name_John(self):
		"""Is 'John' the outputted name?"""
		self.assertEqual(nameResponse('John'), msg='Hello John')

if __name__ == '__main__':
	unittest.main()