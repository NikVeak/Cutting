import unittest
from service import (transpose_matrix,
                     linear_cut_method,
                     compare_equal, sum_array,
                     sum_and_compare,
                     find_optimal_maps,
                     linear_cutting,
                     reсycle_maps,
                     merge_3d_array_to_2d,
                     place_rectangles,
                     linear_cutting_multi,
                     bivariate_cut,
                     linear_cut_method_multi)


class TestCuttingMethods(unittest.TestCase):
    # юнит тесты
    #-------------------------------------------------------------------------------------------------------------------
    def test_linear_cutting_multi(self):
        original_lengths = [6000, 5000]
        cuts_length = [2325, 2000, 1635, 1590, 250, 230, 150]
        cuts_count = [2, 2, 2, 2, 7, 7, 7]
        result = linear_cutting_multi(original_lengths, cuts_length, cuts_count)
        if result:
            print("OK")
        else:
            print("Uncorrect")
    def test_place_rectangles(self):
        original_length = 6000
        cuts_length = [2000, 3000, 400]
        cuts_count = [2, 20, 5]
        result = place_rectangles(original_length, cuts_length, cuts_count)
        if result:
            print("OK")
        else:
            print("Uncorrect")
    def test_merge_3d_array_to_2d(self):
        array_3d = [[[5, 6, 7, 8], [6, 9, 10, 11]], [7, 6, 9, 9, 10]], [[60, 19, 11]]
        result = merge_3d_array_to_2d(array_3d)

        if result:
            print("OK")
        else:
            print("Uncorrect")

        array_3d = []
        result = merge_3d_array_to_2d(array_3d)

        if result:
            print("OK")
        else:
            print("Uncorrect")

    def test_recycle_maps(self):
        original_length = 6000
        cuts_length = [1500, 1000]
        maps = [[2, 0, 3000], [2, 3, 0], [2, 3, 0]]
        result = reсycle_maps(original_length, cuts_length, maps)
        print(result)
        if result:
            print("OK, function recycle_maps was tested (1) ")
        else:
            print("Error, function recycle_maps (1) ")

        original_length = 6000
        cuts_length = [1500, 1000]
        maps = [[2, 0], [2, 3], [2, 3]]
        result = reсycle_maps(original_length, cuts_length, maps)
        print(result)
        if result:
            print("OK, function recycle_maps was tested (2) ")
        else:
            print("Error, function recycle_maps (2) ")

    def test_sum_and_compare(self):
        # случай когда сумма массивов не равна третьему
        arr1 = [2, 9, 0]
        arr2 = [4, 2, 8]
        arr3 = [6, 3, 8]
        result = sum_and_compare(arr1, arr2, arr3)
        if not result:
            print("OK, sum_and_compare (1)")

        arr1 = [2, 1, 0]
        arr2 = [4, 2, 8]
        arr3 = [6, 3, 8]
        result = sum_and_compare(arr1, arr2, arr3)
        if result:
            print("OK, sum_and_compare (2)")
        else:
            print("Error, sum_and_compare (2)")

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
            print("OK ! Arrays arent equal (1)")

        # случай когда массивы не равны
        arr1 = [2, 9, 0]
        arr2 = [2, 9, 0]
        result = compare_equal(arr1, arr2)
        if not result:
            print("OK ! Arrays arent equal (2)")

    def test_linear_cutting(self):
        original_length = 6000
        cuts_length = [2000, 3000, 400]
        cuts_count = [2, 20, 5]
        result = linear_cutting(original_length, cuts_length, cuts_count)

        if result:
            print("OK, linear_cutting")
        else:
            print("Error, linear_cutting")

    def test_transpose_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        result = transpose_matrix(matrix)

        if result:
            print("OK, transpose_matrix")
        else:
            print("Error, transpose_matrix")

    # -------------------------------------------------------------------------------------------------------------------

    # интеграционные тесты
    # -------------------------------------------------------------------------------------------------------------------
    def test_linear_cut_method(self):
        original_length = 100
        cuts_length = [20, 30, 40]
        cuts_count = [2, 2, 2]
        result = linear_cut_method(original_length, cuts_length, cuts_count)
        if result:
            print("OK, linear_cut_method")
        else:
            print("Error, linear_cut_method")

    def test_find_optimal_maps(self):
        original_length = 6000
        cuts_length = [2000, 3000, 400]
        cuts_count = [2, 20, 5]
        result = find_optimal_maps(original_length, cuts_length, cuts_count)
        if result:
            print("OK, find_optimal_maps")
        else:
            print("Error, find_optimal_maps")

    def test_bivariate_cut(self):
        total_area = 30
        smaller_rectangles = [10, 8, 5, 4, 3]
        smaller_rect_count = [1, 2, 2, 1, 0]
        result = bivariate_cut(total_area, smaller_rectangles, smaller_rect_count)

        if result:
            print("OK, bivariate_cut")
        else:
            print("Error, bivariate_cut")

    def test_linear_cut_method_multi(self):
        original_lengths = [6000, 5000]
        cuts_length = [2325, 2000, 1635, 1590, 250, 230, 150]
        cuts_count = [2, 2, 2, 2, 7, 7, 7]
        result = linear_cut_method_multi(original_lengths, cuts_length, cuts_count)
        if result:
            print("OK, linear_cut_method_multi")
        else:
            print("Error, linear_cut_method_multi")
    # -------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
