import re

def parse_input(input_path):
    """Reads and parses the input data."""
    with open(input_path, "r", encoding="utf-8") as f:
        return f.read().strip()


def part1(data):
    """Solves part 1 of the day's puzzle."""
    instructions = re.findall(r"mul\(\d+,\d+\)", data) # Use RegEx to extract mul instructions

    final_result = 0 # Initialise final result
    for instruction in instructions: # Apply mul operators
        num1, num2 = [int(item) for item in re.findall(r"\d+", instruction)]
        final_result += num1 * num2

    return final_result


def part2(data):
    """Solves part 2 of the day's puzzle."""
    instructions = re.findall(r"(?:mul\(\d+,\d+\)|do\(\)|don't\(\))", data) # Extract relevant instructions

    final_result = 0 # Initialise output result
    enabled = True # Initialise enabled condition

    for instruction in instructions:
        match = re.search(r".+(?=\()", instruction) # Determine what kind of instruction this is
        if match:
            process = match.group()
        else:
            raise ValueError(f"Process could not be parsed from instruction: {instruction}")

        if process == "do": # Implement instruction conditions
            enabled = True
        elif process == "don't":
            enabled = False
        elif process == "mul" and enabled:
            num1, num2 = [int(item) for item in re.findall(r"\d+", instruction)]
            final_result += num1 * num2

    return final_result


def main():
    """Main function to run the day's puzzle."""
    input_path = (
        "inputs/day03.txt"
    )
    data = parse_input(input_path)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
