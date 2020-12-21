from helpers import readlines
from tqdm import tqdm

def main():

    data = readlines('inputs/day17_input.txt')

    part1_solution = part1(data)
    part2_solution = part2(data)

    print('\n\n\n')
    print(f'Part 1 solution: {part1_solution}')
    print(f'Part 2 solution: {part2_solution}')

def part1(data):

    print()
    print('='*16 + ' Part 1 ' + '='*16)
    print()

    ON = set()

    for x,row in enumerate(data):
        for y,char in enumerate(row):
            if char == '#':
                ON.add((x,y,0))

    for r in range(6):
        # 6 turns
        print(f'Turn {r+1}')
        NEW_ON = set()
        for x in tqdm(max_range(0, ON)):
            for y in max_range(1, ON):
                for z in max_range(2, ON):
                    nbrs = 0
                    for dx in [-1,0,1]:
                        for dy in [-1,0,1]:
                            for dz in [-1,0,1]:
                                if dx != 0 or dy != 0 or dz != 0:
                                    if (x + dx, y + dy, z + dz) in ON:
                                        nbrs += 1
                        
                    if (x,y,z) not in ON and nbrs == 3:
                        NEW_ON.add((x,y,z))
                    if (x,y,z) in ON and nbrs in [2,3]:
                        NEW_ON.add((x,y,z))
        
        ON = NEW_ON
    
    return len(ON)
    

def part2(data):

    print()
    print('='*16 + ' Part 2 ' + '='*16)
    print()
    
    ON = set()

    for x,row in enumerate(data):
        for y,char in enumerate(row):
            if char == '#':
                ON.add((x,y,0,0))

    for r in range(6):
        # 6 turns
        print(f'Turn {r+1}')
        NEW_ON = set()
        for x in tqdm(max_range(0, ON)):
            for y in max_range(1, ON):
                for z in max_range(2, ON):
                    for w in max_range(3, ON):
                        nbrs = 0
                        for dx in [-1,0,1]:
                            for dy in [-1,0,1]:
                                for dz in [-1,0,1]:
                                    for dw in [-1, 0, 1]:
                                        if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                                            if (x + dx, y + dy, z + dz, w + dw) in ON:
                                                nbrs += 1
                        
                        if (x,y,z, w) not in ON and nbrs == 3:
                            NEW_ON.add((x,y,z, w))
                        if (x,y,z, w) in ON and nbrs in [2,3]:
                            NEW_ON.add((x,y,z, w))
        
        ON = NEW_ON
    
    return len(ON)

def max_range(idx, ON):
    return range(min(p[idx] for p in ON) - 1, max(p[idx] for p in ON) + 2)

if __name__ == "__main__":
    main()