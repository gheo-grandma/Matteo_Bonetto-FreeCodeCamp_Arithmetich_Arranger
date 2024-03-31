def arithmetic_arranger(problems, show_result=False):
  # Initialize output strings
  first_line = ""
  second_line = ""
  third_line = ""
  result_line = ""

  for problem in problems:
    # Get operands and operators
    first_number = problem.split()[0]
    operator = problem.split()[1]
    second_number = problem.split()[2]

    # Errors handling
    if len(problems) > 5:
      return "Error: too many problems."

    if len(first_number) > 4 or len(second_number) > 4:
      return "Error: Numbers cannot be more than four digits."

    if not first_number.isnumeric() or not second_number.isnumeric():
      return "Error: Numbers must only contain digits."

    if operator != "+" and operator != "-":
      return "Error: Operator must be '+' or '-'."

    # Format lines
    max_length = max(len(first_number), len(second_number))
    first_line += first_number.rjust(max_length + 2) + "    "
    second_line += operator + " " + second_number.rjust(max_length) + "    "
    third_line += "-" * (max_length + 2) + "    "

    # Calculate results
    if show_result:
      if operator == "+":
        result = str(int(first_number) + int(second_number))
      else:
        result = str(int(first_number) - int(second_number))
      result_line += result.rjust(max_length + 2) + "    "

  # Build return string
  arranged_problems = f"{first_line}\n{second_line}\n{third_line}\n{result_line}"

  return arranged_problems
