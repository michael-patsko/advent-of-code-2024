from typing import Tuple, Optional

def parse_input(input_path: str) -> list[list[int]]:
    """Reads and parses the input data."""
    with open(input_path, "r", encoding="utf-8") as f:
        reports: list[list[int]] = [] # Create a list that will hold reports as lists of integers
        for line in f.read().splitlines():
            report = list(map(int, line.split()))
            reports.append(report)
        return reports

def report_is_safe(report: list[int]) -> Tuple[bool, Optional[int]]:
    """Determines if a report is safe."""
    # Existing logic to determine safety
    increasing = False
    decreasing = False

    # Determine if report is increasing or decreasing
    if report[0] < report[1]:
        increasing = True
    elif report[0] > report[1]:
        decreasing = True
    else:
        return False, 0

    for i in range(0, len(report) - 1): # Loop through adjacent levels and check conditions
        if report[i] <= report[i + 1] and decreasing:
            return False, i
        if report[i] >= report[i + 1] and increasing:
            return False, i
        if abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
            return False, i

    return True, None

def remove_element(lst: list[int], index: int) -> list[int]:
    """Returns a new list with the element at the specified index removed."""
    return lst[:index] + lst[index + 1:]

def part1(reports: list[list[int]]) -> int:
    """Solves part 1 of the day's puzzle."""
    safety_score = 0 # Initialise safety score

    for report in reports:
        is_safe, _ = report_is_safe(report)

        if is_safe: # Check if reports are safe
            safety_score += 1

    return safety_score

def part2(reports: list[list[int]]) -> int:
    """Solves part 2 of the day's puzzle."""
    safety_score = 0

    for report in reports:
        is_safe, _ = report_is_safe(report)
        if is_safe:
            safety_score += 1
            continue

        # Try removing each level one at a time
        for i in range(len(report)):
            modified_report = remove_element(report, i)
            is_safe_modified, _ = report_is_safe(modified_report)
            if is_safe_modified:
                safety_score += 1
                break  # No need to check other indices if one works

    return safety_score

def main():
    """Main function to run the day's puzzle."""
    input_path = (
        "inputs/day02.txt"  # Update to the correct input file path
    )
    data = parse_input(input_path)

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
