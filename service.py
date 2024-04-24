import pulp


""" здесь начинается описание сервисных функций"""
""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

# функция поэлементного сравнения двух массивов
# ----------------------------------------------------------------------------------------------------------------------
def compare_equal(arr1, arr2):
    for el1, el2 in zip(arr1, arr2):
        if el1 != el2:
            return True
        else:
            return False
# ----------------------------------------------------------------------------------------------------------------------

# функция печати массива
# ----------------------------------------------------------------------------------------------------------------------
def print_arr(A):
    for i in range(len(A)):
        print(A[i])
# ----------------------------------------------------------------------------------------------------------------------

# поэлементное суммирование массива
# ----------------------------------------------------------------------------------------------------------------------
def sum_array(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        # Суммируем элементы поэлементно первых двух массивов
        sum_elements = arr1[i] + arr2[i]
        result.append(sum_elements)
    return result

# поэлементное сравнение элементов на превышение
# ----------------------------------------------------------------------------------------------------------------------
def sum_and_compare(arr1, arr2, arr3):
    result = sum_array(arr1, arr2)
    for i in range(len(result)):
        if result[i] > arr3[i]:
            return False
    return True
# ----------------------------------------------------------------------------------------------------------------------

# транспонирование матрицы
# ----------------------------------------------------------------------------------------------------------------------
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed
# ----------------------------------------------------------------------------------------------------------------------

# составление всех возможных карт раскроя, а также остатков, получаемых из каждой карты
# ----------------------------------------------------------------------------------------------------------------------
def linear_cutting(length, cut_lengths, cut_counts):
    def generate_cuts(length, cut_lengths, cut_counts, current_cut, result, remainders):
        if not cut_lengths:
            result.append(current_cut.copy() + cut_counts)
            remainders.append(length)
            return

        for i in range(min(length // cut_lengths[0], cut_counts[0]) + 1):
            generate_cuts(length - i * cut_lengths[0], cut_lengths[1:], cut_counts[1:], current_cut + [i], result,
                          remainders)

    result = []
    remainders = []
    generate_cuts(length, cut_lengths, cut_counts, [], result, remainders)
    return result, remainders

# ----------------------------------------------------------------------------------------------------------------------
""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """
""" здесь заканчивается описание сервисных функци"""

""" здесь начинается описание методов решения задач раскроя"""
""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """
# решение задачи линейного раскроя методом линейного программирования
# ----------------------------------------------------------------------------------------------------------------------
def linear_cut_method(original_length, cuts_length, cuts_count):
    # создаем карты раскроя и остатки
    possible_cuts, remainders = linear_cutting(original_length, cuts_length, cuts_count)

    # транспонируем матрицу для системы уравнений
    A = transpose_matrix(possible_cuts)

    # создаем описание задачи раскроя
    prob = pulp.LpProblem("Cutting Problem", pulp.LpMinimize)

    # создаем переменные, одна переменная - вариант раскроя
    num_variables = len(possible_cuts)
    x = [pulp.LpVariable(f'x{i}', lowBound=0, cat='Integer') for i in range(1, num_variables + 1)]

    # задаем функцию, которую нужно минизировать
    prob += pulp.lpDot(remainders, x)

    # задаем ограничения (коэффициенты справа)
    rhs_values = cuts_count

    # строим матрицу коэффициентов
    constraints_coefficients = [tuple(comb) for comb in A]

    # составляем систему уравнений
    for i, constraint_coefficients in enumerate(constraints_coefficients):
        prob += pulp.lpDot(constraint_coefficients, x) == rhs_values[i]

    # решаем систему уравнений
    prob.solve()

    # Вывод оптимального решения
    result_maps = []
    for v in prob.variables():
        if v.varValue != 0.0:
            var_index = int(v.name[1:]) - 1  # Получение индекса переменной из имени
            for j in range(int(v.varValue)):
                result_maps.append(possible_cuts[var_index])
            print(v.name, "=", v.varValue)

    print("Суммарная потеря материала:", pulp.value(prob.objective))
    print_arr(result_maps)

    return result_maps
# ----------------------------------------------------------------------------------------------------------------------

# решение задачи линейного раскроя жадным алгоритмом
# ----------------------------------------------------------------------------------------------------------------------
def find_optimal_maps(original_length, cuts_length, counts):
    maps, remains = linear_cutting(original_length, cuts_length, counts)
    for i in range(len(maps)):
        maps[i].append(remains[i])
    sorted_maps = sorted(maps, key=lambda x: (-x[0], x[-1]))
    selected_maps = []
    current_counts = [0]*len(counts)
    for i in range(len(sorted_maps)):
        if sorted_maps[i][-1] == 6000:
            continue
        temp_map = sorted_maps[i]
        temp_map = temp_map[:-1]
        if sum_and_compare(temp_map, current_counts, counts):
            selected_maps.append(sorted_maps[i])
            current_counts = sum_array(current_counts, temp_map)

    print_arr(selected_maps)
    return selected_maps
# ----------------------------------------------------------------------------------------------------------------------
""" здесь заканчивается описание сервисных функций"""
