def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    top_lines = []
    bottom_lines = []
    dash_lines = []
    result_lines = []
    
    for problem in problems:
        operand_one, operator, operand_two = problem.split()

        if operator not in ['+','-']:
            return "Error: Operator must be '+' or '-'."
        if not (operand_one.isdigit() and operand_two.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(operand_one) > 4 or len(operand_two) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(operand_one), len(operand_two)) + 2
        top_line = operand_one.rjust(width)
        bottom_line = operator + ' ' + operand_two.rjust(width - 2)
        dash_line = '-' * width
        
        top_lines.append(top_line)
        bottom_lines.append(bottom_line)
        dash_lines.append(dash_line)

        if show_answers:
            if operator == '+':
                result = str(int(operand_one) + int(operand_two))
            else:
                result = str(int(operand_one) - int(operand_two))
            result_line = result.rjust(width)
            result_lines.append(result_line)
    
    arranged_problems = "    ".join(top_lines) + "\n" + "    ".join(bottom_lines) + "\n" + "    ".join(dash_lines)
    
    if show_answers:
        arranged_problems += "\n" + "    ".join(result_lines)
    
    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
