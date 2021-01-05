from re import search
from itertools import product
from helpers import readlines

def main():

    data = readlines('inputs/day14_input.txt')
    
    print(part1(data))
    print(part2(data))

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

def part2(data):

    memory = {}
    mask = 'X' * 36

    for line in data:
        split = line.split(' = ')
        if split[0] == 'mask':
            mask = split[1]
        else:
            address = search(r'(?<=\[)[0-9]+(?=\])', split[0])
            address = address.group(0)

            value = int(split[1])
            address_bin = int2bin(int(address))

            #print(f'address:\t{address_bin}')
            #print(f'mask:\t\t{mask}')
            masked_value = put_mask_pt2(address_bin, mask)
            #print(f'result:\t\t{masked_value}')

            #print('\n')
            decoded = decode_addresses(masked_value)
            
            for address in decoded:
                memory[address] = value

    return sum([x for x in memory.values() if x != 0])



def decode_addresses(masked_value):

    all_decoded_addresses = list(_filler(masked_value, 'X'))

    all_decoded_addresses_int = [int(x, 2) for x in all_decoded_addresses]
    
    return all_decoded_addresses_int


def _filler(word, from_char):
    options = [(c,) if c != from_char else ('0','1') for c in word]
    return (''.join(o) for o in product(*options))

def put_mask(value, mask):

    new_value = [char for char in value]

    for i, n in enumerate(mask):

        if n != 'X':
            new_value[i] = n

    return ('').join(new_value)

def put_mask_pt2(value, mask):

    new_value = [char for char in value]

    for i, n in enumerate(mask):

        if n == '1':
            new_value[i] = '1'
        elif n == 'X':
            new_value[i] = 'X'
    
    return ('').join(new_value)


def int2bin(integer, digits=36):
    if integer >= 0:
        return bin(integer)[2:].zfill(digits)
    else:
        return bin(2**digits + integer)[2:]

if __name__ == "__main__":
    main()