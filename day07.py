import itertools

def parse_input(input_path):
    """Reads and parses the input data."""
    with open(input_path, "r", encoding="utf-8") as f:
        equations = {}
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Split the line into key and value parts
            parts = line.split(":")
            if len(parts) != 2:
                raise ValueError(f"Invalid line format: {line}")

            # Parse the key and values
            key = int(parts[0].strip())
            values = list(map(int, parts[1].split()))

            # Add the key-value pair to the dictionary
            equations[key] = values

    return equations

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for op, num in zip(operators, numbers[1:]): # Evaluate the expression using current combination
        if op == "+":
            result += num
        elif op == "*":
            result *= num
        elif op == "||":
            result = int(str(result) + str(num))
    return result

def part1(equations):
    """Solves part 1 of the day's puzzle."""
    calibration_result = 0 # Initialise number of possible true values
    operators = ["+", "*"] # Define the operators we will use for this problem

    for target, inputs in equations.items():
        num_gaps = len(inputs) - 1 # Define the number of operations we will be inserting

        all_combinations = itertools.product(operators, repeat=num_gaps) # Generate all permutations of operators
        for combination in all_combinations:
            if evaluate_expression(inputs, combination) == target:
                calibration_result += target
                break

    return calibration_result


def part2(equations):
    """Solves part 2 of the day's puzzle."""
    calibration_result = 0 # Initialise number of possible true values
    operators = ["+", "*", "||"] # Define the operators we will use for this problem

    for target, inputs in equations.items():
        num_gaps = len(inputs) - 1 # Define the number of operations we will be inserting

        all_combinations = itertools.product(operators, repeat=num_gaps) # Generate all permutations of operators
        for combination in all_combinations:
            if evaluate_expression(inputs, combination) == target:
                calibration_result += target
                break

    return calibration_result


def main():
    """Main function to run the day's puzzle."""
    input_path = (
        "inputs/day07.txt"
    )
    data = parse_input(input_path)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
