import pulp


# -----------------------------------------------------------------------------------------------------------------------
# подсчет комбинаций из заданного количества
def find_closest_combinations(target, limits, prices, count):
    combinations = []

    def find_combination(_sum, index, current):
        if index == count:
            if _sum <= target:
                combinations.append(current[:])
            return

        for i in range(limits[index] + 1):
            new_sum = _sum + i * prices[index]
            if new_sum <= target:
                current.append(i)
                find_combination(new_sum, index + 1, current)
                current.pop()
            else:
                break

    find_combination(0, 0, [])
    return [list(map(lambda x, y: x * y, combination, prices)) for combination in combinations]


# -----------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------
def count_remains(comb, L, cuts):
    result = []
    for i in range(len(comb)):
        sum_comb = sum(comb[i])
        remain = L - sum_comb
        comb[i].append(remain)

    for i in range(len(comb)):
        remain = comb[i][-1]

        for cut in range(len(cuts)):
            if remain > cuts[cut]:
                comb[i].append(1)

    for i in range(len(comb)):
        flag = comb[i][-1]
        if flag != 1:
            result.append(comb[i])

    return result


# -----------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------
# подсчет реза каждого размера
def do_count_cut(comb, cuts):
    for i in range(len(comb)):
        for j in range(len(cuts)):
            comb[i][j] = int(comb[i][j] / cuts[j])


# -----------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------
# транспонирование матрицы
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


# -----------------------------------------------------------------------------------------------------------------------


# [print(i,"ый вариант", combinations[i]) for i in range(len(combinations))]
# [print(comb_transpose[i]) for i in range(len(comb_transpose))]

# линейный раскрой с помощью линейного целочисленного программирования
def linear_cut_method(original_length, cuts_length, cuts_count):
    #print(original_length, cuts_length, cuts_count)
    # Создание экземпляра класса задачи
    prob = pulp.LpProblem("Paper Cutting Problem", pulp.LpMinimize)
    solver = pulp.GUROBI()
    #print(prob)

    # количество необходимых отрезков
    count = len(cuts_length)

    # считаем начальные карты раскроя
    closest_combinations = find_closest_combinations(original_length, cuts_count, cuts_length, count)
    #print(closest_combinations)
    # считаем остатки у каждой комбинации
    combinations = count_remains(closest_combinations, original_length, cuts_length)

    # преобразуем комбинации к нужному виду
    do_count_cut(combinations, cuts_length)

    # сохраняем комбинации без остатков
    new_comb = [combinations[i][:-1] for i in range(len(combinations))]

    # транспонируем комбинации для системы уравнений
    comb_transpose = transpose_matrix(new_comb)

    #print(comb_transpose)
    #print(new_comb)

    L = original_length

    # количество переменных = количеству комбинаций
    num_variables = len(combinations)

    # количество переменных
    x = [pulp.LpVariable(f'x{i}', lowBound=0, cat='Integer') for i in range(1, num_variables + 1)]
    #print(x)
    # задаем ограничения для каждог уравнения
    coefficients = [combinations[i][-1] for i in range(len(combinations))]
    #print(coefficients)

    prob += pulp.lpDot(coefficients, x)

    # задаем коэффициенты перед переменными
    constraints_coefficients = [tuple(comb) for comb in comb_transpose]

    # задаем правую часть уравнения
    rhs_values = cuts_count

    for i, constraint_coefficients in enumerate(constraints_coefficients):
        prob += pulp.lpDot(constraint_coefficients, x) == rhs_values[i]

    # Решение задачи
    prob.solve()

    # Вывод оптимального решения
    corresponding_column = []
    #print("Результат:")
    for v in prob.variables():
        if v.varValue != 0.0:
            var_index = int(v.name[1:]) - 1  # Получение индекса переменной из имени
            for j in range(int(v.varValue)):
                corresponding_column.append(combinations[var_index])
            #print(v.name, "=", v.varValue)

    for i in range(len(corresponding_column)):
        #print(corresponding_column[i])
        #str_res = ""
        remain = 0
        for j in range(len(corresponding_column[i]) - 1):
            if corresponding_column[i][j] != 0:
                remain += corresponding_column[i][j] * cuts_length[j]
                #str_res += "| " + str(cuts_length[j]) + " x" + str(corresponding_column[i][j]) + " |"

        #remain = L - remain
        #str_res += " + " + str(remain) + " " + " = " + str(L)
        # print(corresponding_column[i])
        #print(str_res)
    #print("Суммарная потеря материала:", pulp.value(prob.objective))
    #print(corresponding_column)

    return corresponding_column
