# -*- coding: utf-8 -*-
"""a_star_search

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rsk-TJnVIXa69Cj_ER0tdkSKb7KevDfk
"""

from queue import PriorityQueue

def a_star_search(graph, heuristic, start, goal):
    frontier = PriorityQueue()
    frontier.put((0 + heuristic[start], start))
    explored = set()
    path = {}
    g_cost = {start: 0}

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            print("Simpul tujuan ditemukan!")
            route = reconstruct_path(path, start, goal)
            print("Jalur terbaik:", route)
            return route

        explored.add(current)

        for neighbor, cost in graph[current]:
            tentative_g_cost = g_cost[current] + cost

            if neighbor not in explored or tentative_g_cost < g_cost.get(neighbor, float('inf')):
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                frontier.put((f_cost, neighbor))
                path[neighbor] = current

    print("Simpul tujuan tidak ditemukan!")
    return None

def reconstruct_path(path, start, goal):
    current = goal
    route = [current]
    while current != start:
        current = path[current]
        route.append(current)
    route.reverse()
    return route

# Heuristic values from the image
heuristic = {
    'S': 6, 'A': 4, 'B': 3, 'C': 3, 'D': 1, 'G': 0
}

# Updated Graph structure
graph = {
    'S': [('A', 3), ('B', 2)],
    'A': [('B', 1), ('D', 5)],
    'B': [('C', 2), ('D', 3)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 1)],
    'G': []
}

# Starting and goal nodes
start_node = 'S'
goal_node = 'G'

a_star_search(graph, heuristic, start_node, goal_node)