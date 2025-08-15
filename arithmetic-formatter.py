def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_row = []
    second_row = []
    dash_row = []
    answer_row = []

    for problem in problems:
        left, op, right = problem.split()

        # Operator validation
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Digit validation
        if not left.isdigit() or not right.isdigit():
            return 'Error: Numbers must only contain digits.'

        # Length validation
        if len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate answer
        if op == '+':
            result = int(left) + int(right)
        else:
            result = int(left) - int(right)

        # Determine width
        width = max(len(left), len(right)) + 2

        # Format each row
        first_row.append(left.rjust(width))
        second_row.append(op + right.rjust(width - 1))
        dash_row.append('-' * width)
        answer_row.append(str(result).rjust(width))

    # Build arranged string
    arranged = '    '.join(first_row) + '\n' + '    '.join(second_row) + '\n' + '    '.join(dash_row)
    if show_answers:
        arranged += '\n' + '    '.join(answer_row)

    return arranged


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')