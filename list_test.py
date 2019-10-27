import unittest
from list import List

class TestList(unittest.TestCase):
    
    def test_init(self):
        my_list = List()
        assert my_list.element is None
        assert my_list.size == 0


if __name__ == '__main__':
    unittest.main()