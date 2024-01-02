def arithmetic_arranger(problems, solve=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    # Initialize list to store each line of the arranged problems
    first_line = []
    second_line = []
    third_line = []
    if solve:
        fourth_line = []
    # Iterate through the problems
    for problem in problems:
        # Split the problem in a list of strings
        splitted = problem.split()
        # Check if the operator is not '+' or '-'
        if "+" not in problem and "-" not in problem:
            return "Error: Operator must be '+' or '-'."
        # Check if the numbers contain only digits
        if not splitted[0].isdigit() or not splitted[2].isdigit():
            return "Error: Numbers must only contain digits."
        # Extract the length of the numbers
        len1, len2 = len(splitted[0]), len(splitted[2])
        # Check if the numbers are not more than four digits
        if len1 > 4 or len2 > 4:
            return "Error: Numbers cannot be more than four digits."
        # Store the length of the longest number
        max_len = max(len1, len2)
        # Arrange the problem with the specific format for each line:
        # 1. First line: the first number should be right alligned and occupying max_len + 1 space
        # 2. Second line: the operator on the left, one space, and the second number right alligned and occupying max_len space
        # 3. Third line: dashes occupying max_len + 2 spaces
        first_line.append(splitted[0].rjust(max_len + 2))
        second_line.append(f"{splitted[1]} {splitted[2].rjust(max_len)}")
        third_line.append("-" * (max_len + 2))
        # If the problem should be solved add a fourth line with the solution right alligned and occupying max_len + 2 spaces
        if solve:
            fourth_line.append(str(eval(problem)).rjust(max_len + 2))

    # Join every list with 4 spaces between each element
    first_line = 4 * " ".join(first_line)
    second_line = 4 * " ".join(second_line)
    third_line = 4 * " ".join(third_line)
    if solve:
        fourth_line = 4 * " ".join(fourth_line)

    # Join all the list together with a new line between each one
    arranged_problems = first_line + "\n" + second_line + "\n" + third_line
    if solve:
        arranged_problems += "\n" + fourth_line

    return arranged_problems
