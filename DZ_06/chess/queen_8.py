import random

def queen_attack (queens_pos: list[list], position: list[int]) -> bool:
    for queen in queens_pos:
        if(queen[0] - position[0]) == (position[1] - queen[1]) or\
        (queen[0] - position[1]) == (queen[1] - position[0]) or\
        queen[0] == position[0] or\
        queen[1] == position[1]:
            return False
    return True

# Расстановка ферзей
def queens ():
    queens_position = []
    position = [0, 0]
    row = [0, 1, 2, 3, 4, 5, 6, 7]
    column = [0, 1, 2, 3, 4, 5, 6, 7]
    stat = True
    
    position[0] = random.choice(row)
    position[1] = random.choice(column)
    row.remove(position[0])
    column.remove(position[1])
    queens_position.append(position)
    print(queens_position)
    
    while len(row):
        position[0] = random.choice(row)
        row.remove(position[0])
        stat = True
        while stat:
            # print(position)
            position[1] = random.choice(column)
            print(queen_attack(queens_position, position))
            if queen_attack(queens_position, position):
                stat = False 
        queens_position.append(position)
        column.remove(position[1])
        print(position)       
    return queens_position

print(queens())



# # ферзи по диагонали слева направо, снизу верх
# (queen[0] - position[0]) == (position[1] - queen[1])
# # ферзи по диагонали слева направо, сверзу вниз
# (queen[0] - position[1]) == (queen[1] - position[0])
# # ферзи по горизонтали в линии
# queen[0] == position[0]
# # ферзи по вертикали в линии
# queen[1] == position[1]