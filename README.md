# Notes on [Advent of Code 2024](https://adventofcode.com/2024) :christmas_tree: <!-- omit from toc -->

###### By Michael Patsko

> :construction: **Work in Progress**: This README is currently under development. The content and structure will change as I continue to update it. Feel free to check back later when it's a little tidier. :smile:

---

## Project Overview <!-- omit from toc -->

Personal repository for solving [Advent of Code](https://adventofcode.com/) challenges in 2024. This year's goal: explore elegant solutions, improve algorithmic thinking, and have fun with coding puzzles! :rocket:

## Table of Contents <!-- omit from toc -->

- [Things Learned](#things-learned)
- [Things to Improve](#things-to-improve)
- [Reflections on my Approach](#reflections-on-my-approach)
- [Solutions](#solutions)
  - [Day 1: Historian Hysteria :mag\_right:](#day-1-historian-hysteria-mag_right)

# Things Learned

# Things to Improve

# Reflections on my Approach

# Solutions

## Day 1: Historian Hysteria :mag_right:

### Part 1

The elves began this year's Advent of Code with a fascinating problem involving two lists of location IDs from the Chief Historian's office. Our task was to calculate the total distance between these two lists by pairing the smallest numbers together, the next smallest, and so on, then summing up the absolute differences of these pairs.

At first glance, it seemed straightforward—sort both lists, pair them up, calculate the distances, and sum them. But as always, the devil is in the details.

#### My Solution

I started by parsing the input into two separate lists using the following function:

```py
def parse_input(input_path: str) -> tuple[list[int], list[int]]:
    """Reads and parses the input data into two lists of integers."""
    with open(input_path, "r", encoding="utf-8") as f:
        left_list, right_list = [], []
        for line in f.read().splitlines():
            num1, num2 = map(int, line.split())
            left_list.append(num1)
            right_list.append(num2)
        return left_list, right_list
```

This function reads each line of the input file, splits the numbers, and appends them to `left_list` and `right_list` respectively.

Next, I sorted both lists to ensure that the smallest numbers would be paired together:

```py
left_list.sort()
right_list.sort()
```

To calculate the total distance, I initialised a variable `final_sum` and used a loop to iterate over the indices of the sorted lists:

```py
final_sum = 0  # Initialise the total distance
for i, value in enumerate(left_list):
    final_sum += abs(value - right_list[i])
```

Here, `enumerate(left_list)` allows me to access both the index `i` and the value `value` from `left_list`. I then compute the absolute difference between `value` and the corresponding element in `right_list` at the same index `i`, adding it to `final_sum`.

Here's the complete function for Part 1:

```py
def part1(data: tuple[list[int], list[int]]) -> int:
    """Solves part 1 of the day's puzzle."""
    left_list, right_list = data

    left_list.sort()
    right_list.sort()  # Sort the lists

    final_sum = 0  # Initialise the total distance
    for i, value in enumerate(left_list):
        final_sum += abs(value - right_list[i])

    return final_sum
```

Running this code, I obtained the correct total distance for my input: **1223326**.

### Part 2

Just when I thought I had the lists figured out, Part 2 introduced a new challenge. This time, instead of calculating distances, we needed to compute a similarity score based on how often each number from the left list appears in the right list. The score is calculated by multiplying each number by the number of times it appears in the right list and summing these up.

Time to dive back into the code. :dizzy_face:

#### My Solution

First, I needed to count the occurrences of each number in the right list. Instead of using Python's `Counter` from the `collections` module, I decided to build the counts manually:

```py
right_list_counts = {}
for value in right_list:
    if value in right_list_counts:
        right_list_counts[value] += 1
    else:
        right_list_counts[value] = 1
```

This loop creates a dictionary `right_list_counts` where each key is a number from the right list, and each value is the count of how many times it appears.

Next, I initialised the similarity score and iterated over the left list:

```py
similarity_score = 0  # Initialise the similarity score

for value in left_list:
    if value in right_list_counts:
        similarity_score += value * right_list_counts[value]
```

For each number in the left list, I checked if it exists in `right_list_counts`. If it does, I multiplied the number by its count in the right list and added it to `similarity_score`.

Here's the complete function for Part 2:

```py
def part2(data):
    """Solves part 2 of the day's puzzle."""
    left_list, right_list = data

    similarity_score = 0  # Initialise the similarity score

    right_list_counts = {}
    for value in right_list:  # Count occurrences of each value in right list
        if value in right_list_counts:
            right_list_counts[value] += 1
        else:
            right_list_counts[value] = 1

    for value in left_list:  # Build similarity score
        if value in right_list_counts:
            similarity_score += value * right_list_counts[value]

    return similarity_score
```

I ran the code, and success! Got the correct similarity score. :tada:

---

This puzzle was a great way to kick off Advent of Code 2024. It reminded me of the importance of carefully analysing the problem and choosing the right data structures.

In Part 1, sorting the lists and using a simple loop with indexing allowed me to accurately calculate the total distance. In Part 2, manually building a dictionary to count occurrences was a good exercise in understanding how frequency counts can be utilised without relying on external libraries.

One thing I could improve is the efficiency of the counting process. Using `defaultdict` from the `collections` module or even `Counter` could make the code cleaner and possibly more efficient. However, manually implementing the counts gave me a deeper understanding of what's happening under the hood.

In future puzzles, I might consider trying out other programming languages like TypeScript or even Rust to challenge myself further. Only time will tell! :grin:

Looking forward to the challenges ahead!

---