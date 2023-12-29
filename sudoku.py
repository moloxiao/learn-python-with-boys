
from ex02.module import print_sudoku, cal_wait_numbers, cal_point, _cal_coordinate

sudoku_data = [
    0, 0, 9, 7, 2, 0, 4, 6, 0,
    4, 7, 0, 0, 0, 5, 0, 0, 0,
    0, 6, 2, 0, 3, 0, 7, 9, 0,
    0, 5, 6, 0, 8, 0, 0, 7, 4,
    0, 0, 0, 9, 0, 7, 0, 0, 0,
    9, 2, 0, 0, 4, 0, 1, 5, 0,
    0, 8, 5, 0, 1, 0, 2, 3, 0,
    0, 0, 0, 5, 0, 0, 0, 1, 6,
    0, 1, 3, 0, 6, 2, 5, 4, 9,
]

# print_sudoku(sudoku_data)
# wait_numbers = cal_wait_numbers(sudoku_data)
# print(f'wait cal numbers : {wait_numbers}')

for i in range(len(sudoku_data)):
    if sudoku_data[i] == 0:
        result = cal_point(sudoku_data, i)
        if result != 0 : # 获得了结果
            sudoku_data[i] = result
            point = _cal_coordinate(i)
            print(f' pos : {point.pos}, y={point.y}, x={point.x} get number : {result}')






