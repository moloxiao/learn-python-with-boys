
class Point:
    def __init__(self, pos, x, y):
        self.pos = pos
        self.x = x
        self.y = y

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

def _cal_pos_by_coordinate(pont):
    pos = (pont.y-1)*9 + pont.x - 1
    return pos

def small_triangle_toppoint(x, y):
    x1 = int((x-1)/3) + 1
    y1 = int((y-1)/3) + 1
    
    x2 = (x1-1)*3 + 1
    y2 = (y1-1)*3 + 1

    print(f'result = x2={x2}, y2={y2}')

    for y in range(3):
        for x in range(3):
            y1 = y2 + y
            x1 = x2 + x
            pos = _cal_pos_by_coordinate(Point(0, x1, y1))
            print(sudoku_data[pos])

print('test1')
print('input x=3, y=4, hope x2=1, y2=4')
small_triangle_toppoint(3, 4)

# print()

# print('test2')
# print('input x=5, y=6, hope x2=4, y2=4')
# small_triangle_toppoint(5, 6)