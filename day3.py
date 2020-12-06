from helpers import readlines

def main():
    """Day3 solution"""

    data = readlines('inputs/day3_input.txt')

    part1_solution = traverse_map(data, right_step=3, down_step=1)
    part2_solution = part2(data)

    print(f'Part 1 solution: {part1_solution}')
    print(f'Part 2 solution: {part2_solution}')

def traverse_map(map_to_traverse: list, right_step: int, down_step: int) -> int:
    """Objective: Traverse the map
    that is in data by starting at the top left
    and count all # characters while traversing the
    map with stepping {right_step} number of steps right,
    and {down_step} number of steps down.
    If you get to the right, the map repeats again.

    Parameters
    ----------
    data : list
        The map to traverse
    right_step : int
        The number of (x-)coords to the right per step
    down_step : int
        The number of (y-)coords down per step
    
    Returns
    -------
    num_trees : int
        The number of trees encountered

    """

    num_trees = 0

    # Convert to a 2d array
    map_to_traverse = [[c for c in row] for row in map_to_traverse]

    x_coord = 0
    y_coord = 0

    while y_coord < len(map_to_traverse):

        # We need to wrap around if x_coord is bigger than
        # the length of the current row
        x_coord_norm = x_coord % len(map_to_traverse[y_coord])

        item_to_check = map_to_traverse[y_coord][x_coord_norm]
        
        if item_to_check == '#':
            num_trees += 1
        
        x_coord += right_step
        y_coord += down_step

    return num_trees

def part2(data) -> int:
    """Solution for part 2

    Returns
    -------
    part2_solution : int
        The result of multiplying together the
        number of trees encountered on each of the
        slopes in part2_slopes below

    """

    part2_slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    part2_solution = 1

    for slope in part2_slopes:

        num_trees = traverse_map(data, slope[0], slope[1])
        part2_solution *= num_trees
    
    return part2_solution

if __name__ == "__main__":
    main()