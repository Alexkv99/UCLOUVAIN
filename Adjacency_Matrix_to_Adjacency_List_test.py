import unittest
from Adjacency_Matrix_to_Adjacency_List import mat_to_list

class MatToListTestCase(unittest.TestCase):
    def test_mat_to_list_case1(self):
        adj_mat = [[0, 1, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0]]
        expected_output = [[1, 3], [2], [0], [4], [3], []]
        actual_output = mat_to_list(adj_mat)
        self.assertEqual(actual_output, expected_output)

    def test_mat_to_list_case2(self):
        adj_mat = [[0, 0, 0],
                   [1, 0, 1],
                   [1, 1, 0]]
        expected_output = [[], [0, 2], [0, 1]]
        actual_output = mat_to_list(adj_mat)
        self.assertEqual(actual_output, expected_output)
        
    def test_mat_to_list_case3(self):
        adj_mat = [[0, 0, 0],
                   [1, 1, 1],
                   [0, 0, 0]]

        expected_output = [[], [0, 1, 2], []]
        actual_output = mat_to_list(adj_mat)
        self.assertEqual(actual_output, expected_output)
        
    def test_mat_to_list_case4(self):
        adj_mat = [[0, 1, 1, 0],
                   [1, 0, 0, 1],
                   [1, 0, 0, 1],
                   [0, 1, 1, 0]]
        expected_output = [[1, 2], [0, 3], [0, 3], [1, 2]]
        actual_output = mat_to_list(adj_mat)
        self.assertEqual(actual_output, expected_output)

    def test_mat_to_list_case5(self):
        adj_mat = [[0, 0],
                   [0, 0]]
        expected_output = [[], []]
        actual_output = mat_to_list(adj_mat)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()