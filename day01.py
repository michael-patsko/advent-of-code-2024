def parse_input(input_path: str) -> tuple[list[int], list[int]]:
    """Reads and parses the input data into two lists of integers."""
    with open(input_path, "r", encoding="utf-8") as f:
        left_list, right_list = [], []
        for line in f.read().splitlines():
            num1, num2 = map(int, line.split())  # Split the line and convert to integers
            left_list.append(num1)
            right_list.append(num2)
        return left_list, right_list



def part1(data: tuple[list[int], list[int]]) -> int:
    """Solves part 1 of the day's puzzle."""
    left_list, right_list = data

    left_list.sort()
    right_list.sort() # Sort the lists

    final_sum = 0 # Initialise final answer
    for i, value in enumerate(left_list):
        final_sum += abs(value - right_list[i])

    return final_sum

def part2(data):
    """Solves part 2 of the day's puzzle."""
    left_list, right_list = data

    similarity_score = 0 # Initialise similarity score

    right_list_counts = {}
    for value in right_list: # Count occurence of each value in right list
        if value in right_list_counts:
            right_list_counts[value] += 1
        else:
            right_list_counts[value] = 1

    for value in left_list: # Build similarity score
        if value in right_list_counts:
            similarity_score += value * right_list_counts[value] 

    return similarity_score

def main():
    """Main function to run the day's puzzle."""
    input_path = (
        "inputs/day01.txt"
    )
    data = parse_input(input_path)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
