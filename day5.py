from math import floor
from helpers import readlines

def main():
    """Solution for day 5."""

    data = readlines('day5_input.txt')
    seats = _calculate_seat_ids(data)
    seat_ids = [s['seat_id'] for s in seats]

    part1_solution = part1(seat_ids)
    part2_solution = part2(seat_ids)
    
    print(f'Part 1 solution: {part1_solution}')
    print(f'Part 2 solution: {part2_solution}')

def part1(seat_ids: list) -> int:
    """Objective: find the highest seat ID
    (how seats are parsed is described in
    _calculate_seat_ids)

    Parameters
    ----------
    seat_ids : list
        The list of seat IDs to check

    Returns
    -------
    highest_seat_id : int
        The highest seat ID in the list

    """

    highest_seat_id = max(seat_ids)
    return highest_seat_id

def part2(seat_ids: list) -> int:
    """Objective: find our seat which is the only
    missing seat ID in the list of seat IDs

    Parameters
    ----------
    seat_ids : list
        The list of seat IDs to check

    Returns
    -------
    int : int
        The missing (our) seat ID
    """

    seat_ids.sort()

    for i, sid in enumerate(seat_ids):

        if seat_ids[i+1] != sid + 1:
            # It means the next seat ID is not an increment by one
            # which means it is our seat
            return sid + 1

def _calculate_seat_ids(data: list) -> list:
    """To calculate the seat IDs from the puzzle input.

    A seat is specified as 10 characters -
    the first 7 are for the row, the last 3 are for the column.

    There are 127 rows (0-127) and 8 columns (0-7).
    To find the row and column number, go through the list and:
    - If character is F, keep the lower half of the rows
    - If character is B, keep the upper half of the rows
    - If character is L, keep the lower half of the columns
    - If character is R, keep the upper half of the columns

    At the end, the seat ID is calculated by row * 8 + col

    Parameters
    ----------
    data : list
        The puzzle input as a list
    seat_ids : list[dict]
        A list of dicts with row, col and seat_id as keys
        (we only need seat ID but I wanted to check some inputs
        if I get the correct row and col)

    """

    seat_ids = []

    for row in data:
        
        rows = list(range(128))
        cols = list(range(8))

        for char in row:
            
            half_row = floor(len(rows) / 2)
            half_col = floor(len(cols) / 2)

            if char == 'F':
                rows = rows[:half_row]
            elif char == 'B':
                rows = rows[half_row:]
            elif char == 'L':
                cols = cols[:half_col]
            elif char == 'R':
                cols = cols[half_col:]

        row = rows[0]
        col = cols[0]
        seat_id = row * 8 + col

        seat_ids.append({
            'row': row,
            'col': col,
            'seat_id': seat_id
        })

    return seat_ids

if __name__ == "__main__":
    main()