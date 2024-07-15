data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):  # подсчитывает сумму целочисленных значений и длин строк элементов и ключей в струкутре
    sum_str = 0
    for i in data:
        if isinstance(i, int) or isinstance(i, float):
            sum_str += i
        elif isinstance(i, str):
            sum_str += len(i)
        elif isinstance(i, dict):
            sum_str += calculate_structure_sum(i.keys())
            sum_str += calculate_structure_sum(i.values())
        else:
            sum_str += calculate_structure_sum(i)
    return sum_str


result = calculate_structure_sum(data_structure)
print(result)
