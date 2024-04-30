from algo import build_weight_matrix_and_graph , get_neighbors_and_degrees , color_graph ,get_first_node_color , get_ordered_adjacency_courses_of_ci , get_smallest_available_color
import networkx as nx
import matplotlib.pyplot as plt
import math





def plot_graph_with_timeslots(G, color_assignments, num_time_slots):
    pos = nx.spring_layout(G)

    # Define colors for time slots
    colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightyellow']

    for i, node in enumerate(G.nodes()):
        if color_assignments[node] is not None:
            day = color_assignments[node] // num_time_slots
            time_slot = color_assignments[node] % num_time_slots
            color = colors[time_slot]
            # Set node shape based on the assigned day
            if day == 0:
                node_shape = 's'  # Square
            else:
                node_shape = 'o'  # Circle
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color=color, node_shape=node_shape, node_size=500)
            nx.draw_networkx_labels(G, pos, labels={node: f"{courses[node]}\nDay {day+1}, Slot {time_slot+1}"}, font_size=12, font_family="sans-serif")

    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='lightgray')
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
    plt.title("Exam Schedule", fontsize=16, fontweight="bold")
    plt.show()


# Example usage
courses = ['Math101', 'Math102', 'Math103', 'Math104', 'Math105', 'Math106', 'Math107', 'Math108', 'Math109', 'Math110']

sections = { 'Math101': 3, 'Math102': 2, 'Math103': 2, 'Math104': 2, 'Math105': 1, 'Math106': 2, 'Math107': 2, 'Math108': 1, 'Math109': 2, 'Math110': 1 }

students = { 'S1': ['Math101', 'Math102', 'Math103'], 'S2': ['Math101', 'Math104', 'Math105'], 'S3': ['Math101', 'Math106', 'Math107'], 'S4': ['Math102', 'Math104', 'Math108'], 'S5': ['Math102', 'Math106', 'Math109'], 'S6': ['Math103', 'Math105', 'Math110'], 'S7': ['Math103', 'Math107', 'Math108'], 'S8': ['Math103', 'Math109', 'Math110'], 'S9': ['Math104', 'Math105', 'Math106'], 'S10': ['Math104', 'Math107', 'Math109'], 'S11': ['Math105', 'Math108', 'Math110'], 'S12': ['Math106', 'Math107', 'Math108'], 'S13': ['Math106', 'Math109', 'Math110'], 'S14': ['Math107', 'Math108', 'Math109'], 'S15': ['Math107', 'Math109', 'Math110'], }

weight_matrix, graph, concurrency_level = build_weight_matrix_and_graph(courses, sections, students)
neighbors, degrees = get_neighbors_and_degrees(graph)

num_time_slots = 3
num_days = 2
color_assignments = color_graph(weight_matrix, graph, concurrency_level, num_time_slots, num_days)

if color_assignments is not None:
    for i, color in enumerate(color_assignments):
        if color is not None:
            print(f"Course {courses[i]}: Day {color // num_time_slots}, Time Slot {color % num_time_slots}")


# # Visualize the graph
G = nx.Graph()
G.add_nodes_from(range(len(courses)))

for i, j in enumerate(graph):
    for k in j:
        G.add_edge(i, k, weight=weight_matrix[i][k])


plot_graph_with_timeslots(G, color_assignments, num_time_slots)



