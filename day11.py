from helpers import readlines
from collections import Counter
from pprint import pprint
from copy import deepcopy

def main():

    data = readlines('inputs/day11_test_input.txt')
    data = [[*word] for word in data]

    part2(data)

def part1(data):

    data_copy = deepcopy(data)
    prev_run = []

    rounds = 0

    while data_copy != prev_run:
        prev_run = data_copy
        data_copy = rule_round(data_copy)
        rounds += 1
        print(rounds)

    seats = [Counter(x)['#'] for x in data_copy]
    print(sum(seats))

def part2(data):


    data_copy = deepcopy(data)
    prev_run = []

    rounds = 0

    #data_copy_2 = deepcopy(rule_round_pt2(data_copy))

    #data_copy_3 = deepcopy(rule_round_pt2(data_copy_2))

    start = [['#', '.', '#', '#', '.', '#', '#', '.', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '.', '#', '#'],
        ['#', '.', '#', '.', '#', '.', '.', '#', '.', '.'],
        ['#', '#', '#', '#', '.', '#', '#', '.', '#', '#'],
        ['#', '.', '#', '#', '.', '#', '#', '.', '#', '#'],
        ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#'],
        ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#']]

    rule_round_pt2(start)


    #pprint(data_copy)
    #pprint(data_copy_2)
    #pprint(data_copy_3)

    #seats = [Counter(x)['#'] for x in data_copy]
    #print(sum(seats))



def rule_round(data):

    changed_data = deepcopy(data)
    #print(data)

    for i, row in enumerate(data):
        for j, seat in enumerate(row):

            adjacent = gen_adjacent_node(data, (i,j))
            #print(adjacent)

            adjacent_els = []
            for c in adjacent:
                c_y = c[0]
                c_x = c[1]
                adjacent_els.append(data[c_y][c_x])
            #print(adjacent_els)

            count_occupied = Counter(adjacent_els)['#']
            #print(count_occupied)
            
            if seat == 'L' and '#' not in adjacent_els:
                changed_data[i][j] = '#'
            if seat == '#' and count_occupied >= 4:
                changed_data[i][j] = 'L'
        
    return changed_data

def rule_round_pt2(data):


    changed_data = deepcopy(data)
    pprint(data)

    for i, row in enumerate(data):
        counts = []
        for j, seat in enumerate(row):

            adjacent = count_adjacent_nodes_pt2(data, (i,j))
            counts.append(adjacent)
            
            if seat == 'L' and adjacent == 0:
                changed_data[i][j] = '#'
            if seat == '#' and adjacent >= 5:
                changed_data[i][j] = 'L'

        print(counts)
        
    return changed_data



def gen_adjacent_node(matrix_2d, node=(0,0)):
    adj_nodes = []
    rows = len(matrix_2d)
    columns = len(matrix_2d[0])
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == c == 0:
                continue
            # check valid index
            if 0 <= node[0]+r < rows and 0 <= node[1]+c < columns:
                # print((node[0]+i, node[1]+j))
                adj_nodes.append((node[0]+r, node[1]+c))

    return adj_nodes


def count_adjacent_occupied_v2(matrix=None, node=(0,0)):

    num_adjacent_occupied = 0

    data = [['#', '.', '#', '#', '.', '#', '#', '.', '#', '#'],
 ['#', '#', '#', '#', '#', '#', '#', '.', '#', '#'],
 ['#', '.', '#', '.', '#', '.', '.', '#', '.', '.'],
 ['#', '#', '#', '#', '.', '#', '#', '.', '#', '#'],
 ['#', '.', '#', '#', '.', '#', '#', '.', '#', '#'],
 ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#'],
 ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'],
 ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
 ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#'],
 ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#']]

    matrix = data

    starting_y = node[0]
    starting_x = node[1]

    if starting_y == 0:
        # we are in first row
        if starting_x == 0 or starting_x == len(data):
            # we are in corner

    row_of_node = matrix[starting_y]
    column_of_node = [n[starting_y] for n in matrix]

    # check row
    left = row_of_node[:starting_y]
    right = row_of_node[starting_y+1:]

    if '#' in left:
        num_adjacent_occupied += 1
    if '#' in right:
        num_adjacent_occupied += 1

    # check col
    top = column_of_node[:starting_x]
    bottom = column_of_node[starting_x+1:]

    print(top)
    print(bottom)





def count_adjacent_nodes_pt2(matrix_2d, node=(0,0)):

    num_adj = 0
    #pprint(matrix_2d)

    # node = (4,3)
    cpy = deepcopy(matrix_2d)
    new_arr = []
    
    # traverse horizontally
    horiz = cpy[node[0]]
    if Counter(horiz)['#'] > 0:
        num_adj += 1
        print('vertical yes')

    #traverse vertically
    vertic = [row[node[1]] for row in cpy]
    if Counter(vertic)['#'] > 0:
        num_adj += 1
        print('horizontal yes')

    #traverse diagonally
    a,b,c,d = 1,1,1,1
    while True:
        offset1 = node[0] + a
        offset2 = node[1] + a
        try:
            if offset1 > 0 and offset2 > 0:
                next_node = cpy[offset1][offset2]
                if next_node == '#':
                    num_adj += 1
                    print('d1 yes')
                    break
                a += 1
            else:
                break
        except IndexError:
            break
    
    while True:
        offset1 = node[0] + b
        offset2 = node[1] + b
        try:
            if offset1 > 0 and offset2 > 0:
                next_node = cpy[offset1][offset2]
                if next_node == '#':
                    num_adj += 1
                    print('d2 yes')
                    break
                b += 1
            else:
                break
        except IndexError:
            break

    while True:
        offset1 = node[0] + c
        offset2 = node[1] + c
        try:
            if offset1 > 0 and offset2 > 0:
                next_node = cpy[offset1][offset2]
                if next_node == '#':
                    num_adj += 1
                    print('d3 yes')
                    break
                c += 1
            else:
                break
        except IndexError:
            break
    
    while True:
        offset1 = node[0] + d
        offset2 = node[1] + d
        try: 
            if offset1 > 0 and offset2 > 0:
                next_node = cpy[offset1][offset2]
                if next_node == '#':
                    num_adj += 1
                    print('d4 yes')
                    break
                d += 1
            else:
                break
        except IndexError:
            break

    #print(num_adj)
    return num_adj


if __name__ == "__main__":
    count_adjacent_occupied_v2()