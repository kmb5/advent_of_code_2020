from helpers import readfile
from pprint import pprint

def main():
    
    data = readfile('inputs/day20_test_input.txt')

    tiles = data.split('\n\n')
    tiles = [x.split('\n') for x in tiles]
    #tiles = {i[0].replace('Tile ','').replace(':', ''): [[c for c in x] for x in i[1:]] for i in tiles}

    _rotate()
    return
    tiles = {i[0].replace('Tile ','').replace(':', ''): i[1:] for i in tiles}

    all_edges = {}

    for tile in tiles:
        t = tiles[tile]
        edges_with_reversed = []
        edges = [
            t[0],
            t[-1],
            ('').join([x[0] for x in t]),
            ('').join([x[-1] for x in t])
        ]
        for edge in edges:
            edges_with_reversed.append(edge)
            edges_with_reversed.append(('').join(list(reversed(edge))))
        
        for edge in edges_with_reversed:

            if not all_edges.get(edge):
                all_edges[edge] = [tile]
            else:
                all_edges[edge].append(tile)

    x = [(k,v) for k,v in all_edges.items() if '1171' in v]
    print(x)


        
def _rotate(tile=None):

    if not tile:
        tile = [['#', '.', '#', '.', '#', '#', '#', '#', '#', '.'],
          ['.', '#', '.', '.', '#', '#', '#', '#', '#', '#'],
          ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
          ['#', '#', '#', '#', '#', '#', '.', '.', '.', '.'],
          ['#', '#', '#', '#', '.', '#', '.', '.', '#', '.'],
          ['.', '#', '.', '.', '.', '#', '.', '#', '#', '.'],
          ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#'],
          ['.', '.', '#', '.', '#', '#', '#', '.', '.', '.'],
          ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '#', '.', '#', '#', '#', '.', '.', '.']]
    
    rotations = []
    to_rotate = tile
    vertically_flipped = [row for row in tile[::-1]]
    
    
    
    pprint(rotations)

    


    





if __name__ == "__main__":
    main()