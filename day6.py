from helpers import readfile

def main():
    """Day 6 solution"""

    data = readfile('day6_input.py')

    part1_solution = part1(data)
    part2_solution = part2(data)

    print(f'Part 1 solution: {part1_solution}')
    print(f'Part 2 solution: {part2_solution}')


def part1(data: str) -> int:
    """Objective:
    Count the unique letters in each row.

    Parameters
    ----------
    data : str
        The raw puzzle input
    
    Returns
    -------
    sum : int
        The sum of unique letters for each row

    """

    split = data.split('\n\n')
    answers = [x.replace('\n', '') for x in split]

    counts = [len(set(x)) for x in answers]

    return sum(counts)

def part2(data: str) -> int:
    """Objective: Count the letters
    which appear in all rows

    (I hate this code but this is what
    I could come up with)

    Parameters
    ----------
    data : str
        The raw puzzle input
    
    Returns
    -------
    sum : int
        The sum of all letters which appear 
        in all rows of a group

    """

    # test data:
    # data = '''abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb'''
    all_pts = []

    split = data.split('\n\n')
    groups = [x.split('\n') for x in split]

    for row in groups:

        first_row = row[0]
        pts = 0

        if len(row) == 1:
            # If there is only one row
            # for the group, all letters
            # appear in all rows,
            # so we have as many unique letters
            # as there are letters in the row

            all_pts.append(len(row[0]))
            continue

        for letter in first_row:

            # For each letter in the first row,
            # check if it is in all the following rows

            letter_in_how_many_rows = 0

            for row_to_check in row[1:]:

                if letter in row_to_check:
                    # the letter is in the following row
                    letter_in_how_many_rows += 1

            if letter_in_how_many_rows == len(row[1:]):
                # The letter is in ALL following rows
                pts += 1

        all_pts.append(pts)

    return sum(all_pts)


if __name__ == "__main__":
    main()