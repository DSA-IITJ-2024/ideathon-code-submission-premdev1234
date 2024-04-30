<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/en/8/81/Indian_Institute_of_Technology_Jodhpur_Logo.svg" width="250" />
</p>

<p align="center">
    <h1 align="center">DSA_IDEATHON</h1>
</p>


# Exam Scheduling Algorithm

This repository contains an algorithm implemented in Python for scheduling exams based on course dependencies and student concurrency.

## Introduction

The algorithm takes into account the following parameters:

- **Courses**: A list of courses offered.
- **Sections**: The number of sections available for each course.
- **Students**: Mapping of students to the courses they are enrolled in.
- **Concurrency Level**: The number of students that can take an exam concurrently.
- **Time Slots**: The number of time slots available per day.
- **Days**: The number of days available for scheduling exams.

## Files

### `algo.py`

This file contains the implementation of the exam scheduling algorithm. It includes the following functions:

- `build_weight_matrix_and_graph`: Builds the weight matrix and graph representing dependencies between courses.
- `get_neighbors_and_degrees`: Calculates the neighbors and degrees of nodes in the graph.
- `color_graph`: Assigns colors (time slots) to courses based on dependencies and concurrency.
- `get_first_node_color`: Assigns the first available color (time slot) for the initial node.
- `get_ordered_adjacency_courses_of_ci`: Gets the adjacency list of a node sorted by degree and weight.
- `get_smallest_available_color`: Finds the smallest available color (time slot) for a node considering dependencies and concurrency.

### `test.py`

This file demonstrates the usage of the algorithm by providing example data and visualizing the exam schedule using NetworkX and Matplotlib.

## Sample Output

![Exam Schedule](test.png)

## Usage

To use the exam scheduling algorithm:

1. Ensure you have Python installed on your system.
2. Clone this repository.
3. Modify the `courses`, `sections`, and `students` variables in `test.py` to match your data.
4. Run `test.py` to generate the exam schedule and visualize it.

## Dependencies

- Python 3.x
- NetworkX
- Matplotlib


