from helpers import readlines

def main():
    """Main function for the day2 challenge"""

    data = readlines('inputs/day2_input.txt')

    part1_solution = part1(data)
    part2_solution = part2(data)

    print(f'Part 1 solution is: {part1_solution}')
    print(f'Part 2 solution is: {part2_solution}')

def part1(data: list) -> int:
    """Day 2, first part.

    Objective: find the number of valid passwords in data.
    One row in data is as follows:
    {num1}-{num2} {letter}: {password}
    The password is valid if it contains {letter} between {num1} and {num2} times.

    Parameters
    ----------
    data : list
        The data to process

    Returns
    -------
    num_valid_passwords : int
        The number of valid passwords in data
    """

    num_valid_passwords = 0

    for row in data:

        processed = process_policy(row)
        cnt_letter = processed['password'].count(processed['policy_letter'])

        if cnt_letter in range(
            processed['policy_num_from'],
            processed['policy_num_to'] + 1
        ):

            num_valid_passwords += 1

    return num_valid_passwords

def part2(data: list) -> int:
    """Day 2, second part.

    Objective: find the number of valid passwords in data.
    One row in data is as follows:
    {num1}-{num2} {letter}: {password}
    The password is valid if it contains {letter} AT position {num1}
    OR AT position {num2} (but not both!)

    Parameters
    ----------
    data : list
        The data to process

    Returns
    -------
    num_valid_passwords : int
        The number of valid passwords in data
    """

    num_valid_passwords = 0

    for row in data:

        processed = process_policy(row)

        password = processed['password']
        letter = processed['policy_letter']

        # Subtracting 1 from each position because they are 1-indexed
        pos1 = processed['policy_num_from'] - 1
        pos2 = processed['policy_num_to'] - 1

        try:
            if xor(password[pos1] == letter, password[pos2] == letter):
                num_valid_passwords += 1
        except IndexError:
            continue

    return num_valid_passwords

def xor(a: bool, b: bool) -> bool:
    """Exclusive or. Returns true if a or b
    are true, but false if both are true.

    Parameters
    ----------
    a : bool
    b : bool

    Returns
    -------
    bool : bool
        The result of the xor operation
    """

    return (a and not b) or (not a and b)

def process_policy(policy: str) -> dict:
    """To process a row of data,
    because it's needed in both examples.

    Parameters
    ----------
    policy : str
        The policy in the format of {num1}-{num2} {letter}: {password}

    Returns
    -------
    processed : dict
        The processed policy with all needed values
    """

    split = policy.split(': ')
    policy = split[0]
    password = split[1]

    policy_split = policy.split(' ')
    policy_nums = policy_split[0].split('-')
    policy_num_from = int(policy_nums[0])
    policy_num_to = int(policy_nums[1])
    policy_letter = policy_split[1]

    processed = {
        'password': password,
        'policy_num_from': policy_num_from,
        'policy_num_to': policy_num_to,
        'policy_letter': policy_letter
    }

    return processed



if __name__ == "__main__":
    main()

