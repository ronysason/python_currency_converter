import unittest
from cur_convertor import get_rate


class TestCurConverter(unittest.TestCase):

    def test_get_rate(self):
        result = get_rate('USD', 'ILS')
        self.assertEqual(type(result), int, 'types dont match')

