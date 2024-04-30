import heapq
import matplotlib.pyplot as plt

def build_weight_matrix_and_graph(courses, sections, students):
    # Build weight matrix and graph
    num_courses = len(courses)
    weight_matrix = [[0] * num_courses for _ in range(num_courses)]
    graph = [[] for _ in range(num_courses)]
    concurrency_level = [sections[course] for course in courses]

    for student, course_list in students.items():
        for i in range(len(course_list)-1):
            for j in range(i+1, len(course_list)):
                course1, course2 = course_list[i], course_list[j]
                weight_matrix[courses.index(course1)][courses.index(course2)] += 1
                weight_matrix[courses.index(course2)][courses.index(course1)] += 1
                graph[courses.index(course1)].append(courses.index(course2))
                graph[courses.index(course2)].append(courses.index(course1))

    return weight_matrix, graph, concurrency_level


def get_neighbors_and_degrees(graph):
    neighbors = [[] for _ in range(len(graph))]
    degrees = [0] * len(graph)

    for i in range(len(graph)):
        for j in graph[i]:
            neighbors[i].append(j)
            degrees[i] += 1

    return neighbors, degrees

def color_graph(weight_matrix, graph, concurrency_level, num_time_slots, num_days):
    # Sort nodes based on degree and weight
    
    # print("Length of degrees:", len(degrees))
    # print("Length of graph:", len(graph))
    # print("Shape of weight_matrix:", len(weight_matrix), "x", len(weight_matrix[0]))
    # nodes = sorted(range(len(graph)), key=lambda x: (-degrees[x], -weight_matrix[x][x], x))
    # nodes = sorted(range(len(graph)), key=lambda x: (-degrees[x], -weight_matrix[x][x] if x < len(weight_matrix) else 0, x))
    nodes = sorted(range(len(graph)), key=lambda x: (x, -sum(weight_matrix[x]), x))

    color_assignments = [None] * len(graph)
    days_assigned = [0] * len(graph)

    # Function to check if a color is valid for a node
    def is_valid_color(node, color):
        for neighbor in graph[node]:
            if color_assignments[neighbor] == color:
                return False
        return True

    # Function to find the smallest available color for a node
    def find_smallest_available_color(node):
        for color in range(num_days * num_time_slots):
            if is_valid_color(node, color):
                return color
        return None

    # Assign colors to nodes
    for node in nodes:
        if color_assignments[node] is not None:
            continue

        # Get first available color
        if node == 0:
            color_assignments[node] = get_first_node_color(node, concurrency_level, num_time_slots, num_days)
            if color_assignments[node] is None:
                return None
        else:
            color_assignments[node] = find_smallest_available_color(node)
            if color_assignments[node] is None:
                return None

        # Color neighbors
        for neighbor in graph[node]:
            if color_assignments[neighbor] is None:
                days_assigned[neighbor] = max(days_assigned[neighbor], days_assigned[node] + 1)
                color_assignments[neighbor] = find_smallest_available_color(neighbor)
                if color_assignments[neighbor] is None:
                    return None

    return color_assignments


def get_first_node_color(node, concurrency_level, num_time_slots, num_days):
    for day in range(num_days):
        for time_slot in range(num_time_slots):
            if concurrency_level[node] > 0:
                concurrency_level[node] -= 1
                return day * num_time_slots + time_slot
    return None


def get_ordered_adjacency_courses_of_ci(node, graph):
    # Get the adjacency list of the given node
    adjacency_list = graph[node]

    # Sort the adjacency list by degree and weight
    adjacency_list = sorted(adjacency_list, key=lambda x: (-degrees[x], -weight_matrix[x][x], x))

    return [course_index for course_index in adjacency_list if course_index < len(graph)]


    return adjacency_list

def get_smallest_available_color(node, concurrency_level, num_time_slots, num_days, color_assignments, days_assigned):
    # Get adjacency list and sort by degree and weight
    adjacency_list = get_ordered_adjacency_courses_of_ci(node, graph)
    adjacency_list = sorted(adjacency_list, key=lambda x: (-degrees[x], -weight_matrix[x][x],x))

    for day in range(num_days):
        for time_slot in range(num_time_slots):
            valid = True
            for neighbor in adjacency_list:
                if color_assignments[neighbor] is not None:
                    color = color_assignments[neighbor]
                    if (color // num_time_slots) == day and (color % num_time_slots) == time_slot:
                        valid = False
                        break
            if valid and concurrency_level[node] > 0:
                concurrency_level[node] -= 1
                return day * num_time_slots + time_slot

    return None
