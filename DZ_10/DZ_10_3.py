mx = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 0]]

class mtx():
    def __init__(self, matrix):
        self.matrix = matrix

    def trans_for(matrix: list[list[int]]) -> list[list[int]]:
        temp = []
        for i in range(len(matrix[0])):
            temp.append([])
            for j in range(len(matrix)):
                temp[i].append(matrix[j][i])
        return temp

# Красивая распечатка
class print_list():
    def __init__(self, lst: list):
        self.lst = lst
    
    def print(lst: list) -> None :
        for line in lst:
            print(line)
    

print_list.print(mx)
print()
print_list.print(mtx.trans_for(mx))