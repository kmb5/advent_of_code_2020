from helpers import readlines

def main():
    """Solution for day 8."""

    data = readlines('inputs/day8_input.txt')

    part1_solution = part1(data)
    part2_solution = part2(data)

    print(f'Part 1 solution: {part1_solution}')
    print(f'Part 2 solution: {part2_solution}')

def part1(data: list) -> int:
    """Objective:
    Run the computer and stop immediately
    before any instruction is executed a second time.
    The solution is the value in the accumulator at that point.

    Parameters
    ----------
    data : list
        The boot code to run, parsed as a list of rows
    
    Returns
    -------
    accumulator : int
        The value in the accumulator before the computer would execute
        an instruction the second time

    """

    return_value = _run_computer(data)
    return return_value['accumulator']

def part2(data: list) -> int:
    """Objective: In the boot code,
    either one jmp or one nop instruction is wrong.
    If this instruction is fixed, the computer will exit normally.
    Find and correct the wrong instruction and run the correct code.
    The solution is the accumulator value after normal exit.
    
    Parameters
    ----------
    data : list
        The boot code to run, parsed as a list of rows
    
    Returns
    -------
    accumulator : int
        The value in the accumulator after the successful run

    """

    all_data = _prepare_data_for_pt2(data)

    for data in all_data:
        # try all possibilities prepared above

        return_value = _run_computer(data)
        if return_value['exit_reason'] == 'normal_exit':
            return return_value['accumulator']

def _run_computer(data: list) -> dict:
    """Run the computer until it either exits normally,
    which happens when the next instruction it would execute would be
    one row after the last row of data,
    or until right before it would enter an infinite loop,
    which is when it would execute the instruction at the same address
    for the second time.

    Parameters
    ----------
    data : list
        The list of instruction rows it should execute

    Returns
    -------
    dict : dict
        A dict with the following keys:
        - exit_reason : normal_exit or infinite_loop as derscribed above
        - address_value : the address value at exit
        - accumulator : the value of the accumulator at exit

    """

    accumulator = 0
    address = 0
    previous_addresses = []

    while True:

        if address == len(data):
            # would execute the instruction
            # after the last row of data
            # --> normal termination
            return {
                'exit_reason': 'normal_exit',
                'address_value': address,
                'accumulator': accumulator
            }
        
        instruction = _parse_instruction(data[address])

        if address in previous_addresses:
            # would execute an instruction
            # which it already executed previously
            # --> infinite loop
            return {
                'exit_reason': 'infinite_loop',
                'address_value': address,
                'accumulator': accumulator
            }

        # keep track of all previously visited addresses
        previous_addresses.append(address)

        if instruction[0] == 'acc':
            # add the instruction parameter to
            # accumulator and continue to next instruction
            accumulator += instruction[1]
            address += 1
        elif instruction[0] == 'jmp':
            # jump to instruction relative to the current one
            # the parameter tells the offset to which instruction to jump
            address = address + instruction[1]
        else:
            # no operation, continue to next instruction
            address += 1

def _prepare_data_for_pt2(data: list) -> list:
    """To find which of the nop or jmp
    instructions are wrong, we need to consider
    and try all possibilities.
    This function builds all possible variations
    of the data with the nop codes replaced by jmp 
    and vice versa.

    Parameters
    ----------
    data : list
        The original boot code
    
    Returns
    -------
    copies : list[list]
        A 2d list where each inner list is a copy of the original
        boot code with one 'nop' or 'jmp' parameter interchanged

    """

    # start the list of copies with the original boot code
    # (even if we know it's not the working one)
    copies = [data]

    for i, line in enumerate(data):

        instruction = _parse_instruction(line)[0]

        if instruction in ('nop', 'jmp'):

            replace_with = 'nop' if instruction == 'jmp' else 'jmp'

            # copy the original array
            data_chng = data[:]

            # change only one item per loop
            data_chng[i] = data_chng[i].replace(instruction, replace_with)

            # append the full array as a copy to the list of copies
            copies.append(data_chng)

    return copies

def _parse_instruction(line: str) -> list:
    """Parses one line of instruction
    and returns the instruction and the parameter separately

    Parameters
    ----------
    line : str
        One line of instruction to parse

    Returns
    -------
    list : list
        A parsed instruction: [instruction(str), argument(int)]

    """

    split = line.split(' ')
    instruction, argument = split

    return [instruction, int(argument)]

if __name__ == "__main__":
    main()
    