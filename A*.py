import heapq
def astar(graph, start, goal):
    queue = [(0, start)]
    cost_so_far = {start: 0}
    came_from = {}
    while queue:
        current = heapq.heappop(queue)[1]
        if current == goal:
            return came_from
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(queue, (priority, next))
                came_from[next] = current
    return came_from
