import unittest
from service import find_closest_combinations, count_remains, do_count_cut, transpose_matrix, linear_cut_method

class TestPaperCuttingMethods(unittest.TestCase):

    def test_find_closest_combinations(self):
        target = 100
        limits = [5, 3, 4]
        prices = [10, 20, 30]
        count = 3
        result = find_closest_combinations(target, limits, prices, count)
        # Добавьте проверки результатов, чтобы убедиться, что функция работает правильно

    def test_count_remains(self):
        comb = [[1, 2], [3, 4]]
        L = 10
        cuts = [3, 5]
        result = count_remains(comb, L, cuts)
        # Добавьте проверки результатов, чтобы убедиться, что функция работает правильно

    def test_do_count_cut(self):
        comb = [[1, 2], [3, 4]]
        cuts = [3, 5]
        do_count_cut(comb, cuts)
        # Добавьте проверки измененных значений в comb, чтобы убедиться, что функция работает правильно

    def test_transpose_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        result = transpose_matrix(matrix)
        # Добавьте проверки результата, чтобы убедиться, что функция работает правильно

    def test_linear_cut_method(self):
        original_length = 100
        cuts_length = [20, 30, 40]
        cuts_count = [2, 2, 2]
        result = linear_cut_method(original_length, cuts_length, cuts_count)
        # Добавьте проверки результата, чтобы убедиться, что функция работает правильно

if __name__ == '__main__':
    unittest.main()