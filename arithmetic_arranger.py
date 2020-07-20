def arithmetic_arranger(problems, solve=False):
    # only accept 5 problems max
    if len(problems) > 5:
        return "Error: Too many problems."

    # Declaration of needed varibales
    allowed_operators = ['+', '-']
    padding_between_question = "    "
    line_1 = line_2 = line_3 = ""
    if solve:
        line_4 = ""

    for index, problem in enumerate(problems):
        first, operator, second = problem.split(" ")
        # Check if operator is valid
        if operator not in allowed_operators:
            return "Error: Operator must be '+' or '-'."

        # Check if operand is digit
        try:
            int(first)
            int(second)
        except ValueError:
            return "Error: Numbers must only contain digits."

        # Check operand length
        operand_length = max(len(first), len(second))
        if operand_length > 4:
            return "Error: Numbers cannot be more than four digits."

        required_length = operand_length + 2

        # building up each line
        line_1 += " "*(required_length-len(first)) + first
        line_2 += operator + " "*(required_length-1-len(second)) + second
        line_3 += required_length*'-'

        if solve:
            # calculating for solution
            if operator == '+':
                answer = int(first) + int(second)
            else:
                answer = int(first) - int(second)
            line_4 += (required_length-len(str(answer)))*' ' + str(answer)

        # Adding padding if not last question in list
        if index+1 != len(problems):
            line_1 += padding_between_question
            line_2 += padding_between_question
            line_3 += padding_between_question
            if solve:
                line_4 += padding_between_question

    # Connecting all lines together
    arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3
    if solve:
        arranged_problems += '\n' + line_4
    return arranged_problems
