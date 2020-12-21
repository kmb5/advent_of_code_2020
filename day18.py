import re
from helpers import readlines

def main():

    data = readlines('inputs/day18_input.txt')

    sum_of_results = [0, 0] 
    # both pt 1 and pt2

    for line in data:
        sum_of_results[0] += evaluate(line)
        sum_of_results[1] += evaluate_pt2(line)

    print(f'pt1: {sum_of_results[0]}, pt2: {sum_of_results[1]}')

    



def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
 
def is_name(str):
    return re.match("\w+", str)
 
def peek(stack):
    return stack[-1] if stack else None
 
def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    values.append(eval("{0}{1}{2}".format(left, operator, right)))
 
def greater_precedence(op1, op2):
    # not real life but these are the rules from the exercise
    precedences = {'+' : 1, '*' : 0}
    return precedences[op1] > precedences[op2]
 
def evaluate_pt2(expression):
    tokens = re.findall("[+/*()-]|\d+", expression)
    values = []
    operators = []
    for token in tokens:
        if is_number(token):
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = peek(operators)
            while top is not None and top != '(':
                apply_operator(operators, values)
                top = peek(operators)
            operators.pop() # Discard the '('
        else:
            # Operator
            top = peek(operators)
            while top is not None and top not in "()" and greater_precedence(top, token):
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        apply_operator(operators, values)
 
    return values[0]

def evaluate(expression):
    tokens = re.findall("[+/*()-]|\d+", expression)
    values = []
    operators = []
    for token in tokens:
        if is_number(token):
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = peek(operators)
            while top is not None and top != '(':
                apply_operator(operators, values)
                top = peek(operators)
            operators.pop() # Discard the '('
        else:
            # Operator
            top = peek(operators)
            while top is not None and top not in "()":
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        apply_operator(operators, values)
 
    return values[0]

if __name__ == "__main__":
    main()