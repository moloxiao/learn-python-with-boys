# sudoku

## V0.0.1

core algorithm(How to cal some point numbers) :
* check _use_numbers_in_vertical
* check _use_numbers_in_horizontal
* sum numbers, if numbers equals 8, get!!

test result :
| round | solve point | all solve point | wait point |
| :-----| ----: | :----: | :----: |
| 1 | 8 | 8 | |
| 2 | 4 | 12 | |
| 3 | 1 | 13 | |
| 4 | 0 | 13 | 28 |

## V0.0.2
core algorithm(How to cal some point numbers) :
* check _use_numbers_in_vertical
* check _use_numbers_in_horizontal
* (new)check _use_numbers_in_small_triangle
* sum numbers, if numbers equals 8, get!!

| round | v1-solve point | v1-all solve point | v2-solve point | v2-all solve point|
| :-----| ----: | :----: | :----: | :----: |
| 1 | 8 | 8 | 12|12 |
| 2 | 4 | 12 | 8|20 |
| 3 | 1 | 13 | 7|27 |
| 4 | 0 | 13 |  6|33 |
| 5 | 0 | 13 |  6|39 |
| 6 | 0 | 13 |  2|41 |

## V0.0.3
