import time
from ex02.module import print_sudoku, cal_wait_numbers, cal_point, _cal_coordinate

easy = [
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

hard = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
]

sudoku_data = [
    8, 4, 0, 1, 0, 0, 9, 0, 0,
    6, 0, 0, 7, 9, 0, 4, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 3, 0, 0, 5, 1, 9, 0,
    0, 6, 0, 0, 0, 1, 0, 0, 0,
    0, 0, 0, 0, 8, 0, 7, 5, 0,
    7, 5, 8, 0, 0, 0, 0, 3, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 5,
    0, 0, 0, 0, 2, 0, 8, 7, 0,
]

# print_sudoku(sudoku_data)
# wait_numbers = cal_wait_numbers(sudoku_data)
# print(f'wait cal numbers : {wait_numbers}')

going = True
wait_numbers = cal_wait_numbers(sudoku_data)
round = 0
all_slove_numbers = 0

start_time = time.time()
while(going):
    round = round+1
    round_slove_numbers = 0
    print(f'round{round}-start, wait_numbers={wait_numbers}')
    for i in range(len(sudoku_data)):
        if sudoku_data[i] == 0:
            result = cal_point(sudoku_data, i)
            if result != 0 : # 获得了结果
                sudoku_data[i] = result
                point = _cal_coordinate(i)
                round_slove_numbers = round_slove_numbers + 1
                all_slove_numbers = all_slove_numbers + 1
                print(f'----pos : {point.pos}, y={point.y}, x={point.x} get number : {result}')

    print(f'round{round}-end, round slove numbers={round_slove_numbers}, all_slove_numbers={all_slove_numbers}')
    new_wait_numbers = cal_wait_numbers(sudoku_data)
    if(new_wait_numbers == wait_numbers):
        going = False
        print()
        print('-----END-----')
        print(f'Stop. all slove numbers={all_slove_numbers}, wait numbers={new_wait_numbers}')

    if(new_wait_numbers == 0):
        going = False
        print()
        print('-----END-----')
        print('Success finish...')
        print_sudoku(sudoku_data)
    
    wait_numbers = new_wait_numbers
    print()

end_time = time.time()
execution_time = end_time - start_time
print(f"My function took {execution_time} seconds to execute.")




