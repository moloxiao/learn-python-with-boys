
class Point:
    def __init__(self, pos, x, y):
        self.pos = pos
        self.x = x
        self.y = y



def print_sudoku(sudoku_data):
    for i in range(len(sudoku_data)):
        print(sudoku_data[i], end=' ')
        if (i + 1) % 9 == 0:
            print()

def cal_wait_numbers(sudoku_data):
    wait_numbers = 0
    for i in range(len(sudoku_data)):
        if sudoku_data[i] == 0:
            wait_numbers = wait_numbers+1
    return wait_numbers

def cal_point(sudoku_data, pos):
    # print(f'cal position : {pos}')
    use_numbers = _allow_numbers(sudoku_data, pos)
    numbers = 0
    if(len(use_numbers) >= 8):
        # 计算可以填写的数字
        numbers = find_missing_number(use_numbers)
    return numbers
    

# --------------------------------------------------------------------------------
# internal function 
# --------------------------------------------------------------------------------
    
# x [1, 9]; y [1, 9]
def _cal_coordinate(pos):
    x = (pos+1)%9
    if x == 0:
        x = 9
    y = int(pos/9) + 1
    point = Point(pos, x, y)
    return point
    
def _allow_numbers(sudoku_data, pos):
    """
    计算允许填写的数字

    Parameters:
    sudoku_data (list): sudoku data
    point (Point) : current point.
    use_numbers (list) : 前面计算已经存在的数字

    Returns:
    list : 添加了横坐标已经存在数字的新数组
    """
    point = _cal_coordinate(pos) 
    # print(f'point.pos ={point.pos}, point.x ={point.x},point.y ={point.y}')
    use_numbers = _use_numbers_in_vertical(sudoku_data, point) # 1 竖排有没有重复
    use_numbers = _use_numbers_in_horizontal(sudoku_data, point, use_numbers)# 2 横排有没有重复
    use_numbers = list(set(use_numbers))
    # 3 小三角有没有重复

    return use_numbers

    # for i in range(len(use_numbers)):
    #     print(use_numbers[i])

def _use_numbers_in_vertical(sudoku_data, point):
    """
    检查纵坐标的已经存在的数字

    Parameters:
    sudoku_data (list): sudoku data
    point (Point) : current point.

    Returns:
    list : 添加了纵坐标已经存在数字的数组
    """
    use_numbers = []

    for i in range(9):
        if(i + 1 != point.y and sudoku_data[i*9+point.x-1] != 0):
            use_numbers.append(sudoku_data[i*9+point.x-1])

    return use_numbers


def _use_numbers_in_horizontal(sudoku_data, point, use_numbers):
    """
    检查横坐标的已经存在的数字

    Parameters:
    sudoku_data (list): sudoku data
    point (Point) : current point.
    use_numbers (list) : 前面计算已经存在的数字

    Returns:
    list : 添加了横坐标已经存在数字的新数组
    """
    for i in range(9):
        if(i + 1 != point.x and sudoku_data[9*(point.y-1) + i] != 0):
            use_numbers.append(sudoku_data[9*(point.y-1) + i])
    return use_numbers

def find_missing_number(arr):
    # The complete set of numbers from 1 to 9
    complete_set = set(range(1, 10))
    
    # Convert the input array to a set
    arr_set = set(arr)

    # Find the difference between the complete set and the array set
    missing_number = complete_set - arr_set

    # Return the missing number (there should be only one)
    return missing_number.pop()