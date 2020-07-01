from math import sqrt
from heapq import *


def heuristic(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def shortest_path(M, start, goal):
    """
    A* search algorithm to find the shortest path
    Args:
        M: map model (map_10 or map_40)
        start: start node - int
        goal: target node - int

    Returns:
        path: the shortest path - list
    """

    print("shortest path called")

    came_from = {}
    g_score = {}
    came_from[start] = None
    g_score[start] = 0
    open_heap = []
    heappush(open_heap, (0, start))

    while open_heap:
        current = heappop(open_heap)[1]

        if current == goal:
            break

        for neighbor in M.roads[current]:
            new_g_score = g_score[current] + heuristic(M.intersections[current], M.intersections[neighbor])

            if neighbor not in g_score or new_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = new_g_score
                heappush(open_heap, (new_g_score, neighbor))

    optimal_path = []
    node = goal

    while came_from[node]:
        optimal_path.append(node)
        node = came_from[node]
    else:
        optimal_path.append(node)

    optimal_path.reverse()

    return optimal_path
