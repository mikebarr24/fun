# https://www.codewars.com/kata/549ee8b47111a81214000941/train/python


def mover(current_position):
    moves = [[1, 2], [1, -2], [-1, 2], [-1, -2],
             [2, 1], [2, -1], [-2, 1], [-2, -1]]
    arr = []
    for move in moves:
        x = current_position[0] + move[0]
        y = current_position[1] + move[1]
        if x >= 0 and y >= 0 and x <= 7 and y <= 7:
            arr.append([x, y])
    return arr


def knight(p1, p2):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
    matrix = []
    for letter in letters:
        demo = []
        for number in numbers:
            demo.append(letter+number)
        else:
            matrix.append(demo)
    positions = []
    for index, position in enumerate(matrix):
        if p1 in position:
            positions.append([index, position.index(p1)])
        if p2 in position:
            positions.append([index, position.index(p2)])
    moves = []
    num_moves = 0
    current_position = positions[0]
    while current_position != positions[1]:
        possible_positions = mover(current_position)
        saved_positions = possible_positions
        for index, position in enumerate(saved_positions):
            if positions[1] in possible_positions:
                current_position = position
            else:
                possible_positions = mover(saved_positions[index])
        num_moves += 1
    return num_moves


print(knight("a1", "c3"))
