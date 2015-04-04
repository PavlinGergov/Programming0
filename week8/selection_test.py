import unittest
import selection


class SelectionTest(unittest.TestCase):

    def test_find_the_smalles_index(self):
        self.assertEqual(2, selection.find_index_of_smallest_number(
            0, [2, 3, 0, 5]))

    def test_slection(self):
        self.assertEqual([1, 2, 3, 4], selection.selection_sort([3, 1, 4, 2]))

if __name__ == '__main__':
    unittest.main()
