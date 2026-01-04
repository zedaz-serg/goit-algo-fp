import heapq

def dejkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2, 'E': 4},
    'D': {'B': 3, 'C': 2, 'F': 6},
    'E': {'C': 4, 'F': 1},
    'F': {'D': 6, 'E': 1}
}

start_node = 'A'
shortest_paths = dejkstra(graph, start_node)

for vertex, distance in shortest_paths.items():
    print(f"{vertex}: {distance}")