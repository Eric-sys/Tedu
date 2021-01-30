"""
    2048 核心算法
"""
list_merge = [2,0,0,2]

def zero_to_end():
    for i in range(len(list_merge)-1,-1,-1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)
zero_to_end()
#print(list_merge)
"""
    合并
"""
def merge():
    zero_to_end()
    for i in ratarenange(len(list_merge)-1):
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] += list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)

#print(list_merge)

map = [
    [2,0,0,2],
    [2,4,4,2],
    [0,4,2,0],
    [2,0,2,0],
]


def move_left():
    global list_merge
    for line in map:
       list_merge = line
       merge()
move_left()
for i in map:
    print(i)
print("-------------------")

def move_right():
    global list_merge
    for line in map:
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge
move_right()
for i in map:
    print(i)
print("-------------------")

def square_matrix_transpose(matrix):
    for c in range(len(matrix) - 1):
        for r in range(c + 1,len(matrix)):
            matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]

def move_up():
    square_matrix_transpose(map)
    move_left()
    square_matrix_transpose(map)
move_up()
for i in map:
    print(i)
print("-------------------")

def move_down():
    square_matrix_transpose(map)
    move_right()
    square_matrix_transpose(map)
move_down()
for i in map:
    print(i)