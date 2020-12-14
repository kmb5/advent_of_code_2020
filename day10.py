from helpers import readlines
from functools import reduce
import operator


def main():
    
    data = readlines('inputs/day10_input.txt')
    data = [int(l) for l in data]
    data.sort()

    part1_solution = part1(data)
    part2_solution = part2(data)

    print(f'Part 1 solution is {part1_solution}')
    print(f'Part 2 solution is {part2_solution}')


def part1(data):

    diff_1_cnt = 0
    diff_3_cnt = 0

    prev_num = 0

    for num in data:

        diff = num - prev_num
        if diff == 1:
            diff_1_cnt += 1
        elif diff == 3:
            diff_3_cnt += 1

        prev_num = num
    
    diff_3_cnt += 1
        
    return diff_1_cnt * diff_3_cnt

def part2(data):

    """no idea why it works tho"""
    
    data = [0] + data + [max(data) + 3]
    differences = [data[i + 1] - data[i] for i in range(len(data) - 1)]

    diff_string = ''.join([str(num) for num in differences])
    diff_strings = diff_string.split('3')

    lens = list(set([len(s) for s in diff_strings]))

    tribonaccies = {i: tribonacci(i) for i in lens}

    return _prod([tribonaccies[len(string)] for string in diff_strings]) 

def tribonacci(i):
    tribonacci_numbers = [1,1,2]
    index = 0
    while index < i:
        tribonacci_numbers.append(sum(tribonacci_numbers[index:]))
        index += 1

    return tribonacci_numbers[i]

def _prod(iterable):
    return reduce(operator.mul, iterable, 1)
    

if __name__ == "__main__":
    main()