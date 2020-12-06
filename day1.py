from helpers import readlines

def main():
    """Main function for the day1 challenge"""

    inp = readlines('inputs/day1_input.txt')
    inp = [int(x) for x in inp]

    day1_pt1_answer = day1_pt1(inp)
    day1_pt2_answer = day1_pt2(inp)

    print(f'Part 1 answer is {day1_pt1_answer}')
    print(f'Part 2 answer is {day1_pt2_answer}')


def day1_pt1(data: list) -> int:
    """Day 1, first part.

    Objective: find the two entries in data
    that sum to 2020. The solution is the
    product of these two entries.

    Parameters
    ----------
    data : list
        The data to process
  
    Returns
    -------
    result : int
        The product of the two entries in data
        that sum to 2020
    """

    for i, num1 in enumerate(data):
        for num2 in data[i + 1:]:

            sum_entries = num1 + num2

            if sum_entries == 2020:
                return num1 * num2

def day1_pt2(data: list) -> int:
    """Day 1, second part.
    
    Objective: find the three entries in data
    that sum to 2020. The solution is the
    product of these three entries.

    Parameters
    ----------
    data : list
        The data to process
  
    Returns
    -------
    result : int
        The product of the three entries in data
        that sum to 2020
    """

    for i, num1 in enumerate(data):
        for j, num2 in enumerate(data[i + 1:]):
            for num3 in data[j + 1:]:

                sum_entries = num1 + num2 + num3

                if sum_entries == 2020:
                    return num1 * num2 * num3

if __name__ == "__main__":
    main()
