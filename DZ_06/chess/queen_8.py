import random

# Расстановка ферзей
def queens ():
    queens_position = []
    position = []
    row = [0, 1, 2, 3, 4, 5, 6, 7]
    column = [0, 1, 2, 3, 4, 5, 6, 7]
    
    while row:
        position = []
        position.append(random.choice(row))
        row.remove(position[0])
        
        if len(queens_position) != 0:
            while True:
                count = 0
                for queen in queens_position:
                    position.append(random.choice(column))
                    # print(queen, position)
                    if (queen[0] - position[0]) == (position[1] - queen[1]) or\
                    (queen[0] - position[1]) == (queen[1] - position[0]) or\
                    queen[0] == position[0] or\
                    queen[1] == position[1]:
                        position.pop()
                        count += 1
                
                if count == 0: 
                    queens_position.append(position)
                    column.remove(position[1])
                    position = []
                    break
                break

        else:        
            position.append(random.choice(column))
            column.remove(position[1])
            queens_position.append(position)
            position = []
            
        
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