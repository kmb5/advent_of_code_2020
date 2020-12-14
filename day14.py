from re import search
from helpers import readlines

def main():

    data = readlines('inputs/day14_input.txt')
    
    print(part1(data))

def part1(data):

    memory = {}
    mask = 'X' * 36

    for line in data:

        split = line.split(' = ')

        if split[0] == 'mask':
            mask = split[1]
        else:
            # extract all numbers between the []
            address = search(r'(?<=\[)[0-9]+(?=\])', split[0])
            address = address.group(0)

            value = int(split[1])


            masked_value = put_mask(int2bin(value), mask)

            memory[address] = int(masked_value, 2)

    return sum([x for x in memory.values() if x != 0])



    
    print(mask)


def put_mask(value, mask):

    new_value = [char for char in value]

    for i, n in enumerate(mask):

        if n != 'X':
            new_value[i] = n

    return ('').join(new_value)


def int2bin(integer, digits=36):
    if integer >= 0:
        return bin(integer)[2:].zfill(digits)
    else:
        return bin(2**digits + integer)[2:]

if __name__ == "__main__":
    main()