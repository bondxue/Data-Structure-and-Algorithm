import heapq
import math


def shortest_path(M, start, goal):
    print("shortest path called")
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    frontier = [(0, start)]

    while len(frontier) > 0:
        node = heapq.heappop(frontier)[1]

        if node == goal:
            break

        for neighbor in M.roads[node]:
            path_cost = distance(M.intersections[node], M.intersections[neighbor])
            new_cost = cost_so_far[node] + path_cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                came_from[neighbor] = node
                cost_so_far[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor))

    return best_route(came_from, start, goal)


def distance(start, end):
    # path cost is distance between two points
    return math.hypot(end[0] - start[0], end[1] - start[1])


def best_route(came_from, start, goal):
    # traverse backwards to find optimal path
    node = goal
    path = []

    if node not in came_from:
        print(f"Node: {node} not found in map.")
        return

    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()
    print(path)
    return path
