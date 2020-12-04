import re
from helpers import readfile

def main():
    """Day 4 solution"""

    data = readfile('day4_input.txt')
    passports = parse_passports(data)

    part1_solution = part1(passports)
    part2_solution = part2(passports)

    print(f'Part 1 solution is {part1_solution}')
    print(f'Part 2 solution is {part2_solution}')

def part1(passports: list) -> int:
    """Day 4, first part

    Objective: Find the number of valid passports.
    A passport is valid if it contains all of the following
    attributes: byr, iyr, eyr, hgt, hcl, ecl and pid

    Any other attributes can be ignored and the password is still
    considered valid. The values can be anything.

    Parameters
    ----------
    passports : list
        A list of passports where each passport is a dict
        of attribute-value pairs

    Returns
    -------
    num_valid_passports : int
        The number of valid passports in the list

    """

    num_valid_passports = 0

    required_attributes = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]

    for passport in passports:

        all_required_attributes_there = False

        keys = passport.keys()

        for attribute in required_attributes:
            if attribute not in keys:
                # At least one required attribute is missing,
                # passport is definitely invalid
                all_required_attributes_there = False
                break
            # This attribute is there, but we can't
            # yet consider the whole passport valid
            all_required_attributes_there = True

        # We checked all attributes (or found an invalid one),
        # if the value is still true it means the passport is valid.
        if all_required_attributes_there:
            num_valid_passports += 1

    return num_valid_passports

def part2(passports: list) -> int:
    """Day 4, second part.

    Objective:
    Find the number of valid passports within the list.
    For a passport to be valid it has to pass ALL the following conditions:
    - byr has to be between 1920 and 2002 inclusive
    - iyr has to be between 2010 and 2020 inclusive
    - eyr has to be between 2020 and 2030 inclusive
    - hgt has to be a number followed by either cm or in:
        ~ if cm, the number must be at least 150 and at most 193
        ~ if in, the number must be at least 59 and at most 76
    - hcl has to be a # followed by exactly six characters 0-9 or a-f
    - ecl has to be exactly one of: amb blu brn gry grn hzl oth
    - pid has to be a nine-digit number

    Any other attributes can be safely ignored and the password is still
    considered valid as long as all attributes above are PRESENT and VALID.

    Parameters
    ----------
    passports : list
        A list of passports where each passport is a dict
        of attribute-value pairs

    Returns
    -------
    num_valid_passports : int
        The number of valid passports in the list

    """

    num_valid_passports = 0

    # Regex for matching hcl
    # eg. '#123abc' is valid, but '#123abz' and '123abc' are not
    hcl_regex = r'#[0-9a-f]{6}'

    # All requirements are functions that return True
    # if the requirement is met and False otherwise
    # The functions will be called when the requirements are
    # being checked in the loop below
    requirements = {
        'byr': lambda x: (1920 <= int(x) <= 2002),
        'iyr': lambda x: (2010 <= int(x) <= 2020),
        'eyr': lambda x: (2020 <= int(x) <= 2030),
        'hgt': _validate_height,
        'hcl': lambda x: (re.fullmatch(hcl_regex, x)),
        'ecl': lambda x: (x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
        'pid': lambda x: (len(x) == 9)
    }

    for passport in passports:

        all_requirements_match = False

        for attibute in requirements:
            try:
                value_to_check = passport[attibute]

                # call the corresponding function with the value to check
                if requirements[attibute](value_to_check):
                    # This attribute meets requirements, but we can't
                    # yet consider the whole passport valid
                    all_requirements_match = True
                else:
                    # This attribute doesn't meet the requirement,
                    # the whole passport is definitely invalid
                    all_requirements_match = False
                    break
            except KeyError:
                # This attribute is not in the passport at all,
                # the whole passport is definitely invalid
                all_requirements_match = False
                break

        if all_requirements_match:
            # We checked all attributes (or found an invalid one),
            # if the value is still true it means the passport is valid.
            num_valid_passports += 1
        
    return num_valid_passports

def parse_passports(data: str) -> list:
    """Parses the batch data and
    returns it as a list of dicts
    where each dict is an attribute-value pair

    Parameters
    ----------
    data : str
        The data to parse

    Returns
    -------
    all_passports : list
        A list of dicts with all passports

    """

    # each passport is separated by a blank line
    data = data.split('\n\n')

    # each passport can contain newlines which can be
    # ignored, I convert to space because space is what
    # separates the other attributes as well
    data = [x.replace('\n', ' ') for x in data]
    
    all_passports = []

    for passport in data:
        passport_dict = {}
        pairs = passport.split(' ')
        for pair in pairs:
            attribute, value = pair.split(':')
            passport_dict[attribute] = value
        all_passports.append(passport_dict)
    
    return all_passports

def _validate_height(height: str) -> bool:
    """Helper function to validate height.
    Height is valid if it:
    - contains 'in' and is between 59 and 76 inclusive
    - contins 'cm' and is between 150 and 193 inclusive

    Parameters
    ----------
    height : str
        The height to validate
    bool : bool
        True if height is valid, false otherwise

    """

    if 'in' in height:
        height = int(height.replace('in', ''))
        return 59 <= height <= 76
    if 'cm' in height:
        height = int(height.replace('cm', ''))
        return 150 <= height <= 193
    return False

if __name__ == "__main__":
    main()