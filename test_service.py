import unittest
from service import transpose_matrix, linear_cut_method, compare_equal, sum_array, sum_and_compare, find_optimal_maps, \
    linear_cutting


class TestCuttingMethods(unittest.TestCase):

    def test_find_optimal_maps(self):
        original_length = 6000
        cuts_length = [2000, 3000, 400]
        cuts_count = [2, 20, 5]
        result = find_optimal_maps(original_length, cuts_length, cuts_count)
        if result:
            print("OK")
            return 0
        else:
            print("Error")
            return 1

    def test_sum_and_compare(self):
        # случай когда сумма массивов не равна третьему
        arr1 = [2, 9, 0]
        arr2 = [4, 2, 8]
        arr3 = [6, 3, 8]
        result = sum_and_compare(arr1, arr2, arr3)
        if not result:
            print("OK")

        arr1 = [2, 1, 0]
        arr2 = [4, 2, 8]
        arr3 = [6, 3, 8]
        result = sum_and_compare(arr1, arr2, arr3)
        if result:
            print("OK")
        else:
            print("Error")

    def test_sum_array(self):
        arr1 = [2, 9, 0]
        arr2 = [4, 2, 8]
        result = sum_array(arr1, arr2)
        if result:
            print("OK")
        else:
            print("Error")

    def test_compare_equal(self):
        # случай когда массивы не равны
        arr1 = [2, 9, 0]
        arr2 = [4, 2, 8]
        result = compare_equal(arr1, arr2)
        if result:
            print("OK ! Arrays arent equal")

        # случай когда массивы не равны
        arr1 = [2, 9, 0]
        arr2 = [2, 9, 0]
        result = compare_equal(arr1, arr2)
        if not result:
            print("OK ! Arrays arent equal")

    def test_linear_cutting(self):
        original_length = 6000
        cuts_length = [2000, 3000, 400]
        cuts_count = [2, 20, 5]
        result = linear_cutting(original_length, cuts_length, cuts_count)

        if result:
            print("OK")
            return 0
        else:
            print("Error")
            return 1

    def test_transpose_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        result = transpose_matrix(matrix)

        if result:
            print("OK")
            return 0
        else:
            print("Error")
            return 1

    def test_linear_cut_method(self):
        original_length = 100
        cuts_length = [20, 30, 40]
        cuts_count = [2, 2, 2]
        result = linear_cut_method(original_length, cuts_length, cuts_count)
        if result:
            print("OK")
            return 0
        else:
            print("Error")
            return 1


if __name__ == '__main__':
    unittest.main()
